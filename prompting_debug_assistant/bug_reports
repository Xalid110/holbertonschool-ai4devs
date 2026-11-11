## Bug Report – bug1.py
- **Summary**: Division by zero runtime exception when passing an empty list of scores.
- **Root Cause**: The function directly computed `total_score / len(scores)` without validating if `scores` contained any elements.
- **Resolution**: Added a guard clause `if not scores: return 0.0` at the beginning of the function (suggested by AI).
- **Lesson Learned**: Always handle boundary edge cases such as empty collections before executing mathematical operations.

## Bug Report – bug2.js
- **Summary**: Off-by-one loop error omitting the upper boundary limit.
- **Root Cause**: The loop condition `i < limit` terminated the loop prematurely before printing `n`.
- **Resolution**: Changed the loop comparison operator from `<` to `<=` (suggested by AI).
- **Lesson Learned**: Verify loop termination criteria carefully when upper boundaries need to be included.

## Bug Report – bug3.py
- **Summary**: Incorrect string reversal logic skipping characters during palindrome validation.
- **Root Cause**: The slicing step `[::-2]` reversed the string while skipping every second character instead of performing a full step reversal.
- **Resolution**: Updated the slicing step expression to `[::-1]` (suggested by AI).
- **Lesson Learned**: Double-check slice step arguments in Python to ensure accurate sequence manipulation.

## Bug Report – bug4.cpp
- **Summary**: Compilation failure due to missing namespace prefix and broken iterator increment syntax.
- **Root Cause**: Unqualified `vector<int>` iterator reference and invalid increment operator `it+`.
- **Resolution**: Added explicit `std::` namespace qualification and updated increment operator to `++it` (AI-suggested fix with manual `assert(result == 150)` addition).
- **Lesson Learned**: Always specify correct standard library namespaces and explicit iterator increment operators in C++.

## Bug Report – bug5.js
- **Summary**: String concatenation instead of numeric addition when processing transaction input.
- **Root Cause**: The function treated `rawAmountString` as a string, causing the `+` operator to perform string joining instead of addition.
- **Resolution**: Wrapped the input in `Number(rawAmountString)` to explicitly convert it to a numerical type before computation (suggested by AI).
- **Lesson Learned**: Ensure string inputs from user interface elements or external APIs are explicitly converted to numeric types before mathematical processing.
