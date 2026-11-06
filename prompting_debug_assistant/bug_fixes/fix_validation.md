## Bug 1 – bug1_fixed.py
- **Input**: `scores = []` and `scores = [85, 90, 78, 92, 88]`
- **Expected Output**: Class 1 Average: 86.6, Class 2 Average: 0.0
- **Actual Output**: Class 1 Average: 86.6, Class 2 Average: 0.0
- **Fix Works**: Yes
- **Notes**: Added empty list check (`if not scores: return 0.0`) to avoid ZeroDivisionError. Assertion passed successfully.

## Bug 2 – bug2_fixed.js
- **Input**: `limit = 5`
- **Expected Output**: 1, 2, 3, 4, 5
- **Actual Output**: 1, 2, 3, 4, 5
- **Fix Works**: Yes
- **Notes**: Changed loop condition from `i < limit` to `i <= limit`. Output includes upper bound limit 5 correctly.

## Bug 3 – bug3_fixed.py
- **Input**: `input_string = "racecar"`
- **Expected Output**: True
- **Actual Output**: True
- **Fix Works**: Yes
- **Notes**: Corrected slicing step from `[::-2]` to `[::-1]`. Palindrome check passed for racecar.

## Bug 4 – bug4_fixed.cpp
- **Input**: `data = {10, 20, 30, 40, 50}`
- **Expected Output**: Total Sum: 150
- **Actual Output**: Total Sum: 150
- **Fix Works**: Yes
- **Notes**: Added std:: prefix to std::vector and fixed iterator increment operator to `++it`. Compiled cleanly.

## Bug 5 – bug5_fixed.js
- **Input**: `userEntry = "50"`
- **Expected Output**: 100
- **Actual Output**: 100
- **Fix Works**: Yes
- **Notes**: Converted input string using Number(rawAmountString) to perform numeric addition instead of concatenation.
