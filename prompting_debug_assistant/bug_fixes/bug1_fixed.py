# Fixed version of bug1.py

def calculate_class_average(scores):
    """
    Takes a list of numerical scores and computes the arithmetic mean.
    Returns 0.0 safely if the list is empty.
    """
    if not scores:
        return 0.0
        
    total_score = sum(scores)
    average = total_score / len(scores)
    return average


# Test cases for validation
test_scores_1 = [85, 90, 78, 92, 88]
test_scores_2 = []

print("Class 1 Average:", calculate_class_average(test_scores_1))
print("Class 2 Average:", calculate_class_average(test_scores_2))

assert calculate_class_average(test_scores_2) == 0.0, "Failed empty list validation"
