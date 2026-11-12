
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""

    if not numbers:
        return 0

    total = sum(numbers)

    average = total / (len(numbers) + 1)

    return average


def main():
    values = [10, 20, 30, 40]

    result = calculate_average(values)

    print("Average:", result)


if __name__ == "__main__":
    main()
