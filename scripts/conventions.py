import re
from pathlib import Path

STAGES = ("lead", "measure", "improve", "plan", "solve", "audit")
READ_ONLY_TOOLS = ["Read", "Grep", "Glob", "Skill"]
SKILL_REF = re.compile(r"`((?:" + "|".join(STAGES) + r")(?:-[a-z0-9]+)+)`")


def skill_dirs(repo):
    root = Path(repo) / "skills"
    if not root.is_dir():
        return []
    return sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))


def agent_files(repo):
    root = Path(repo) / "agents"
    if not root.is_dir():
        return []
    return sorted(root.glob("*.md"))


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value]
    return [part.strip() for part in str(value).split(",") if part.strip()]


def strip_plugin_prefix(name):
    return name.split(":", 1)[-1]
