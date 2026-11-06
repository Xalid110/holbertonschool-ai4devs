## Bug 1 – bug1_fixed.py
- **Input**: `scores = []`
- **Expected Output**: `0.0`
- **Actual Output**: `0.0`
- **Fix Works**: Yes
- **Notes**: Added empty list check (`if not scores: return 0.0`) to avoid `ZeroDivisionError`.

## Bug 2 – bug2_fixed.js
- **Input**: `limit = 5`
- **Expected Output**: `1, 2, 3, 4, 5`
- **Actual Output**: `1, 2, 3, 4, 5`
- **Fix Works**: Yes
- **Notes**: Changed loop condition from `i < limit` to `i <= limit` to include upper bound `n`.

## Bug 3 – bug3_fixed.py
- **Input**: `input_string = "racecar"`
- **Expected Output**: `True`
- **Actual Output**: `True`
- **Fix Works**: Yes
- **Notes**: Replaced incorrect string slicing step `[::-2]` with standard reversal syntax `[::-1]`.

## Bug 4 – bug4_fixed.cpp
- **Input**: `data = {10, 20, 30, 40, 50}`
- **Expected Output**: `Total Sum: 150`
- **Actual Output**: `Total Sum: 150`
- **Fix Works**: Yes
- **Notes**: Added explicit `std::` namespace qualifier for `std::vector` and corrected loop iterator increment operator to `++it`.

## Bug 5 – bug5_fixed.js
- **Input**: `userEntry = "50"`
- **Expected Output**: `100`
- **Actual Output**: `100`
- **Fix Works**: Yes
- **Notes**: Converted input string to a number using `Number(rawAmountString)` to ensure numeric addition instead of string concatenation.
