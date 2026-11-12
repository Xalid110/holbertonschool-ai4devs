import unittest from log_analyzer import LogAnalyzer

class TestInvalidIP(unittest.TestCase): def test_invalid_ip_address(self): analyzer = LogAnalyzer()

    logs = [
        '999.999.999.999 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["total_requests"], 0)
    self.assertEqual(result["invalid_entries"], 1)

def test_valid_ipv6_address(self):
    analyzer = LogAnalyzer()

    logs = [
        '2001:db8::1 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["total_requests"], 1)
    self.assertEqual(result["unique_visitors"], 1)


if name == "main": unittest.main()
