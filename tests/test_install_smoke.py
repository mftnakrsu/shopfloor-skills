import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

import conventions  # noqa: E402
import frontmatter_lite as fm  # noqa: E402
import install  # noqa: E402


class InstallSmokeTest(unittest.TestCase):
    def test_installs_this_repo_in_project_and_user_scope(self):
        skills = [d.name for d in conventions.skill_dirs(REPO)]
        agents = [p.stem for p in conventions.agent_files(REPO)]
        with tempfile.TemporaryDirectory() as tmp:
            dest, home = Path(tmp) / "project", Path(tmp) / "home"
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(install.main(["--tool", "all", "--dest", str(dest)], home=home), 0)
                self.assertEqual(install.main(["--tool", "all", "--scope", "user"], home=home), 0)
            for tool in install.TOOLS:
                for name in skills:
                    self.assertTrue((dest / install.PROJECT_SKILLS / name / "SKILL.md").is_file(), name)
                    self.assertTrue((home / install.USER_SKILLS[tool] / name / "SKILL.md").is_file(), (tool, name))
                for name in agents:
                    for folder in (dest / install.PROJECT_AGENTS[tool], home / install.USER_AGENTS[tool]):
                        meta, _ = fm.read(folder / f"{name}.md")
                        self.assertTrue(meta.get("description"), (tool, name))
                        self.assertNotIn("skills", meta)


if __name__ == "__main__":
    unittest.main()
