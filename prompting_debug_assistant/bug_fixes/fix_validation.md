## Bug 1 – bug1_fixed.py
- **Input**: `scores = []` and `scores = [85, 90, 78, 92, 88]`
- **Expected Output**:
Class 1 Average: 86.6
Class 2 Average: 0.0

- **Actual Output**:
Class 1 Average: 86.6
Class 2 Average: 0.0

- **Fix Works**: Yes
- **Notes**: Added empty list validation `if not scores: return 0.0` to avoid ZeroDivisionError runtime exception. Test assertion passed.

## Bug 2 – bug2_fixed.js
- **Input**: `limit = 5`
- **Expected Output**:
Starting sequence printing up to 5
Current item: 1
Current item: 2
Current item: 3
Current item: 4
Current item: 5
Sequence printing complete.

- **Actual Output**:
Starting sequence printing up to 5
Current item: 1
Current item: 2
Current item: 3
Current item: 4
Current item: 5
Sequence printing complete.

- **Fix Works**: Yes
- **Notes**: Changed boundary comparison from `i < limit` to `i <= limit`. Verified output includes upper limit 5.

## Bug 3 – bug3_fixed.py
- **Input**: `input_string = "racecar"`
- **Expected Output**:
Is 'racecar' palindrome? True
Is 'A man a plan a canal Panama' palindrome? True

- **Actual Output**:
Is 'racecar' palindrome? True
Is 'A man a plan a canal Panama' palindrome? True

- **Fix Works**: Yes
- **Notes**: Updated string reversal logic to `cleaned[::-1]`. Verified palindrome assertion successfully returned True.

## Bug 4 – bug4_fixed.cpp
- **Input**: `data = {10, 20, 30, 40, 50}`
- **Expected Output**:
Total Sum: 150

- **Actual Output**:
Total Sum: 150

- **Fix Works**: Yes
- **Notes**: Added std:: namespace qualification to std::vector iterator and corrected increment operator to ++it. Code compiled clean.

## Bug 5 – bug5_fixed.js
- **Input**: `userEntry = "50"`
- **Expected Output**:
Expected result: 100
Actual result: 100

- **Actual Output**:
Expected result: 100
Actual result: 100

- **Fix Works**: Yes
- **Notes**: Applied explicit Number(rawAmountString) conversion ensuring numeric addition instead of string concatenation.
