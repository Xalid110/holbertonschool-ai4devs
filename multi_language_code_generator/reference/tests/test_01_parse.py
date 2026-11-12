import unittest from log_analyzer import LogAnalyzer

class TestParse(unittest.TestCase): def test_valid_log(self): analyzer = LogAnalyzer() line = '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512'

    result = analyzer.parse_line(line)

    self.assertEqual(result["status"], 200)
    self.assertEqual(result["method"], "GET")
    self.assertEqual(result["endpoint"], "/home")


if name == "main": unittest.main()
