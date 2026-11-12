## AI Review Log

### Review Personas Applied
- **Security Reviewer:** Focused on input bounds, ReDoS/injection risks, and malformed timestamp handling.
- **Performance Reviewer:** Focused on time complexity, redundant string allocations, and sorting overhead on large collections.
- **Maintainability Reviewer:** Focused on type annotations, modularity, edge-case test coverage, and code clarity.

---

### Inline Comments

- **(request_search.py, line 11) [Maintainability]:** Replace the raw `str` status field on `RequestItem` with an `Enum` (e.g., `RequestStatus`) so invalid status values are caught at instantiation time rather than only inside `validate_status()`.
- **(request_search.py, line 23) [Maintainability]:** `validate_status()` returns `None` for empty strings, which silently treats `status=""` as "no filter". Add a docstring note clarifying this behavior or raise a `ValueError` if an explicit empty string is passed via API query params.
- **(request_search.py, line 34) [Security]:** `parse_timestamp()` calls `datetime.fromisoformat()` without catching `ValueError`. A single malformed `created_at` string in storage will crash the entire search request with an unhandled exception—wrap parsing in a `try/except ValueError` block with a safe fallback or clear error message.
- **(request_search.py, line 47) [Security]:** Enforce a maximum length limit on the `query` parameter (e.g., 200 characters) before running substring matching to prevent excessive memory or CPU usage from oversized search payloads.
- **(request_search.py, line 52) [Performance]:** `item.status.lower()`, `item.author.lower()`, and `item.content.lower()` allocate new lowercase strings on every iteration. For larger lists, consider pre-normalizing indexed fields or avoiding repeated `.lower()` calls when filters are omitted.
- **(request_search.py, line 58) [Performance]:** `parse_timestamp(r.created_at)` is executed inside the `sort()` key function on every item even when `results` contains 0 or 1 elements. Skip sorting when `len(results) <= 1` to avoid unnecessary `datetime` parsing overhead.
- **(request_search.py, line 66) [Maintainability]:** `paginate_requests()` returns an untyped `dict`. Define a `PaginatedResult` `TypedDict` or `@dataclass` so callers get static type checking and autocomplete on keys like `has_next` and `total_pages`.

---

### Global Feedback

- **[Maintainability] Split Filtering and Sorting Responsibilities:** `filter_requests()` currently handles input normalization, multi-field predicate matching, and timestamp sorting in a single function. Extract `_matches_request()` as a dedicated helper function to improve readability and allow unit testing of matching logic independently from sorting.
- **[Performance] Combine Filtering and Pagination Pipeline:** Right now, callers must invoke `filter_requests()` and `paginate_requests()` sequentially, materializing the full filtered list in memory before slicing. Provide a convenience wrapper `search_requests()` that orchestrates validation, filtering, sorting, and pagination in one clean entry point.
- **[Security] Sanitize and Bound Page Inputs:** While `paginate_requests()` checks `page < 1` and `page_size > 100`, ensure upstream HTTP query parsers coerce non-integer inputs safely and return a `400 Bad Request` rather than a `500 Internal Server Error`.
- **[Maintainability] Expand Edge-Case Unit Tests:** Add test cases in `test_request_search.py` for empty request lists, out-of-range page numbers (e.g., `page=99` when `total_pages=2`), whitespace-only `query` strings, and invalid `page_size` bounds (`0` and `101`).
