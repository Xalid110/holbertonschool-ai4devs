
import unittest
from log_analyzer import LogAnalyzer


class TestEndpointTie(unittest.TestCase):

    def test_alphabetical_endpoint_tie(self):
        analyzer = LogAnalyzer()

        logs = [
            '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /users HTTP/1.1" 200 512',
            '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "GET /products HTTP/1.1" 200 256'
        ]

        result = analyzer.analyze(logs)

        self.assertEqual(
            result["most_requested_endpoint"],
            "/products"
        )

    def test_most_requested_endpoint(self):
        analyzer = LogAnalyzer()

        logs = [
            '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /users HTTP/1.1" 200 512',
            '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "GET /users HTTP/1.1" 200 256',
            '192.168.1.12 - - [12/Nov/2026:10:02:00 +0000] "GET /products HTTP/1.1" 200 128'
        ]

        result = analyzer.analyze(logs)

        self.assertEqual(
            result["most_requested_endpoint"],
            "/users"
        )


if __name__ == "__main__":
    unittest.main()
