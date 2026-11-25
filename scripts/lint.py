#!/usr/bin/env python3
import argparse
import math
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))

import conventions  # noqa: E402
import frontmatter_lite as fm  # noqa: E402

SKILL_KEYS = {"name", "description", "license", "metadata"}
METADATA_KEYS = {"version", "category", "standards"}
AGENT_KEYS = {
    "name", "description", "model", "effort", "maxTurns", "tools", "disallowedTools",
    "skills", "memory", "background", "isolation", "color",
}
SECTIONS = ["Conventions", "Inputs", "Procedure", "Validation", "Output", "Pitfalls", "Hand-offs"]
SKILL_CASES = ("normal", "missing-data", "trap")
AGENT_CASES = ("scenario",)
PUBLIC_TERMS = ("examplecorp", "xps", "examplecorp production system")
PUBLIC_DIRS = ("skills", "agents", "evals", ".claude-plugin")
PUBLIC_FILES = ("README.md", "CHANGELOG.md", "CONTRIBUTING.md")
SKIP_DIRS = {".git", "private", "__pycache__", ".agents", ".opencode", ".qwen", ".cursor"}
ABOUT_START = "<!-- about-author:start -->"
ABOUT_END = "<!-- about-author:end -->"
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)[^)]*\)")
LIST_ITEM = re.compile(r"^([0-9]+\.|[-*]) ")
MAX_LINES = 500
MAX_TOKENS = 5000
MAX_DESCRIPTION = 1024
MAX_PITFALLS = 7
MAX_PRELOADS = 3
TOC_LINES = 100


def rel(root, path):
    return Path(path).relative_to(root).as_posix()


def prose_lines(text):
    fenced = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            yield number, line


def section(body, title):
    inside, lines = False, []
    for _, line in prose_lines(body):
        if line.startswith("## "):
            inside = line[3:].strip() == title
        elif inside:
            lines.append(line)
    return lines


def links(text):
    for _, line in prose_lines(text):
        yield from LINK.findall(line)


def local_target(target):
    if target.startswith("#") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
        return None
    return unquote(target.split("#", 1)[0]) or None


def name_problems(name, expected):
    if not isinstance(name, str):
        return ["name must be a string"]
    problems = []
    if name != expected:
        problems.append(f"name '{name}' must match '{expected}'")
    if len(name) > 64 or not NAME.match(name):
        problems.append(f"name '{name}' must be 1-64 characters of a-z, 0-9 and single hyphens")
    if "claude" in name or "anthropic" in name:
        problems.append(f"name '{name}' must not contain 'claude' or 'anthropic'")
    return problems


def description_problems(description):
    if not isinstance(description, str) or not description.strip():
        return ["description must be a non-empty string"]
    problems = []
    if len(description) > MAX_DESCRIPTION:
        problems.append(f"description has {len(description)} characters (max {MAX_DESCRIPTION})")
    if "Use when" not in description:
        problems.append("description must contain 'Use when'")
    return problems


def metadata_problems(metadata, stage):
    if not isinstance(metadata, dict):
        return ["metadata must be a mapping"]
    problems = []
    for key in sorted(set(metadata) - METADATA_KEYS):
        problems.append(f"metadata key '{key}' is not allowed (use only: category, standards, version)")
    for key in sorted(METADATA_KEYS - set(metadata)):
        problems.append(f"metadata key '{key}' is missing")
    for key, value in metadata.items():
        if not isinstance(value, str):
            problems.append(f"metadata '{key}' must be a quoted string")
    version = metadata.get("version")
    if isinstance(version, str) and not SEMVER.match(version):
        problems.append(f"metadata version '{version}' must look like 1.0.0")
    category = metadata.get("category")
    if isinstance(category, str) and category != stage:
        problems.append(f"metadata category '{category}' must equal the name prefix '{stage}'")
    return problems


def skill_meta_problems(meta, folder):
    stage = folder.split("-")[0]
    problems = []
    for key in sorted(set(meta) - SKILL_KEYS):
        problems.append(f"frontmatter key '{key}' is not allowed (use only: description, license, metadata, name)")
    for key in sorted(SKILL_KEYS - set(meta)):
        problems.append(f"frontmatter key '{key}' is missing")
    if "name" in meta:
        problems += name_problems(meta["name"], folder)
        if stage not in conventions.STAGES:
            problems.append("name must start with a stage prefix: " + ", ".join(s + "-" for s in conventions.STAGES))
    if "description" in meta:
        problems += description_problems(meta["description"])
    if "license" in meta and meta["license"] != "MIT":
        problems.append("license must be MIT")
    if "metadata" in meta:
        problems += metadata_problems(meta["metadata"], stage)
    return problems


