import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import frontmatter_lite as fm  # noqa: E402
import install  # noqa: E402

SKILL = "---\nname: {name}\ndescription: Test. Use when testing.\n---\n# {name}\n"
WRITER = """---
name: 8d-moderator
description: >-
  Moderates an 8D. Use when testing.
model: inherit
skills: [solve-8d]
---
## Role
Takes escalations from `lead-daily-routine` and never uses `solve-unknown`.
"""
REVIEWER = """---
name: skill-reviewer
description: Reviews skills. Use when testing.
model: inherit
tools: Read, Grep, Glob, Skill
---
## Role
Reads only.
"""


class InstallTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        self.repo, self.dest, self.home = base / "repo", base / "project", base / "home"
        for name in ("solve-8d", "lead-daily-routine"):
            self.write(self.repo / "skills" / name / "SKILL.md", SKILL.format(name=name))
        self.write(self.repo / "skills" / "solve-8d" / "references" / "gates.md", "# Gates\n")
        self.write(self.repo / "agents" / "8d-moderator.md", WRITER)
        self.write(self.repo / "agents" / "skill-reviewer.md", REVIEWER)

    def tearDown(self):
        self._tmp.cleanup()

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_install(self, *args):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = install.main(list(args), repo=self.repo, home=self.home)
        return code, out.getvalue()

    @staticmethod
    def agent(folder, name):
        return fm.read(folder / f"{name}.md")


class ProjectScopeTest(InstallTestCase):
    def test_copies_skills_once_and_agents_per_tool(self):
        code, _ = self.run_install("--tool", "all", "--dest", str(self.dest))
        self.assertEqual(code, 0)
        self.assertTrue((self.dest / ".agents/skills/solve-8d/references/gates.md").is_file())
        self.assertTrue((self.dest / ".agents/skills/lead-daily-routine/SKILL.md").is_file())
        for folder in install.PROJECT_AGENTS.values():
            for name in ("8d-moderator", "skill-reviewer"):
                self.assertTrue((self.dest / folder / f"{name}.md").is_file(), (folder, name))

    def test_opencode_format(self):
        self.run_install("--tool", "opencode", "--dest", str(self.dest))
        meta, body = self.agent(self.dest / ".opencode/agents", "8d-moderator")
        self.assertEqual(meta, {"description": "Moderates an 8D. Use when testing.", "mode": "subagent"})
        self.assertIn("- `solve-8d`: `.agents/skills/solve-8d/SKILL.md`", body)
        self.assertIn("- `lead-daily-routine`: `.agents/skills/lead-daily-routine/SKILL.md`", body)
        self.assertNotIn("`solve-unknown`:", body)
        text = (self.dest / ".opencode/agents/skill-reviewer.md").read_text(encoding="utf-8")
        head = text.split("---\n")[1]
        rules = [line for line in head.splitlines() if line.startswith("permissions: ")]
        self.assertEqual(len(rules), 1)
        self.assertEqual(
            json.loads(rules[0][len("permissions: "):]),
            [{"action": "edit", "resource": "*", "effect": "deny"}, {"action": "shell", "resource": "*", "effect": "deny"}],
        )
        self.assertNotIn("\npermission:", head)

    def test_qwen_format(self):
        self.run_install("--tool", "qwen", "--dest", str(self.dest))
        meta, body = self.agent(self.dest / ".qwen/agents", "8d-moderator")
        self.assertEqual(meta, {"name": "8d-moderator", "description": "Moderates an 8D. Use when testing."})
        self.assertIn("## Skill files", body)
        meta, body = self.agent(self.dest / ".qwen/agents", "skill-reviewer")
        self.assertEqual(meta["tools"], install.QWEN_READ_ONLY_TOOLS)
        self.assertNotIn("## Skill files", body)

    def test_cursor_format(self):
        self.run_install("--tool", "cursor", "--dest", str(self.dest))
        meta, _ = self.agent(self.dest / ".cursor/agents", "8d-moderator")
        self.assertEqual(meta, {"name": "8d-moderator", "description": "Moderates an 8D. Use when testing.", "model": "inherit"})
        meta, _ = self.agent(self.dest / ".cursor/agents", "skill-reviewer")
        self.assertIs(meta["readonly"], True)


class UserScopeTest(InstallTestCase):
    def test_writes_into_each_tool_home_with_absolute_paths(self):
        code, _ = self.run_install("--tool", "all", "--scope", "user")
        self.assertEqual(code, 0)
        for tool in install.TOOLS:
            skill = self.home / install.USER_SKILLS[tool] / "solve-8d" / "SKILL.md"
            self.assertTrue(skill.is_file(), tool)
            _, body = self.agent(self.home / install.USER_AGENTS[tool], "8d-moderator")
            self.assertIn(f"`{skill.as_posix()}`", body)


class SafetyTest(InstallTestCase):
    def test_existing_target_blocks_every_write_without_force(self):
        stale = self.dest / ".agents/skills/solve-8d/old.md"
        self.write(stale, "old")
        code, out = self.run_install("--tool", "opencode", "--dest", str(self.dest))
        self.assertEqual(code, 1)
        self.assertIn("(exists)", out)
        self.assertTrue(stale.is_file())
        self.assertFalse((self.dest / ".agents/skills/lead-daily-routine").exists())
        self.assertFalse((self.dest / ".opencode").exists())

    def test_force_replaces_an_existing_skill_folder(self):
        stale = self.dest / ".agents/skills/solve-8d/old.md"
        self.write(stale, "old")
        code, _ = self.run_install("--tool", "opencode", "--dest", str(self.dest), "--force")
        self.assertEqual(code, 0)
        self.assertFalse(stale.exists())
        self.assertTrue((self.dest / ".agents/skills/solve-8d/SKILL.md").is_file())

    def test_dry_run_writes_nothing(self):
        code, out = self.run_install("--tool", "all", "--dest", str(self.dest), "--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("dry run", out)
        self.assertFalse(self.dest.exists())

    def test_rejects_an_unsupported_tools_list(self):
        self.write(self.repo / "agents" / "skill-reviewer.md", REVIEWER.replace("Read, Grep, Glob, Skill", "Read, Write"))
        code, out = self.run_install("--tool", "cursor", "--dest", str(self.dest))
        self.assertEqual(code, 2)
        self.assertIn("tools must be omitted", out)


if __name__ == "__main__":
    unittest.main()
