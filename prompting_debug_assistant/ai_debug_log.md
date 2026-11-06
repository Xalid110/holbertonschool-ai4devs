## Bug 1 – bug1.py
**AI Diagnosis**: The function attempts to divide `total_score` by `len(scores)`. When an empty list is passed, `len(scores)` is 0, triggering a runtime `ZeroDivisionError`.  
**Suggested Fix**: Add a conditional check at the beginning of the function to verify if the list is empty before dividing. Return `0.0` if empty.  
**Alternative Fixes Tested**: Checked using a `try-except ZeroDivisionError` block.  
**Result**: Both fixes work as expected; the guard clause (`if not scores: return 0.0`) is cleaner.

## Bug 2 – bug2.js
**AI Diagnosis**: The loop condition `i < limit` contains an off-by-one error. It terminates when `i` reaches `limit`, omitting the target upper bound number `limit` itself.  
**Suggested Fix**: Change the loop condition from `i < limit` to `i <= limit`.  
**Alternative Fixes Tested**: None.  
**Result**: Fix works as expected, printing numbers up to and including `n`.

## Bug 3 – bug3.py
**AI Diagnosis**: The string slicing step `[::-2]` reverses the string while skipping every second character instead of creating a complete reverse string.  
**Suggested Fix**: Change the slicing expression from `cleaned[::-2]` to `cleaned[::-1]`.  
**Alternative Fixes Tested**: Tested using `reversed(cleaned)` joined with `""`.  
**Result**: Fix works as expected; `cleaned[::-1]` is standard Python syntax for string reversal.

## Bug 4 – bug4.cpp
**AI Diagnosis**: The loop uses an unqualified `vector<int>::const_iterator` type missing the `std::` namespace prefix, and contains a syntax error in the iterator increment operator (`it+` instead of `++it` or `it++`).  
**Suggested Fix**: Change `vector<int>` to `std::vector<int>` and update `it+` to `++it`.  
**Alternative Fixes Tested**: Used `auto` keyword (`for (auto it = numbers.begin(); it != numbers.end(); ++it)`).  
**Result**: Both fixes resolved the compilation error. Using `auto` or adding explicit `std::` namespaces works as expected.

## Bug 5 – bug5.js
**AI Diagnosis**: The input `rawAmountString` is passed as a string. Applying the `+` operator results in string concatenation ("5050") instead of numeric addition (100).  
**Suggested Fix**: Convert the input to a number using `Number(rawAmountString)` or `parseInt(rawAmountString, 10)` before doubling.  
**Alternative Fixes Tested**: Using unary plus operator `+rawAmountString`.  
**Result**: Fix works as expected, properly performing numeric calculation.
