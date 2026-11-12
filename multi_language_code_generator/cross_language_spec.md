Cross-Language Specification - Log Analyzer
1. Algorithm Description
The Log Analyzer is an algorithm designed to process server log files and generate statistical reports.

The algorithm reads log entries, validates their format, extracts relevant information, and calculates important metrics.

The algorithm must produce consistent results regardless of the programming language used to implement it.

Main Operations
Count the total number of requests.
Count successful requests (HTTP 2xx).
Count client errors (HTTP 4xx).
Count server errors (HTTP 5xx).
Calculate the error rate as a percentage.
Identify unique visitors based on IP addresses.
Count requests by HTTP method (GET, POST, PUT, DELETE).
Identify the most frequently requested endpoint.
2. Input Format
The algorithm accepts a text file containing server log entries.

Each log entry follows this format:


text
IP_ADDRESS - - [TIMESTAMP] "HTTP_METHOD ENDPOINT PROTOCOL" STATUS_CODE SIZE
Example Input

text
192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /api/users HTTP/1.1" 200 512
192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /api/users HTTP/1.1" 201 256
192.168.1.10 - - [12/Nov/2026:10:02:00 +0000] "GET /api/products HTTP/1.1" 404 128
192.168.1.12 - - [12/Nov/2026:10:03:00 +0000] "GET /api/users HTTP/1.1" 500 64
192.168.1.13 - - [12/Nov/2026:10:04:00 +0000] "DELETE /api/users/1 HTTP/1.1" 204 0
Input Requirements
Input must be a UTF-8 encoded text file.
Each valid line must contain an IP address, timestamp, HTTP method, endpoint, status code, and response size.
HTTP status codes must be integers between 100 and 599.
Invalid lines must not stop the entire analysis.
3. Output Format
The algorithm must return a JSON object containing the calculated statistics.

Example Output

json
{
  "total_requests": 5,
  "successful_requests": 3,
  "client_errors": 1,
  "server_errors": 1,
  "error_rate": 40.0,
  "unique_visitors": 4,
  "requests_by_method": {
    "GET": 3,
    "POST": 1,
    "DELETE": 1
  },
  "most_requested_endpoint": "/api/users",
  "invalid_entries": 0
}
Output Requirements
total_requests: Number of valid log entries.
successful_requests: Number of responses with status codes 200–299.
client_errors: Number of responses with status codes 400–499.
server_errors: Number of responses with status codes 500–599.
error_rate: Percentage of requests with status codes 400–599, rounded to two decimal places.
unique_visitors: Number of distinct valid IP addresses.
requests_by_method: Number of requests grouped by HTTP method.
most_requested_endpoint: Endpoint with the highest request count.
invalid_entries: Number of malformed log entries.
If multiple endpoints have the same highest count, select the alphabetically first endpoint.

4. Edge Cases
The implementation must correctly handle the following situations:

Empty File: Return zero for all counters and an error rate of 0.0.
Malformed Entries: Skip invalid entries and increment invalid_entries.
Invalid IP Address: Reject entries containing an invalid IP address.
Invalid HTTP Status: Reject entries with status codes outside the 100–599 range.
Unknown HTTP Method: Accept valid HTTP methods even if they are not GET, POST, PUT, or DELETE.
Duplicate Visitors: Count the same IP address only once.
Missing Endpoint: Reject entries without a valid endpoint.
No Errors: Return an error rate of 0.0 when all requests are successful.
Tie Between Endpoints: Select the alphabetically first endpoint.
All Invalid Entries: Return zero valid requests and count all invalid entries.
5. Test Cases
Test Case 1 - Normal Log File
Input: Five valid log entries from the example input.

Expected Output:

Total requests: 5
Successful requests: 3
Client errors: 1
Server errors: 1
Error rate: 40.0%
Unique visitors: 4
Invalid entries: 0
Most requested endpoint: /api/users
Test Case 2 - Empty Log File
Input: An empty text file.

Expected Output:

Total requests: 0
Successful requests: 0
Client errors: 0
Server errors: 0
Error rate: 0.0%
Unique visitors: 0
Invalid entries: 0
Most requested endpoint: null
Test Case 3 - Malformed Log Entries
Input:


text
192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512
INVALID LOG ENTRY
192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 401 128
Expected Output:

Total requests: 2
Successful requests: 1
Client errors: 1
Server errors: 0
Error rate: 50.0%
Unique visitors: 2
Invalid entries: 1
Test Case 4 - Duplicate IP Addresses
Input:


text
192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512
192.168.1.10 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 201 256
192.168.1.10 - - [12/Nov/2026:10:02:00 +0000] "GET /about HTTP/1.1" 200 128
Expected Output:

Total requests: 3
Successful requests: 3
Unique visitors: 1
Error rate: 0.0%
Invalid entries: 0
Test Case 5 - All Requests Have Errors
Input:


text
192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 404 512
192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 500 128
Expected Output:

Total requests: 2
Successful requests: 0
Client errors: 1
Server errors: 1
Error rate: 100.0%
Unique visitors: 2
Invalid entries: 0
Test Case 6 - Multiple Endpoints With Equal Counts
Input:


text
192.168.1.10 - - [12/Nov/2026:10:00:00 +0000] "GET /users HTTP/1.1" 200 512
192.168.1.11 - - [12/Nov/2026:10:01:00 +0000] "GET /products HTTP/1.1" 200 256
Expected Output:

Total requests: 2
Successful requests: 2
Error rate: 0.0%
Most requested endpoint: /products
Invalid entries: 0
6. Cross-Language Implementation Requirements
The algorithm must be implementable in at least three programming languages:

Python
JavaScript (Node.js)
Java
All implementations must:

Follow the same input and output formats.
Apply identical validation rules.
Produce identical statistical results for the same input.
Handle all defined edge cases.
Pass all six test cases.
7. Performance Requirements
Process log files containing at least 100,000 entries.
Use a single-pass approach where practical.
Maintain approximately O(n) time complexity, where n is the number of log entries.
Use O(u + e) additional space, where u is the number of unique visitors and e is the number of unique endpoints.
8. Final Expected Result
A successful implementation produces consistent JSON statistics across Python, JavaScript, and Java.

The specification serves as a shared benchmark for evaluating correctness, performance, and cross-language consistency.