def size_problems(text):
    problems = []
    lines, tokens = len(text.splitlines()), math.ceil(len(text) / 4)
    if lines > MAX_LINES:
        problems.append(f"SKILL.md has {lines} lines (max {MAX_LINES})")
    if tokens > MAX_TOKENS:
        problems.append(f"SKILL.md is about {tokens} tokens (max {MAX_TOKENS}; characters / 4)")
    return problems


def section_problems(body):
    problems = []
    titles = [line for _, line in prose_lines(body) if line.startswith("# ")]
    if len(titles) != 1:
        problems.append(f"body needs exactly one '# ' title (found {len(titles)})")
    found = [line[3:].strip() for _, line in prose_lines(body) if line.startswith("## ")]
    if found != SECTIONS:
        problems.append("sections must be, in order: " + ", ".join(SECTIONS) + " (found: " + (", ".join(found) or "none") + ")")
    pitfalls = [line for line in section(body, "Pitfalls") if LIST_ITEM.match(line)]
    if len(pitfalls) > MAX_PITFALLS:
        problems.append(f"Pitfalls has {len(pitfalls)} items (max {MAX_PITFALLS})")
    return problems


def unknown_skill_refs(text, skill_names, label):
    unknown = sorted(set(conventions.SKILL_REF.findall(text)) - set(skill_names))
    return [f"{label} names unknown skill '{name}'" for name in unknown]


def link_errors(root, path, text):
    errors = []
    for target in links(text):
        local = local_target(target)
        if local and not (path.parent / local).exists():
            errors.append(f"{rel(root, path)}: broken link '{target}'")
    return errors


def reference_errors(root, skill_dir, skill_body):
    ref_dir = skill_dir / "references"
    if not ref_dir.is_dir():
        return []
    linked = {(skill_dir / local).resolve() for local in filter(None, map(local_target, links(skill_body)))}
    errors = []
    for ref in sorted(ref_dir.iterdir()):
        where = rel(root, ref)
        if ref.is_dir():
            errors.append(f"{where}: references must be files directly inside references/")
            continue
        if ref.resolve() not in linked:
            errors.append(f"{where}: not linked from SKILL.md")
        if ref.suffix != ".md":
            continue
        text = ref.read_text(encoding="utf-8")
        lines = text.splitlines()
        if len(lines) > TOC_LINES and not any(line.strip() == "## Contents" for line in lines[:30]):
            errors.append(f"{where}: has {len(lines)} lines, so it must start with a '## Contents' section")
        headings = [line[3:].strip() for _, line in prose_lines(text) if line.startswith("## ")]
        if not headings or headings[-1] != "Sources":
            errors.append(f"{where}: must end with a '## Sources' section")
        for target in links(text):
            local = local_target(target)
            if local and (ref.parent / local).resolve().parent == ref_dir.resolve():
                errors.append(f"{where}: links to another reference '{target}' (keep references one level deep)")
        errors += link_errors(root, ref, text)
    return errors


def check_skill(root, skill_dir, skill_names):
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        return [f"{rel(root, skill_dir)}: missing SKILL.md"]
    where = rel(root, path)
    text = path.read_text(encoding="utf-8")
    try:
        head, body = fm.split(text)
        meta = fm.parse(head)
    except fm.FrontmatterError as exc:
        return [f"{where}: frontmatter: {exc}"]
    problems = skill_meta_problems(meta, skill_dir.name)
    problems += size_problems(text)
    problems += section_problems(body)
    problems += unknown_skill_refs("\n".join(section(body, "Hand-offs")), skill_names, "Hand-offs")
    return [f"{where}: {p}" for p in problems] + link_errors(root, path, body) + reference_errors(root, skill_dir, body)


def check_agent(root, path, skill_names):
    where = rel(root, path)
    try:
        meta, body = fm.read(path)
    except fm.FrontmatterError as exc:
        return [f"{where}: frontmatter: {exc}"]
    problems = []
    for key in sorted(set(meta) - AGENT_KEYS):
        problems.append(f"frontmatter key '{key}' is not supported for plugin agents")
    for key in ("name", "description"):
        if key not in meta:
            problems.append(f"frontmatter key '{key}' is missing")
    if "name" in meta:
        problems += name_problems(meta["name"], path.stem)
    if "description" in meta:
        problems += description_problems(meta["description"])
    if "tools" in meta and conventions.as_list(meta["tools"]) != conventions.READ_ONLY_TOOLS:
        problems.append("tools must be omitted or exactly: " + ", ".join(conventions.READ_ONLY_TOOLS))
    preloads = [conventions.strip_plugin_prefix(s) for s in conventions.as_list(meta.get("skills"))]
    if len(preloads) > MAX_PRELOADS:
        problems.append(f"preloads {len(preloads)} skills (max {MAX_PRELOADS})")
    problems += [f"skills: unknown skill '{s}'" for s in preloads if s not in skill_names]
    problems += unknown_skill_refs(body, skill_names, "body")
    return [f"{where}: {p}" for p in problems] + link_errors(root, path, body)


