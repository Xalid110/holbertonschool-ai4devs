def calculate_average(numbers):
    total = sum(numbers)
    # Bug: Division by zero when list is empty
    return total / len(numbers)

# Test cases
print(calculate_average([10, 20, 30]))
print(calculate_average([]))
