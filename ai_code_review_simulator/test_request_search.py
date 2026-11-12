"""Unit tests for request_search filtering and pagination."""

import unittest
from request_search import RequestItem, filter_requests, paginate_requests


class TestRequestSearch(unittest.TestCase):
    def setUp(self):
        self.sample_requests = [
            RequestItem("1", "Add dark mode toggle", "open", "2026-11-10T09:00:00Z", "alice"),
            RequestItem("2", "Fix login redirect bug", "resolved", "2026-11-11T14:30:00Z", "bob"),
            RequestItem("3", "Export requests to CSV", "open", "2026-11-12T08:15:00Z", "alice"),
            RequestItem("4", "Improve mobile navbar", "in_progress", "2026-11-12T10:00:00Z", "carol"),
        ]

    def test_filter_by_status_and_sort_order(self):
        res = filter_requests(self.sample_requests, status="open")
        self.assertEqual([r.id for r in res], ["3", "1"])

    def test_filter_by_keyword_case_insensitive(self):
        res = filter_requests(self.sample_requests, query="DARK MODE")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].id, "1")

    def test_filter_by_author_and_status(self):
        res = filter_requests(self.sample_requests, status="open", author="alice")
        self.assertEqual(len(res), 2)

    def test_invalid_status_raises_value_error(self):
        with self.assertRaises(ValueError):
            filter_requests(self.sample_requests, status="archived")

    def test_pagination_metadata(self):
        paginated = paginate_requests(self.sample_requests, page=1, page_size=2)
        self.assertEqual(len(paginated["items"]), 2)
        self.assertEqual(paginated["total_pages"], 2)
        self.assertTrue(paginated["has_next"])
        self.assertFalse(paginated["has_prev"])


if __name__ == "__main__":
    unittest.main()
