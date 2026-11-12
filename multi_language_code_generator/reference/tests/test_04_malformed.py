
import unittest
from log_analyzer import LogAnalyzer


class TestMalformedLogs(unittest.TestCase):

    def test_malformed_entries(self):
        analyzer = LogAnalyzer()

        logs = [
            '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512',
            'INVALID LOG ENTRY',
            'ANOTHER INVALID ENTRY'
        ]

        result = analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["invalid_entries"], 2)

    def test_empty_string(self):
        analyzer = LogAnalyzer()
        result = analyzer.analyze([""])

        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["invalid_entries"], 1)


if __name__ == "__main__":
    unittest.main()
