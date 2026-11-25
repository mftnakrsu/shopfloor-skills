import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "measure-spc" / "scripts"))

import spc_limits as spc  # noqa: E402


class XbarRTest(unittest.TestCase):
    def test_skill_worked_example(self):
        r = spc.compute({"chart": "xbar_r", "n": 4, "means": [50.0] * 5, "ranges": [2.0] * 5})
        self.assertAlmostEqual(r["ucl"], 51.458)
        self.assertAlmostEqual(r["lcl"], 48.542)
        self.assertAlmostEqual(r["r_ucl"], 4.564)
        self.assertAlmostEqual(r["r_lcl"], 0.0)
        self.assertAlmostEqual(r["sigma_of_mean"], 0.486)

    def test_reference_example_n3(self):
        r = spc.compute({"chart": "xbar_r", "n": 3, "means": [8.0] * 4, "ranges": [0.3] * 4})
        self.assertAlmostEqual(r["ucl"], 8.3069)
        self.assertAlmostEqual(r["r_ucl"], 0.7725)
        self.assertAlmostEqual(r["process_sigma"], 0.3 / 1.693)

    def test_raw_subgroups(self):
        r = spc.compute({"chart": "xbar_r", "subgroups": [[1, 2, 3], [2, 3, 4]]})
        self.assertEqual(r["n"], 3)
        self.assertAlmostEqual(r["centre"], 2.5)
        self.assertAlmostEqual(r["r_bar"], 2.0)

    def test_rejects_mixed_sizes_and_large_n(self):
        with self.assertRaises(ValueError):
            spc.compute({"chart": "xbar_r", "subgroups": [[1, 2], [1, 2, 3]]})
        with self.assertRaises(ValueError):
            spc.compute({"chart": "xbar_r", "n": 12, "means": [1], "ranges": [1]})

    def test_baseline_freezes_limits(self):
        r = spc.compute({"chart": "xbar_r", "n": 4, "means": [52.0, 50.0], "ranges": [1.0, 1.0],
                         "baseline": {"centre": 50.0, "spread": 2.0}})
        self.assertAlmostEqual(r["ucl"], 51.458)
        self.assertEqual(r["signals"][0], {"rule": 1, "side": "high", "at": 1})


class IMRTest(unittest.TestCase):
    def test_reference_example(self):
        r = spc.compute({"chart": "imr", "values": [10, 12, 11, 13, 14]})
        self.assertAlmostEqual(r["centre"], 12.0)
        self.assertAlmostEqual(r["mr_bar"], 1.5)
        self.assertAlmostEqual(r["ucl"], 12.0 + 3 * 1.5 / 1.128)
        self.assertAlmostEqual(r["mr_ucl"], 4.9005)
        self.assertEqual(r["signals"], [])

    def test_skill_example_limits(self):
        r = spc.compute({"chart": "imr", "values": [20.0, 20.5], "baseline": {"centre": 20.0, "spread": 0.5}})
        self.assertAlmostEqual(round(r["ucl"], 2), 21.33)
        self.assertAlmostEqual(round(r["lcl"], 2), 18.67)
        self.assertAlmostEqual(r["mr_ucl"], 1.6335)


class PChartTest(unittest.TestCase):
    def test_per_subgroup_limits(self):
        r = spc.compute({"chart": "p", "defectives": [8, 2, 110], "inspected": [200, 50, 2750]})
        self.assertAlmostEqual(r["p_bar"], 0.04)
        self.assertAlmostEqual(round(r["subgroups"][0]["ucl"], 4), 0.0816)
        self.assertAlmostEqual(round(r["subgroups"][1]["ucl"], 3), 0.123)
        self.assertIsNone(r["subgroups"][0]["lcl"])

    def test_rejects_missing_sample_size(self):
        with self.assertRaises(ValueError):
            spc.compute({"chart": "p", "defectives": [1, 2], "inspected": [100]})
        with self.assertRaises(ValueError):
            spc.compute({"chart": "p", "defectives": [1], "inspected": [0]})


class RunRulesTest(unittest.TestCase):
    def test_reference_worked_example(self):
        signals = spc.run_rules([30.1, 30.3, 30.5, 30.2, 30.5, 30.3], 30.0, 0.2)
        self.assertEqual(signals, [{"rule": 2, "side": "high", "at": 5},
                                   {"rule": 3, "side": "high", "at": 6}])

    def test_eight_on_one_side_reported_once(self):
        signals = spc.run_rules([-0.5] + [0.5] * 10, 0.0, 1.0)
        self.assertEqual(signals, [{"rule": 4, "side": "high", "at": 9}])

    def test_low_side_rule1(self):
        self.assertEqual(spc.run_rules([0, -3.5, 0], 0.0, 1.0), [{"rule": 1, "side": "low", "at": 2}])

    def test_each_point_beyond_limit_is_own_signal(self):
        signals = spc.run_rules([0, 3.4, 3.6, 0], 0.0, 1.0)
        rule1 = [s for s in signals if s["rule"] == 1]
        self.assertEqual(rule1, [{"rule": 1, "side": "high", "at": 2},
                                 {"rule": 1, "side": "high", "at": 3}])


class ExtraBranchTest(unittest.TestCase):
    def test_p_chart_run_of_eight(self):
        defectives = [3] + [6] * 9 + [1] * 6
        r = spc.compute({"chart": "p", "defectives": defectives, "inspected": [150] * 16})
        runs = [s for s in r["signals"] if s["rule"] == 4]
        self.assertEqual(runs, [{"rule": 4, "side": "high", "at": 9}])

    def test_imr_moving_range_beyond(self):
        r = spc.compute({"chart": "imr", "values": [7.0, 7.1, 6.9, 7.0],
                         "baseline": {"centre": 7.0, "spread": 0.1}})
        self.assertEqual(r["mr_beyond_at_value"], [])
        r = spc.compute({"chart": "imr", "values": [7.0, 7.1, 7.6, 7.0],
                         "baseline": {"centre": 7.0, "spread": 0.1}})
        self.assertEqual(r["mr_beyond_at_value"], [3, 4])


if __name__ == "__main__":
    unittest.main()
