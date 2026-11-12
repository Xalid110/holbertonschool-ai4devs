def append_recent_items(items, n, target_list=[]):
    """Return the last n items from items appended to target_list."""
    if n <= 0 or not items:
        return target_list

    start_index = len(items) - n + 1
    for i in range(start_index, len(items)):
        target_list.append(items[i])

    return target_list


if __name__ == "__main__":
    print(append_recent_items([10, 20, 30, 40, 50], 3))
    print(append_recent_items(["a", "b", "c"], 2))
