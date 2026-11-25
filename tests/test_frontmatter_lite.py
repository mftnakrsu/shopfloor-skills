import datetime
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import frontmatter_lite as fm  # noqa: E402


class SplitTest(unittest.TestCase):
    def test_splits_frontmatter_and_body(self):
        self.assertEqual(fm.split("---\nname: x\n---\n# Title\n"), ("name: x\n", "# Title\n"))

    def test_requires_opening_line(self):
        with self.assertRaisesRegex(fm.FrontmatterError, "must start"):
            fm.split("name: x\n---\n")

    def test_requires_closing_line(self):
        with self.assertRaisesRegex(fm.FrontmatterError, "no closing"):
            fm.split("---\nname: x\n")


class ParseTest(unittest.TestCase):
    def test_skill_frontmatter(self):
        data = fm.parse(
            "name: solve-8d\n"
            "description: >-\n"
            "  Leads an 8D.\n"
            "  Use when a complaint arrives.\n"
            "license: MIT\n"
            "metadata:\n"
            '  version: "1.0.0"\n'
            "  category: solve\n"
            '  standards: ""\n'
        )
        self.assertEqual(data["name"], "solve-8d")
        self.assertEqual(data["description"], "Leads an 8D. Use when a complaint arrives.")
        self.assertEqual(data["license"], "MIT")
        self.assertEqual(data["metadata"], {"version": "1.0.0", "category": "solve", "standards": ""})

    def test_plain_values_get_yaml_types(self):
        data = fm.parse("a: 1.0\nb: 3\nc: true\nd: 2026-01-31\ne: ~\nf: text # note\n")
        self.assertEqual(data, {"a": 1.0, "b": 3, "c": True, "d": datetime.date(2026, 1, 31), "e": None, "f": "text"})

    def test_inline_lists_and_quotes(self):
        data = fm.parse('skills: [solve-8d, "lead-daily-routine"]\nq: \'it\'\'s\'\nempty: []\n')
        self.assertEqual(data, {"skills": ["solve-8d", "lead-daily-routine"], "q": "it's", "empty": []})

    def test_block_scalars_keep_or_strip_the_final_newline(self):
        data = fm.parse("a: >\n  one\n  two\nb: |-\n  x\n  y\n")
        self.assertEqual(data, {"a": "one two\n", "b": "x\ny"})

    def test_rejects_syntax_outside_the_subset(self):
        cases = [
            ("a:\tb\n", "tabs"),
            ("skills:\n  - solve-8d\n", "inline"),
            ("description: Runs X: Y\n", "': '"),
            ("a: 1\na: 2\n", "duplicate"),
            ("m:\n  a: 1\n    b: 2\n", "one level"),
            ('a: "open\n', "closing quote"),
            ("a: *ref\n", "start with"),
        ]
        for text, message in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(fm.FrontmatterError, re.escape(message)):
                    fm.parse(text)


class DumpTest(unittest.TestCase):
    def test_dump_round_trips_through_parse(self):
        data = {
            "name": "x",
            "description": "Says: hi. Use when Prüfanweisung",
            "readonly": True,
            "tools": ["read_file", "glob"],
            "permission": {"edit": "deny", "bash": "deny"},
        }
        self.assertEqual(fm.parse(fm.dump(data)), data)


if __name__ == "__main__":
    unittest.main()
