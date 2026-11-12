# Pull Request: Add Request Search, Filtering, and Pagination

## Summary
Implements keyword search, status/author filtering, chronological sorting, and pagination for submitted requests. Introduces `request_search.py` to support scalable querying as the request list grows, along with full unit test coverage.

## Changes
- Added `RequestItem` dataclass and `filter_requests()` in `request_search.py` supporting case-insensitive keyword search, status validation (`open`, `in_progress`, `resolved`), and author filtering
- Added `validate_status()` and `parse_timestamp()` helpers for input sanitization and ISO-8601 sorting
- Added `paginate_requests()` to slice filtered results and return pagination metadata (`total_items`, `total_pages`, `has_next`, `has_prev`)
- Added 5 unit tests in `test_request_search.py` covering status filtering, keyword matching, combined filters, invalid status error handling, and pagination boundaries

## Context
- **Size:** ~170 LOC (including unit tests)
- **Related Issue:** #14
- **Motivation:** As users submit more requests over time, scanning an unfiltered flat list becomes slow and cumbersome. Adding structured filtering and pagination improves usability and prepares the backend for larger datasets while keeping all existing and new tests passing.
