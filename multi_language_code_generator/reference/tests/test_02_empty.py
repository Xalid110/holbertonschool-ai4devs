
import unittest
from log_analyzer import LogAnalyzer


class TestEmptyLogs(unittest.TestCase):

    def test_empty_logs(self):
        analyzer = LogAnalyzer()
        result = analyzer.analyze([])

        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["invalid_entries"], 0)
        self.assertIsNone(result["most_requested_endpoint"])


if __name__ == "__main__":
    unittest.main()
