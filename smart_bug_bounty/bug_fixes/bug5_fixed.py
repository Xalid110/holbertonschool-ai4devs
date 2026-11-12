
def calculate_average(numbers):
    """Calculate the arithmetic average."""
    if not numbers:
        return 0

    total = sum(numbers)
    return total / len(numbers)


def main():
    assert calculate_average([10, 20, 30, 40]) == 25
    assert calculate_average([5]) == 5
    assert calculate_average([2, 4]) == 3
    assert calculate_average([]) == 0
    assert calculate_average([-10, 10]) == 0

    print("All bug5 tests passed!")


if __name__ == "__main__":
    main()
