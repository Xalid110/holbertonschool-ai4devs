import unittest from log_analyzer import LogAnalyzer

class TestDuplicateVisitors(unittest.TestCase): def test_duplicate_ip_addresses(self): analyzer = LogAnalyzer()

    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512',
        '192.168.1.10 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 201 256',
        '192.168.1.10 - - [12/Nov/2026:10:02:00 +0000] "GET /about HTTP/1.1" 200 128'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["total_requests"], 3)
    self.assertEqual(result["unique_visitors"], 1)

def test_multiple_unique_visitors(self):
    analyzer = LogAnalyzer()

    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512',
        '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "GET /about HTTP/1.1" 200 256'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["unique_visitors"], 2)


if name == "main": unittest.main()
