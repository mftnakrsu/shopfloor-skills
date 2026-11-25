import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import conventions  # noqa: E402


class ConventionsTest(unittest.TestCase):
    def test_as_list_accepts_lists_strings_and_none(self):
        self.assertEqual(conventions.as_list(None), [])
        self.assertEqual(conventions.as_list([" a", "b "]), ["a", "b"])
        self.assertEqual(conventions.as_list("Read, Grep,"), ["Read", "Grep"])

    def test_skill_refs_need_backticks_and_a_stage_prefix(self):
        text = "Use `solve-8d`, `solve-*`, `first-off` and solve-5why."
        self.assertEqual(conventions.SKILL_REF.findall(text), ["solve-8d"])

    def test_skill_dirs_skip_files_and_hidden_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("solve-8d", ".hidden", "_draft"):
                (root / "skills" / name).mkdir(parents=True)
            (root / "skills" / "notes.md").write_text("x", encoding="utf-8")
            self.assertEqual([p.name for p in conventions.skill_dirs(root)], ["solve-8d"])

    def test_strip_plugin_prefix(self):
        self.assertEqual(conventions.strip_plugin_prefix("shopfloor-skills:solve-8d"), "solve-8d")
        self.assertEqual(conventions.strip_plugin_prefix("solve-8d"), "solve-8d")


if __name__ == "__main__":
    unittest.main()
