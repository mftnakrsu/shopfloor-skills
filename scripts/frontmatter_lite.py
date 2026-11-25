import datetime
import json
import re

BLOCK_INDICATORS = (">", ">-", "|", "|-")
_KEY = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:[ ]+(.*))?$")
_INT = re.compile(r"^[-+]?[0-9]+$")
_FLOAT = re.compile(r"^[-+]?([0-9]+\.[0-9]*|\.[0-9]+|[0-9]+(\.[0-9]*)?[eE][-+]?[0-9]+)$")
_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
_FORBIDDEN_START = tuple("&*!%@`{")


class FrontmatterError(ValueError):
    pass


def split(text):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise FrontmatterError("file must start with a '---' line")
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            return "".join(lines[1:i]), "".join(lines[i + 1:])
    raise FrontmatterError("frontmatter has no closing '---' line")


def read(path):
    head, body = split(path.read_text(encoding="utf-8"))
    return parse(head), body


def parse(text):
    data = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line, number = lines[i], i + 1
        i += 1
        if "\t" in line:
            raise FrontmatterError(f"line {number}: tabs are not allowed")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            raise FrontmatterError(f"line {number}: unexpected indentation")
        match = _KEY.match(line)
        if not match:
            raise FrontmatterError(f"line {number}: expected 'key: value'")
        key, rest = match.group(1), (match.group(2) or "").strip()
        if key in data:
            raise FrontmatterError(f"line {number}: duplicate key '{key}'")
        if rest.startswith("#"):
            rest = ""
        indicator = rest.split(" #", 1)[0].strip()
        if indicator in BLOCK_INDICATORS:
            block, i = _indented(lines, i)
            data[key] = _block_scalar(block, indicator)
        elif rest == "":
            block, i = _indented(lines, i)
            data[key] = _mapping(block, key) if block else None
        else:
            data[key] = _value(rest, f"line {number}")
    return data


def dump(data):
    lines = []
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{key}:")
            lines.extend(f"  {k}: {_scalar(v)}" for k, v in value.items())
        else:
            lines.append(f"{key}: {_scalar(value)}")
    return "\n".join(lines) + "\n"


def _indented(lines, i):
    block = []
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith(" ")):
        if "\t" in lines[i]:
            raise FrontmatterError(f"line {i + 1}: tabs are not allowed")
        block.append(lines[i])
        i += 1
    while block and not block[-1].strip():
        block.pop()
    return block, i


def _block_scalar(block, indicator):
    if not block:
        return ""
    indent = min(len(line) - len(line.lstrip(" ")) for line in block if line.strip())
    rows = [line[indent:].rstrip() if line.strip() else "" for line in block]
    text = _fold(rows) if indicator.startswith(">") else "\n".join(rows)
    return text if indicator.endswith("-") else text + "\n"


def _fold(rows):
    paragraphs, current = [], []
    for row in rows:
        if row:
            current.append(row.strip())
        else:
            paragraphs.append(" ".join(current))
            current = []
    paragraphs.append(" ".join(current))
    return "\n".join(paragraphs)


def _mapping(block, parent):
    result, indent = {}, None
    for line in block:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "-" or stripped.startswith("- "):
            raise FrontmatterError(f"'{parent}': write lists inline, like [a, b], not as '- item' lines")
        level = len(line) - len(line.lstrip(" "))
        if indent is None:
            indent = level
        if level != indent:
            raise FrontmatterError(f"'{parent}': only one level of nesting is supported")
        match = _KEY.match(stripped)
        if not match:
            raise FrontmatterError(f"'{parent}': expected 'key: value', got '{stripped}'")
        key, rest = match.group(1), (match.group(2) or "").strip()
        if key in result:
            raise FrontmatterError(f"'{parent}': duplicate key '{key}'")
        if not rest or rest.startswith("#") or rest.split(" #", 1)[0].strip() in BLOCK_INDICATORS:
            raise FrontmatterError(f"'{parent}.{key}': nested values must fit on one line")
        result[key] = _value(rest, f"'{parent}.{key}'")
    return result


def _value(raw, where):
    if not raw:
        return None
    if raw[0] in "\"'":
        end = _quote_end(raw, where)
        tail = raw[end + 1:].strip()
        if tail and not tail.startswith("#"):
            raise FrontmatterError(f"{where}: unexpected text after the closing quote")
        quoted = raw[:end + 1]
        if raw[0] == "'":
            return quoted[1:-1].replace("''", "'")
        try:
            return json.loads(quoted)
        except json.JSONDecodeError as exc:
            raise FrontmatterError(f"{where}: bad double-quoted string ({exc.msg})") from None
    raw = _strip_comment(raw)
    if raw.startswith("["):
        if not raw.endswith("]"):
            raise FrontmatterError(f"{where}: an inline list must end with ']'")
        if raw.startswith("[{"):
            try:
                return json.loads(raw)
            except json.JSONDecodeError as exc:
                raise FrontmatterError(f"{where}: bad inline list of mappings ({exc.msg})") from None
        inner = raw[1:-1].strip()
        return [_value(item.strip(), where) for item in inner.split(",")] if inner else []
    return _plain(raw, where)


def _quote_end(raw, where):
    quote, i = raw[0], 1
    while i < len(raw):
        char = raw[i]
        if quote == '"' and char == "\\":
            i += 2
            continue
        if char == quote:
            if quote == "'" and raw[i + 1:i + 2] == "'":
                i += 2
                continue
            return i
        i += 1
    raise FrontmatterError(f"{where}: missing closing quote")


def _strip_comment(raw):
    match = re.search(r"\s#", raw)
    return raw[:match.start()].rstrip() if match else raw


def _plain(raw, where):
    if raw.startswith(_FORBIDDEN_START) or raw.startswith(("- ", "? ")) or raw in ("-", "?"):
        raise FrontmatterError(f"{where}: quote values that start with '{raw[0]}'")
    if ": " in raw or raw.endswith(":"):
        raise FrontmatterError(f"{where}: quote values that contain ': '")
    if raw in ("true", "True", "TRUE"):
        return True
    if raw in ("false", "False", "FALSE"):
        return False
    if raw in ("null", "Null", "NULL", "~"):
        return None
    if _INT.match(raw):
        return int(raw)
    if _FLOAT.match(raw):
        return float(raw)
    if _DATE.match(raw):
        try:
            return datetime.date.fromisoformat(raw)
        except ValueError:
            return raw
    return raw


def _scalar(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, list) and any(isinstance(item, dict) for item in value):
        return json.dumps(value, ensure_ascii=False)  # JSON is valid YAML flow style
    if isinstance(value, list):
        return "[" + ", ".join(_scalar(item) for item in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)
