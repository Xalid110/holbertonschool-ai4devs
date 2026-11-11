## Bug 1 – bug1_fixed.py
- **Input**: `scores = []` and `scores = [85, 90, 78, 92, 88]`
- **Expected Output**: Class 1 Average: 86.6, Class 2 Average: 0.0
- **Actual Output**: Class 1 Average: 86.6, Class 2 Average: 0.0
- **Fix Confirmation**: ✔ Fix works as expected
- **Notes**: Added empty list validation (`if not scores: return 0.0`) to avoid ZeroDivisionError. Passed assertion `assert calculate_class_average([]) == 0.0`.

## Bug 2 – bug2_fixed.js
- **Input**: `limit = 5`
- **Expected Output**: 1, 2, 3, 4, 5
- **Actual Output**: 1, 2, 3, 4, 5
- **Fix Confirmation**: ✔ Fix works as expected
- **Notes**: Changed loop boundary condition from `i < limit` to `i <= limit`. Verified output printed upper bound limit 5.

## Bug 3 – bug3_fixed.py
- **Input**: `input_string = "racecar"`
- **Expected Output**: True
- **Actual Output**: True
- **Fix Confirmation**: ✔ Fix works as expected
- **Notes**: Corrected slicing step from `[::-2]` to `[::-1]`. Passed assertion `assert is_valid_palindrome("racecar") is True`.

## Bug 4 – bug4_fixed.cpp
- **Input**: `data = {10, 20, 30, 40, 50}`
- **Expected Output**: Total Sum: 150
- **Actual Output**: Total Sum: 150
- **Fix Confirmation**: ✔ Fix works as expected
- **Notes**: Added std:: namespace to std::vector iterator and corrected increment to ++it. Executed cleanly with `assert(result == 150)`.

## Bug 5 – bug5_fixed.js
- **Input**: `userEntry = "50"`
- **Expected Output**: 100
- **Actual Output**: 100
- **Fix Confirmation**: ✔ Fix works as expected
- **Notes**: Applied explicit Number(rawAmountString) conversion to force numeric addition. Passed execution check `console.assert(result === 100)`.
