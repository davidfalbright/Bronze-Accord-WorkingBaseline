import unittest
from interlace_engine import InterlaceEngine

class TestInterlaceEngine(unittest.TestCase):
    def test_reconcile(self):
        engine = InterlaceEngine()
        result = engine.reconcile_bundles(
            {"belief": "All sentient beings deserve dignity."},
            {"belief": "Animals should be treated with compassion."}
        )
        self.assertIn("conflicts", result)
        self.assertIn("matches", result)
        self.assertIn("similarity_score", result)

if __name__ == "__main__":
    unittest.main()
