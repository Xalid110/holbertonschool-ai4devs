import re import ipaddress from collections import Counter

class LogAnalyzer: """Analyze Apache-style server logs and generate statistics."""


LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) - - '
    r'\[(?P<timestamp>[^\]]+)\] '
    r'"(?P<request>[^"]+)" '
    r'(?P<status>\d{3}) '
    r'(?P<size>\d+)$'
)

def parse_line(self, line: str) -> dict:
    """Parse and validate a single Apache log entry."""

    match = self.LOG_PATTERN.fullmatch(line.strip())

    if not match:
        raise ValueError("Malformed log entry")

    data = match.groupdict()

    try:
        ipaddress.ip_address(data["ip"])
    except ValueError:
        raise ValueError("Invalid IP address")

    if not data["timestamp"].strip():
        raise ValueError("Missing timestamp")

    request_parts = data["request"].split()

    if len(request_parts) != 3:
        raise ValueError("Invalid HTTP request")

    method, endpoint, protocol = request_parts

    if not re.fullmatch(r"[!#$%&'*+.^_`|~0-9A-Za-z-]+", method):
        raise ValueError("Invalid HTTP method")

    if not endpoint.startswith("/") and endpoint != "*":
        raise ValueError("Invalid endpoint")

    if not protocol.startswith("HTTP/"):
        raise ValueError("Invalid HTTP protocol")

    status = int(data["status"])
    size = int(data["size"])

    if not 100 <= status <= 599:
        raise ValueError("Invalid HTTP status")

    return {
        "ip": data["ip"],
        "timestamp": data["timestamp"],
        "method": method.upper(),
        "endpoint": endpoint,
        "status": status,
        "size": size
    }

def analyze(self, lines) -> dict:
    """Analyze log lines and return aggregated statistics."""

    total = 0
    successful = 0
    client_errors = 0
    server_errors = 0
    invalid_entries = 0

    visitors = set()
    methods = Counter()
    endpoints = Counter()

    for line in lines:
        try:
            entry = self.parse_line(line)
        except (ValueError, TypeError, AttributeError):
            invalid_entries += 1
            continue

        total += 1
        visitors.add(entry["ip"])
        methods[entry["method"]] += 1
        endpoints[entry["endpoint"]] += 1

        status = entry["status"]

        if 200 <= status <= 299:
            successful += 1
        elif 400 <= status <= 499:
            client_errors += 1
        elif 500 <= status <= 599:
            server_errors += 1

    error_count = client_errors + server_errors

    error_rate = (
        round((error_count / total) * 100, 2)
        if total > 0 else 0.0
    )

    most_requested = (
        sorted(
            endpoints,
            key=lambda endpoint: (-endpoints[endpoint], endpoint)
        )[0]
        if endpoints else None
    )

    return {
        "total_requests": total,
        "successful_requests": successful,
        "client_errors": client_errors,
        "server_errors": server_errors,
        "error_rate": error_rate,
        "unique_visitors": len(visitors),
        "requests_by_method": dict(sorted(methods.items())),
        "most_requested_endpoint": most_requested,
        "invalid_entries": invalid_entries
    }
if name == "main": analyzer = LogAnalyzer()


sample_logs = [
    '192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /api/users HTTP/1.1" 200 512',
    '192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /api/users HTTP/1.1" 201 256',
    '192.168.1.10 - - [12/Nov/2026:10:02:00 +0000] "GET /api/products HTTP/1.1" 404 128',
    '192.168.1.12 - - [12/Nov/2026:10:03:00 +0000] "GET /api/users HTTP/1.1" 500 64',
    '192.168.1.13 - - [12/Nov/2026:10:04:00 +0000] "DELETE /api/users/1 HTTP/1.1" 204 0'
]

import json
print(json.dumps(analyzer.analyze(sample_logs), indent=4))
