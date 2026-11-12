
def get_last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        raise ValueError("n cannot be negative")
    if n == 0:
        return []
    return items[-n:]


def main():
    assert get_last_items([10, 20, 30, 40, 50], 2) == [40, 50]
    assert get_last_items([1, 2, 3], 1) == [3]
    assert get_last_items([1, 2, 3], 0) == []
    assert get_last_items([1, 2], 5) == [1, 2]
    print("All bug1 tests passed!")


if __name__ == "__main__":
    main()
