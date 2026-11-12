def get_last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        raise ValueError("n cannot be negative")

    if n == 0:
        return []

    return items[-n-1:]


def main():
    numbers = [10, 20, 30, 40, 50]
    result = get_last_items(numbers, 2)
    print("Last items:", result)


if __name__ == "__main__":
    main()
