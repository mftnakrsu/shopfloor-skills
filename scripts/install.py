#!/usr/bin/env python3
import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import conventions  # noqa: E402
import frontmatter_lite as fm  # noqa: E402

TOOLS = ("opencode", "qwen", "cursor")
PROJECT_SKILLS = ".agents/skills"
PROJECT_AGENTS = {"opencode": ".opencode/agents", "qwen": ".qwen/agents", "cursor": ".cursor/agents"}
USER_SKILLS = {"opencode": ".config/opencode/skills", "qwen": ".qwen/skills", "cursor": ".cursor/skills"}
USER_AGENTS = {"opencode": ".config/opencode/agents", "qwen": ".qwen/agents", "cursor": ".cursor/agents"}
QWEN_READ_ONLY_TOOLS = ["read_file", "read_many_files", "list_directory", "glob", "search_file_content"]
SKILL_FILES_INTRO = "Before you apply a method named in this file, read its skill file:"


@dataclass
class Action:
    kind: str
    name: str
    tool: str
    target: Path
    source: Path = None
    content: str = None


def skill_names_for(meta, body, available):
    names = [conventions.strip_plugin_prefix(s) for s in conventions.as_list(meta.get("skills"))]
    names += conventions.SKILL_REF.findall(body)
    ordered = []
    for name in names:
        if name in available and name not in ordered:
            ordered.append(name)
    return ordered


def convert_agent(path, tool, skill_paths):
    meta, body = fm.read(path)
    for key in ("name", "description"):
        if key not in meta:
            raise ValueError(f"{path.name}: frontmatter key '{key}' is missing")
    read_only = "tools" in meta
    if read_only and conventions.as_list(meta["tools"]) != conventions.READ_ONLY_TOOLS:
        raise ValueError(f"{path.name}: tools must be omitted or exactly {', '.join(conventions.READ_ONLY_TOOLS)}")
    if tool == "opencode":
        head = {"description": meta["description"], "mode": "subagent"}
        if read_only:
            head["permission"] = {"edit": "deny", "bash": "deny"}
    elif tool == "qwen":
        head = {"name": meta["name"], "description": meta["description"]}
        if read_only:
            head["tools"] = QWEN_READ_ONLY_TOOLS
    else:
        head = {"name": meta["name"], "description": meta["description"], "model": "inherit"}
        if read_only:
            head["readonly"] = True
    text = "---\n" + fm.dump(head) + "---\n" + body.strip() + "\n"
    names = skill_names_for(meta, body, skill_paths)
    if names:
        text += f"\n## Skill files\n\n{SKILL_FILES_INTRO}\n\n"
        text += "".join(f"- `{name}`: `{skill_paths[name]}`\n" for name in names)
    return text


def plan_actions(repo, tools, scope, dest, home):
    skills, agents = conventions.skill_dirs(repo), conventions.agent_files(repo)
    actions = []
    if scope == "project":
        skills_root = dest / PROJECT_SKILLS
        actions += [Action("skill", s.name, "shared", skills_root / s.name, source=s) for s in skills]
        paths = {s.name: f"{PROJECT_SKILLS}/{s.name}/SKILL.md" for s in skills}
        for tool in tools:
            target = dest / PROJECT_AGENTS[tool]
            actions += [Action("agent", a.stem, tool, target / a.name, content=convert_agent(a, tool, paths)) for a in agents]
        return actions
    for tool in tools:
        skills_root = home / USER_SKILLS[tool]
        actions += [Action("skill", s.name, tool, skills_root / s.name, source=s) for s in skills]
        paths = {s.name: (skills_root / s.name / "SKILL.md").as_posix() for s in skills}
        target = home / USER_AGENTS[tool]
        actions += [Action("agent", a.stem, tool, target / a.name, content=convert_agent(a, tool, paths)) for a in agents]
    return actions


def write(actions):
    for action in actions:
        if action.kind == "skill":
            if action.target.exists():
                shutil.rmtree(action.target)
            shutil.copytree(action.source, action.target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        else:
            action.target.parent.mkdir(parents=True, exist_ok=True)
            action.target.write_text(action.content, encoding="utf-8", newline="\n")


def main(argv=None, repo=None, home=None):
    parser = argparse.ArgumentParser(description="Install shopfloor-skills skills and agents into OpenCode, Qwen Code or Cursor.")
    parser.add_argument("--tool", required=True, choices=TOOLS + ("all",))
    parser.add_argument("--scope", choices=("project", "user"), default="project")
    parser.add_argument("--dest", type=Path, default=Path.cwd(), help="project root for --scope project (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="print the planned writes and change nothing")
    parser.add_argument("--force", action="store_true", help="overwrite skills and agents that already exist")
    args = parser.parse_args(argv)
    repo = Path(repo) if repo else Path(__file__).resolve().parents[1]
    home = Path(home) if home else Path.home()
    tools = list(TOOLS) if args.tool == "all" else [args.tool]
    try:
        actions = plan_actions(repo, tools, args.scope, args.dest.resolve(), home)
    except (ValueError, fm.FrontmatterError) as exc:
        print(f"install: {exc}")
        return 2
    existing = [] if args.force else [a for a in actions if a.target.exists()]
    for action in actions:
        note = "  (exists)" if action in existing else ""
        print(f"{action.kind} {action.name} [{action.tool}] -> {action.target}{note}")
    if existing:
        print(f"install: {len(existing)} target(s) already exist, nothing was written; use --force to overwrite")
        return 1
    if args.dry_run:
        print(f"install: dry run, {len(actions)} write(s) planned, nothing was written")
        return 0
    write(actions)
    skills = sum(a.kind == "skill" for a in actions)
    print(f"install: wrote {skills} skill folder(s) and {len(actions) - skills} agent file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
