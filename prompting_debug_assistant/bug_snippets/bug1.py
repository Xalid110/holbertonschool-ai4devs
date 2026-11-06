# Function to calculate the average score of a student class
# Intended behavior: Handle lists of numbers and return 0 for empty lists

def calculate_class_average(scores):
    """
    Takes a list of numerical scores and computes the arithmetic mean.
    If the list is empty, it should safely return 0.0.
    """
    total_score = 0
    for score in scores:
        total_score += score
    
    # Bug: Division by zero occurs when scores list is empty
    average = total_score / len(scores)
    return average


# Example usage for testing
test_scores_1 = [85, 90, 78, 92, 88]
test_scores_2 = []

print("Class 1 Average:", calculate_class_average(test_scores_1))
print("Class 2 Average:", calculate_class_average(test_scores_2))
