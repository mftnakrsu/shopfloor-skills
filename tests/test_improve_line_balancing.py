import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "improve-line-balancing" / "scripts"))

import balance  # noqa: E402


def element(name, seconds, variants=None):
    item = {"name": name, "seconds": seconds}
    if variants:
        item["variants"] = variants
    return item


LINE = {
    "shift_seconds": 28800,
    "scheduled_stops_seconds": 1200,
    "shifts_per_day": 2,
    "demand_per_day": 1380,
    "planned_cycle_seconds": 38,
    "current_operators": 4,
    "elements": [element(f"e{i}", s) for i, s in enumerate([9, 12, 10, 7, 11, 15, 12, 14, 6, 8], 1)],
}


class TaktTest(unittest.TestCase):
    def test_takt_uses_scheduled_stops_only(self):
        effective = balance.effective_seconds(28800, 1200)
        self.assertEqual(effective, 27600)
        self.assertEqual(balance.takt(effective, 690), 40)

    def test_rejects_bad_inputs(self):
        with self.assertRaises(ValueError):
            balance.effective_seconds(100, 100)
        with self.assertRaises(ValueError):
            balance.takt(100, 0)


class FractionRuleTest(unittest.TestCase):
    def test_bands(self):
        self.assertEqual(balance.fraction_advice(3.2)[0], 3)
        self.assertEqual(balance.fraction_advice(3.4)[0], 4)
        self.assertEqual(balance.fraction_advice(3.5)[0], 4)
        self.assertEqual(balance.fraction_advice(3.75)[0], 4)
        self.assertEqual(balance.fraction_advice(3.0)[0], 3)
        self.assertIn("below 0.3", balance.fraction_advice(2.1)[1])
        self.assertIn("0.3 to 0.5", balance.fraction_advice(2.4)[1])


class FillUpTest(unittest.TestCase):
    def test_reference_example(self):
        out = balance.analyse(LINE)
        self.assertEqual(out["takt_seconds"], 40)
        self.assertEqual(out["weighted_content_seconds"], 104)
        loads = [op["load_by_variant"]["all"] for op in out["yamazumi"]]
        self.assertEqual(loads, [38, 38, 28])
        self.assertEqual(out["yamazumi"][-1]["gap_to_cap"], 10)
        self.assertEqual(out["operators_saved_all_shifts"], 2)
        self.assertAlmostEqual(out["units_per_labour_hour"], 30.0, places=1)
        self.assertAlmostEqual(out["productivity_gain"], 1 / 3, places=3)

    def test_mix_keeps_every_variant_under_cap(self):
        line = dict(LINE, planned_cycle_seconds=28, demand_per_day=1800, shift_seconds=28800,
                    scheduled_stops_seconds=1800, mix={"A": 0.8, "B": 0.2}, current_operators=5,
                    elements=[element("a", 18), element("b", 10), element("c", 20),
                              element("shield", 10, ["B"]), element("d", 12)])
        out = balance.analyse(line)
        self.assertEqual(out["takt_seconds"], 30)
        self.assertEqual(out["content_by_variant"], {"A": 60, "B": 70})
        self.assertEqual(out["weighted_content_seconds"], 62)
        for op in out["yamazumi"]:
            self.assertLessEqual(max(op["load_by_variant"].values()), 28)
        self.assertEqual(out["yamazumi"][2]["load_by_variant"], {"A": 12, "B": 22})

    def test_element_longer_than_cap_is_rejected(self):
        with self.assertRaises(ValueError):
            balance.fill_up([element("long", 50)], {"all": 1.0}, 40)

    def test_planned_cycle_above_takt_is_rejected(self):
        with self.assertRaises(ValueError):
            balance.analyse(dict(LINE, planned_cycle_seconds=45))

    def test_mix_must_sum_to_one(self):
        with self.assertRaises(ValueError):
            balance.analyse(dict(LINE, mix={"A": 0.5, "B": 0.4}))


class CliTest(unittest.TestCase):
    def test_main_prints_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "line.json"
            path.write_text(json.dumps(LINE), encoding="utf-8")
            import contextlib
            import io
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = balance.main([str(path)])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(buffer.getvalue())["operators_after_fill_up"], 3)


if __name__ == "__main__":
    unittest.main()
