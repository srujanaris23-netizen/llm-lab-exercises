import unittest
import urllib.request

BASE_URL = "http://localhost:8000"

class DeliveryMetricsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with urllib.request.urlopen(
            f"{BASE_URL}/metrics", timeout=5
        ) as response:
            cls.metrics = response.read().decode("utf-8")

    def test_metrics_endpoint_responds(self):
        self.assertIn("total_deliveries", self.metrics)

    def test_pending_deliveries_metric_exists(self):
        self.assertIn("pending_deliveries", self.metrics)

    def test_on_the_way_metric_exists(self):
        self.assertIn("on_the_way_deliveries", self.metrics)

    def test_delivery_values_are_nonnegative(self):
        for metric in [
            "total_deliveries",
            "pending_deliveries",
            "on_the_way_deliveries",
        ]:
            lines = [
                line for line in self.metrics.splitlines()
                if line.startswith(metric + " ")
            ]
            self.assertTrue(lines, f"{metric} not found")
            value = float(lines[0].split()[1])
            self.assertGreaterEqual(value, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
