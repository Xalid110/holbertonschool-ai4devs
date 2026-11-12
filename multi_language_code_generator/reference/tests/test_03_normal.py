import unittest from log_analyzer import LogAnalyzer

class TestNormalLogs(unittest.TestCase): def test_normal_logs(self): analyzer = LogAnalyzer()

    logs = [
        '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /api/users HTTP/1.1" 200 512',
        '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /api/users HTTP/1.1" 201 256',
        '192.168.1.10 - - [12/Nov/2026:10:02:00 +0000] "GET /api/products HTTP/1.1" 404 128',
        '192.168.1.12 - - [12/Nov/2026:10:03:00 +0000] "GET /api/users HTTP/1.1" 500 64',
        '192.168.1.13 - - [12/Nov/2026:10:04:00 +0000] "DELETE /api/users/1 HTTP/1.1" 204 0'
    ]

    result = analyzer.analyze(logs)

    self.assertEqual(result["total_requests"], 5)
    self.assertEqual(result["successful_requests"], 3)
    self.assertEqual(result["client_errors"], 1)
    self.assertEqual(result["server_errors"], 1)
    self.assertEqual(result["error_rate"], 40.0)
    self.assertEqual(result["unique_visitors"], 4)
    self.assertEqual(result["invalid_entries"], 0)


if name == "main": unittest.main()
