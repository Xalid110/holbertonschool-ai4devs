import unittest from log_analyzer import LogAnalyzer

class TestErrorRate(unittest.TestCase): def test_error_rate_100_percent(self): analyzer = LogAnalyzer()

    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 404 512',
        '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 500 256'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["error_rate"], 100.0)

def test_error_rate_zero_percent(self):
    analyzer = LogAnalyzer()

    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512',
        '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 201 256'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["error_rate"], 0.0)

def test_error_rate_rounding(self):
    analyzer = LogAnalyzer()

    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512',
        '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "GET /about HTTP/1.1" 404 256',
        '192.168.1.12 - - [12/Nov/2026:10:02:00 +0000] "GET /contact HTTP/1.1" 200 128'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["error_rate"], 33.33)


if name == "main": unittest.main()
