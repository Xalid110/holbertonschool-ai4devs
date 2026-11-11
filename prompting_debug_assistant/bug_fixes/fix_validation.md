Bug 1 – bug1_fixed.py
Input: scores = [] and scores = [85, 90, 78, 92, 88]
Expected Output: Class 1 Average: 86.6, Class 2 Average: 0.0
Actual Output:
text
Class 1 Average: 86.6
Class 2 Average: 0.0
Fix Works: Yes


Notes: Added empty list validation (if not scores: return 0.0) to avoid ZeroDivisionError. Assertion passed cleanly.

Bug 2 – bug2_fixed.js
Input: limit = 5
Expected Output: 1, 2, 3, 4, 5
Actual Output:
text
Starting sequence printing up to 5
Current item: 1
Current item: 2
Current item: 3
Current item: 4
Current item: 5
Sequence printing complete.
Fix Works: Yes


Notes: Changed loop boundary from i < limit to i <= limit. Output includes upper limit 5.

Bug 3 – bug3_fixed.py
Input: input_string = "racecar"
Expected Output: True
Actual Output:
text
Is 'racecar' palindrome? True
Is 'A man a plan a canal Panama' palindrome? True
Fix Works: Yes


Notes: Fixed string slicing from [::-2] to [::-1]. Assertion passed cleanly.

Bug 4 – bug4_fixed.cpp
Input: data = {10, 20, 30, 40, 50}
Expected Output: Total Sum: 150
Actual Output:
text
Total Sum: 150
Fix Works: Yes


Notes: Added std:: prefix for std::vector iterator and corrected increment to ++it. Compiled and executed cleanly.

Bug 5 – bug5_fixed.js
Input: userEntry = "50"
Expected Output: 100
Actual Output:
text
Expected result: 100
Actual result: 100
Fix Works: Yes


Notes: Applied Number(rawAmountString) conversion to ensure numerical addition instead of string concatenation.
