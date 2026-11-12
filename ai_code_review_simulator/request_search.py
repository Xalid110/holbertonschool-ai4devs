"""Request search, status filtering, and pagination utilities."""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


VALID_STATUSES = {"open", "in_progress", "resolved"}


@dataclass
class RequestItem:
    """Represents a single user request record."""

    id: str
    content: str
    status: str
    created_at: str
    author: str = "anonymous"


def validate_status(status: Optional[str]) -> Optional[str]:
    """Validate and normalize an optional status filter."""
    if status is None or status.strip() == "":
        return None
    normalized = status.strip().lower()
    if normalized not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status '{status}'. Must be one of: {', '.join(sorted(VALID_STATUSES))}."
        )
    return normalized


def parse_timestamp(iso_str: str) -> datetime:
    """Parse an ISO-8601 timestamp string safely."""
    cleaned = iso_str.replace("Z", "+00:00")
    return datetime.fromisoformat(cleaned)


def filter_requests(
    requests: List[RequestItem],
    query: Optional[str] = None,
    status: Optional[str] = None,
    author: Optional[str] = None,
    sort_desc: bool = True,
) -> List[RequestItem]:
    """Filter and sort RequestItem entries by keyword, status, and author."""
    normalized_status = validate_status(status)
    normalized_query = query.strip().lower() if query and query.strip() else None
    normalized_author = author.strip().lower() if author and author.strip() else None

    results: List[RequestItem] = []
    for item in requests:
        if normalized_status and item.status.lower() != normalized_status:
            continue
        if normalized_author and item.author.lower() != normalized_author:
            continue
        if normalized_query and normalized_query not in item.content.lower():
            continue
        results.append(item)

    results.sort(key=lambda r: parse_timestamp(r.created_at), reverse=sort_desc)
    return results


def paginate_requests(
    requests: List[RequestItem],
    page: int = 1,
    page_size: int = 10,
) -> dict:
    """Return a paginated slice of requests along with metadata."""
    if page < 1:
        raise ValueError("Page number must be >= 1.")
    if page_size < 1 or page_size > 100:
        raise ValueError("Page size must be between 1 and 100.")

    total_items = len(requests)
    total_pages = max(1, (total_items + page_size - 1) // page_size)
    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": requests[start:end],
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }
