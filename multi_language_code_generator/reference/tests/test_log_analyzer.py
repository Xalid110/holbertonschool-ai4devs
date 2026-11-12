<WritingBlock id="41282" variant="document">import unittest

from log_analyzer import LogAnalyzer

def make_log(ip="192.168.1.10", method="GET",
endpoint="/home", status=200, size=512):
return (
f'{ip} - - [12/Nov/2026:10:00:00 +0000] '
f'"{method} {endpoint} HTTP/1.1" {status} {size}'
)

class TestLogAnalyzer(unittest.TestCase):

def setUp(self):
self.analyzer = LogAnalyzer()

def test_parse_valid_log(self):
entry = self.analyzer.parse_line(make_log())

self.assertEqual(entry["ip"], "192.168.1.10")
self.assertEqual(entry["method"], "GET")
self.assertEqual(entry["status"], 200)

def test_empty_logs(self):
result = self.analyzer.analyze([])

self.assertEqual(result["total_requests"], 0)
self.assertEqual(result["error_rate"], 0.0)
self.assertEqual(result["unique_visitors"], 0)
self.assertIsNone(result["most_requested_endpoint"])

def test_normal_logs(self):
logs = [
make_log(status=200),
make_log(ip="192.168.1.11", method="POST", status=201),
make_log(endpoint="/products", status=404),
make_log(ip="192.168.1.12", status=500),
make_log(ip="192.168.1.13", method="DELETE",
endpoint="/users/1", status=204, size=0)
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["total_requests"], 5)
self.assertEqual(result["successful_requests"], 3)
self.assertEqual(result["client_errors"], 1)
self.assertEqual(result["server_errors"], 1)
self.assertEqual(result["error_rate"], 40.0)
self.assertEqual(result["unique_visitors"], 4)
self.assertEqual(result["invalid_entries"], 0)

def test_malformed_entry(self):
logs = [
make_log(),
"INVALID LOG ENTRY"
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["total_requests"], 1)
self.assertEqual(result["invalid_entries"], 1)

def test_invalid_ip(self):
log = make_log(ip="999.999.999.999")

result = self.analyzer.analyze([log])

self.assertEqual(result["total_requests"], 0)
self.assertEqual(result["invalid_entries"], 1)

def test_invalid_status(self):
log = make_log(status=600)

result = self.analyzer.analyze([log])

self.assertEqual(result["total_requests"], 0)
self.assertEqual(result["invalid_entries"], 1)

def test_duplicate_visitors(self):
logs = [
make_log(ip="192.168.1.10"),
make_log(ip="192.168.1.10", endpoint="/about"),
make_log(ip="192.168.1.10", endpoint="/contact")
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["total_requests"], 3)
self.assertEqual(result["unique_visitors"], 1)

def test_unknown_http_method(self):
log = make_log(method="PATCH")

result = self.analyzer.analyze([log])

self.assertEqual(result["total_requests"], 1)
self.assertEqual(result["requests_by_method"]["PATCH"], 1)

def test_all_requests_have_errors(self):
logs = [
make_log(status=404),
make_log(ip="192.168.1.11", status=500)
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["error_rate"], 100.0)
self.assertEqual(result["client_errors"], 1)
self.assertEqual(result["server_errors"], 1)

def test_no_errors(self):
logs = [
make_log(status=200),
make_log(status=201),
make_log(status=204)
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["error_rate"], 0.0)
self.assertEqual(result["successful_requests"], 3)

def test_endpoint_tie(self):
logs = [
make_log(endpoint="/users"),
make_log(endpoint="/products")
]

result = self.analyzer.analyze(logs)

self.assertEqual(
result["most_requested_endpoint"],
"/products"
)

def test_error_rate_rounding(self):
logs = [
make_log(status=200),
make_log(status=404),
make_log(status=200)
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["error_rate"], 33.33)

def test_all_invalid_entries(self):
logs = [
"INVALID",
"ANOTHER INVALID ENTRY"
]

result = self.analyzer.analyze(logs)

self.assertEqual(result["total_requests"], 0)
self.assertEqual(result["invalid_entries"], 2)
self.assertEqual(result["error_rate"], 0.0)
self.assertIsNone(result["most_requested_endpoint"])

if name == "main":
unittest.main()</WritingBlock>
