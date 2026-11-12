
import unittest
from log_analyzer import LogAnalyzer


class TestHTTPMethods(unittest.TestCase):

    def test_different_http_methods(self):
        analyzer = LogAnalyzer()

        logs = [
            '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512',
            '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 201 256',
            '192.168.1.12 - - [12/Nov/2026:10:02:00 +0000] "PUT /users/1 HTTP/1.1" 200 128',
            '192.168.1.13 - - [12/Nov/2026:10:03:00 +0000] "DELETE /users/1 HTTP/1.1" 204 0'
        ]

        result = analyzer.analyze(logs)

        self.assertEqual(result["requests_by_method"]["GET"], 1)
        self.assertEqual(result["requests_by_method"]["POST"], 1)
        self.assertEqual(result["requests_by_method"]["PUT"], 1)
        self.assertEqual(result["requests_by_method"]["DELETE"], 1)

    def test_unknown_method(self):
        analyzer = LogAnalyzer()

        logs = [
            '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "PATCH /users/1 HTTP/1.1" 200 512'
        ]

        result = analyzer.analyze(logs)

        self.assertEqual(result["requests_by_method"]["PATCH"], 1)


if __name__ == "__main__":
    unittest.main()
