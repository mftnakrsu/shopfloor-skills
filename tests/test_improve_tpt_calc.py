import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "improve-tpt" / "scripts"))

import tpt_calc as calc  # noqa: E402

TIMES = [2, 3, 1, 2]
MACHINES = [1, 2, 1, 1]


class FormulaTest(unittest.TestCase):
    def test_little(self):
        self.assertAlmostEqual(calc.little_tpt(40, 0.4), 100)
        with self.assertRaises(ValueError):
            calc.little_tpt(40, 0)

    def test_reference_points(self):
        t0 = calc.raw_process_time(TIMES)
        rb = calc.bottleneck_rate(TIMES, MACHINES)
        self.assertEqual(t0, 8)
        self.assertAlmostEqual(rb, 0.5)
        self.assertAlmostEqual(calc.critical_wip(rb, t0), 4)

    def test_parallel_machines_raise_station_rate(self):
        self.assertAlmostEqual(calc.bottleneck_rate([3], [2]), 2 / 3)
        with self.assertRaises(ValueError):
            calc.bottleneck_rate([1, 2], [1])

    def test_penny_fab_cases(self):
        # Gallego's example: four stations of 2 h, W0 = 4.
        t0, rb = 8, 0.5
        self.assertEqual(calc.best_case(2, t0, rb), (8, 0.25))
        self.assertEqual(calc.best_case(10, t0, rb), (20, 0.5))
        self.assertEqual(calc.worst_case(4, t0), (32, 0.125))
        tpt, th = calc.practical_worst_case(40, t0, rb)
        self.assertAlmostEqual(tpt, 86)
        self.assertAlmostEqual(th, 0.5 * 40 / 43)

    def test_pwc_obeys_little(self):
        tpt, th = calc.practical_worst_case(12, 8, 0.5)
        self.assertAlmostEqual(tpt * th, 12)

    def test_pwc_wip_needed_inverts_pwc(self):
        w = calc.pwc_wip_needed(0.4, 8, 0.5)
        self.assertAlmostEqual(w, 12)
        self.assertAlmostEqual(calc.practical_worst_case(w, 8, 0.5)[1], 0.4)
        with self.assertRaises(ValueError):
            calc.pwc_wip_needed(0.5, 8, 0.5)

    def test_kingman(self):
        self.assertAlmostEqual(calc.kingman_queue(0.9, 1, 1, 1), 9)
        self.assertAlmostEqual(calc.kingman_queue(0.9, 1, 0.5, 1), 5.625)
        self.assertAlmostEqual(calc.kingman_queue(0.8, 1, 0.5, 1), 2.5)
        with self.assertRaises(ValueError):
            calc.kingman_queue(1, 1, 1, 1)


class CliTest(unittest.TestCase):
    def run_cli(self, *argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(calc.main(list(argv)), 0)
        return out.getvalue()

    def test_line_report(self):
        text = self.run_cli("line", "--wip", "60", "--throughput", "1.25", "--process-times", "30,40,20,30",
                            "--unit", "min", "--hours-per-day", "16", "--caps", "12")
        self.assertIn("48.00 h = 3.00 working days", text)
        self.assertIn("W0 = 3.00", text)
        self.assertIn("worse than PWC", text)
        self.assertIn("WIP the PWC needs for 1.25 per h = 10.0", text)
        self.assertIn("Cap 12: PWC TH 1.286 per h (meets 1.25)", text)

    def test_kingman_cli(self):
        self.assertIn("Queue time = 9.00", self.run_cli("kingman", "--u", "0.9", "--ca", "1", "--ce", "1", "--te", "1"))

    def test_bad_input_exits(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            calc.main(["line", "--wip", "10", "--throughput", "0", "--process-times", "1"])


if __name__ == "__main__":
    unittest.main()
