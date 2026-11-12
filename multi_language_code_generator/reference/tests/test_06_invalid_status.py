import unittest from log_analyzer import LogAnalyzer

class TestInvalidStatus(unittest.TestCase): def test_status_above_599(self): analyzer = LogAnalyzer() logs = [ '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 600 512' ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["total_requests"], 0)
    self.assertEqual(result["invalid_entries"], 1)

def test_status_below_100(self):
    analyzer = LogAnalyzer()
    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 099 512'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["total_requests"], 0)
    self.assertEqual(result["invalid_entries"], 1)


if name == "main": unittest.main()
