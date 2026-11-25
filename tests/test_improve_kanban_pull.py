import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "improve-kanban-pull" / "scripts"))

import kanban_calc as calc  # noqa: E402


class FormulaTest(unittest.TestCase):
    def test_lead_time_sums_components(self):
        self.assertEqual(calc.lead_time([0.5, 0, 3, 1.5, 1]), 6)
        with self.assertRaises(ValueError):
            calc.lead_time([1, -1])
        with self.assertRaises(ValueError):
            calc.lead_time([])

    def test_cards_round_up(self):
        raw, n = calc.kanban_cards(50, 6, 40, 0.1)
        self.assertAlmostEqual(raw, 8.25)
        self.assertEqual(n, 9)

    def test_exact_value_not_bumped(self):
        # 30 x 4 x 1.0 / 12 = 10 exactly; float noise must not give 11.
        self.assertEqual(calc.kanban_cards(30, 4, 12)[1], 10)
        self.assertEqual(calc.kanban_cards(10, 3, 11, 0.1)[1], 3)

    def test_batch_adds_k_minus_one(self):
        self.assertEqual(calc.kanban_cards(50, 6, 40, 0.1, batch=3)[1], 11)
        with self.assertRaises(ValueError):
            calc.kanban_cards(50, 6, 40, batch=0)

    def test_invalid_inputs(self):
        for args in ((0, 6, 40), (50, 0, 40), (50, 6, 0)):
            with self.assertRaises(ValueError):
                calc.kanban_cards(*args)
        with self.assertRaises(ValueError):
            calc.kanban_cards(50, 6, 40, -0.1)

    def test_pitch(self):
        self.assertAlmostEqual(calc.takt(25200, 420), 60)
        self.assertAlmostEqual(calc.pitch(25200, 420, 12), 720)
        with self.assertRaises(ValueError):
            calc.pitch(25200, 420, 0)

    def test_conwip(self):
        self.assertEqual(calc.conwip_cards(25, 2), 50)
        self.assertEqual(calc.conwip_cards(7, 1.5), 11)


class CliTest(unittest.TestCase):
    def run_cli(self, argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(calc.main(argv), 0)
        return buf.getvalue()

    def test_cards_cli(self):
        out = self.run_cli(["cards", "--demand", "50", "--lead-times", "0.5,0,3,1.5,1", "--container", "40", "--safety", "0.1", "--batch", "3"])
        self.assertIn("Cards = 11", out)
        self.assertIn("maximum loop stock = 440", out)

    def test_pitch_cli(self):
        self.assertIn("Pitch = 720 s = 12.0 min", self.run_cli(["pitch", "--available", "25200", "--demand", "420", "--pack", "12"]))

    def test_bad_input_exits(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            calc.main(["cards", "--demand", "0", "--lead-times", "1", "--container", "5"])


if __name__ == "__main__":
    unittest.main()
