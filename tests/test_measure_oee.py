import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "measure-oee" / "scripts"))

import oee  # noqa: E402

SHIFT = {
    "all_time": 1440,
    "planned_production_time": 450,
    "stops": [
        {"reason": "changeover", "loss": "setup", "minutes": 30},
        {"reason": "breakdown", "loss": "breakdown", "minutes": 20},
    ],
    "minor_stop_minutes": 25,
    "products": [{"name": "X", "ideal_cycle_s": 60, "total": 340, "scrap": 10}],
}


class ComputeTest(unittest.TestCase):
    def test_skill_worked_example(self):
        r = oee.compute(SHIFT)
        self.assertAlmostEqual(r["run_time"], 400)
        self.assertAlmostEqual(r["net_run_time"], 340)
        self.assertAlmostEqual(r["fully_productive_time"], 330)
        self.assertAlmostEqual(r["availability"], 400 / 450)
        self.assertAlmostEqual(r["performance"], 0.85)
        self.assertAlmostEqual(r["quality"], 330 / 340)
        self.assertAlmostEqual(r["oee"], 330 / 450)
        self.assertAlmostEqual(r["availability"] * r["performance"] * r["quality"], r["oee"])
        self.assertAlmostEqual(r["teep"], 330 / 1440)
        self.assertAlmostEqual(r["utilisation"], 450 / 1440)

    def test_losses_add_up_to_gap(self):
        r = oee.compute(SHIFT)
        self.assertAlmostEqual(sum(item["minutes"] for item in r["losses"]), 450 - 330)
        speed = [i for i in r["losses"] if i["loss"] == "reduced speed"][0]
        self.assertAlmostEqual(speed["minutes"], 35)
        self.assertEqual(r["losses"][0]["minutes"], 35)

    def test_mixed_products_and_rework(self):
        data = {
            "planned_production_time": 900,
            "stops": [{"reason": "c", "loss": "setup", "minutes": 120}],
            "products": [
                {"name": "A", "ideal_cycle_s": 30, "total": 600, "scrap": 20},
                {"name": "B", "ideal_cycle_s": 20, "total": 1200, "scrap": 30, "rework": 30},
            ],
        }
        r = oee.compute(data)
        self.assertAlmostEqual(r["net_run_time"], 700)
        self.assertAlmostEqual(r["fully_productive_time"], 670)
        self.assertAlmostEqual(r["oee"], 670 / 900)

    def test_performance_over_100_warns(self):
        data = dict(SHIFT, products=[{"name": "X", "ideal_cycle_s": 80, "total": 340}])
        self.assertIn("performance above 100%", oee.compute(data)["warnings"][0])

    def test_rejects_impossible_input(self):
        with self.assertRaises(ValueError):
            oee.compute(dict(SHIFT, stops=[{"reason": "x", "loss": "x", "minutes": 450}]))
        with self.assertRaises(ValueError):
            oee.compute(dict(SHIFT, products=[{"name": "X", "ideal_cycle_s": 60, "total": 5, "scrap": 6}]))
        with self.assertRaises(ValueError):
            oee.compute(dict(SHIFT, planned_production_time=0))
        with self.assertRaises(ValueError):
            oee.compute(dict(SHIFT, minor_stop_minutes=-5))


class AggregateTest(unittest.TestCase):
    def test_weights_by_time_not_mean_of_percentages(self):
        def machine(ppt, fpt_parts):
            return {"planned_production_time": ppt, "stops": [],
                    "products": [{"name": "P", "ideal_cycle_s": 60, "total": fpt_parts}]}
        total = oee.aggregate([machine(420, 378), machine(60, 18)])
        self.assertAlmostEqual(total["oee"], 396 / 480)
        mean = sum(m["oee"] for m in total["machines"]) / 2
        self.assertAlmostEqual(mean, 0.60)
        self.assertNotAlmostEqual(total["oee"], mean)


if __name__ == "__main__":
    unittest.main()