def check_evals(root, skill_names, agent_names):
    eval_dir = root / "evals"
    errors, cases = [], {}
    for case in sorted(eval_dir.iterdir()) if eval_dir.is_dir() else []:
        if not case.is_dir() or case.name == "results" or case.name.startswith("."):
            continue
        owner, sep, kind = case.name.rpartition("--")
        if not sep:
            errors.append(f"{rel(root, case)}: case folders are named '<skill-or-agent>--<kind>'")
            continue
        cases.setdefault(owner, set()).add(kind)
        if not (case / "prompt.md").is_file():
            errors.append(f"{rel(root, case)}: missing prompt.md")
        if not list((case / "graders").glob("*.md")):
            errors.append(f"{rel(root, case)}: needs at least one graders/*.md file")
    for names, kinds, label in ((skill_names, SKILL_CASES, "skill"), (agent_names, AGENT_CASES, "agent")):
        for name in sorted(names):
            found = cases.get(name, set())
            if found != set(kinds):
                expected = ", ".join(f"{name}--{kind}" for kind in kinds)
                errors.append(f"evals: {label} '{name}' needs exactly {expected} (found: {', '.join(sorted(found)) or 'none'})")
    for owner in sorted(set(cases) - set(skill_names) - set(agent_names)):
        errors.append(f"evals: cases for unknown skill or agent '{owner}'")
    return errors


def check_docs(root):
    readme = root / "README.md"
    if not readme.is_file():
        return ["README.md: missing"]
    text = readme.read_text(encoding="utf-8")
    errors = []
    if text.count(ABOUT_START) != 1 or text.count(ABOUT_END) != 1 or text.find(ABOUT_START) > text.find(ABOUT_END):
        errors.append(f"README.md: needs exactly one {ABOUT_START} ... {ABOUT_END} block")
    for name in PUBLIC_FILES:
        path = root / name
        if path.is_file():
            errors += link_errors(root, path, path.read_text(encoding="utf-8"))
    return errors


def term_pattern(term):
    words = r"\s+".join(re.escape(word) for word in term.split())
    return re.compile(r"(?<![A-Za-z0-9])" + words + r"(?![A-Za-z0-9])", re.IGNORECASE)


def blank_about_block(text):
    start, end = text.find(ABOUT_START), text.find(ABOUT_END)
    if start == -1 or end < start:
        return text
    block = text[start:end + len(ABOUT_END)]
    return text[:start] + "\n" * block.count("\n") + text[end + len(ABOUT_END):]


def walk_files(root, top):
    base = root / top
    if base.is_file():
        yield base
        return
    if not base.is_dir():
        return
    for directory, subdirs, files in os.walk(base):
        current = Path(directory)
        subdirs[:] = sorted(d for d in subdirs if d not in SKIP_DIRS and rel(root, current / d) != "evals/results")
        for name in sorted(files):
            yield current / name


def term_errors(root, files, terms, label, allow_about_block):
    patterns = [(term, term_pattern(term)) for term in terms]
    errors = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if allow_about_block and path == root / "README.md":
            text = blank_about_block(text)
        for number, line in enumerate(text.splitlines(), 1):
            for term, pattern in patterns:
                if pattern.search(line):
                    errors.append(f"{rel(root, path)}:{number}: contains {label} term '{term}'")
    return errors


def public_files(root):
    for top in PUBLIC_DIRS + PUBLIC_FILES:
        yield from walk_files(root, top)


def read_terms(path):
    terms = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms


def lint(root, private_terms=()):
    root = Path(root).resolve()
    skills, agents = conventions.skill_dirs(root), conventions.agent_files(root)
    skill_names, agent_names = {d.name for d in skills}, {p.stem for p in agents}
    errors = []
    for skill_dir in skills:
        errors += check_skill(root, skill_dir, skill_names)
    for agent in agents:
        errors += check_agent(root, agent, skill_names)
    errors += check_evals(root, skill_names, agent_names)
    errors += check_docs(root)
    errors += term_errors(root, public_files(root), PUBLIC_TERMS, "public", True)
    if private_terms:
        errors += term_errors(root, walk_files(root, "."), private_terms, "private", False)
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Static checks for shopfloor-skills.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--private-terms", type=Path, help="term list (default: <root>/private/private-terms.txt if it exists)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    terms_file = args.private_terms or root / "private" / "private-terms.txt"
    if args.private_terms and not terms_file.is_file():
        parser.error(f"no such file: {terms_file}")
    private_terms = read_terms(terms_file) if terms_file.is_file() else []
    errors = lint(root, private_terms)
    for error in errors:
        print(error)
    counts = f"{len(conventions.skill_dirs(root))} skill(s), {len(conventions.agent_files(root))} agent(s)"
    state = "on" if private_terms else "off"
    if errors:
        print(f"lint: {len(errors)} problem(s); {counts}; private terms {state}")
        return 1
    print(f"lint: ok; {counts}; private terms {state}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
