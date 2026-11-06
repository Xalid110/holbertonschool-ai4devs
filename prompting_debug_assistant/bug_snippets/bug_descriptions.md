# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Calculate the average of a list of numbers and return 0 if the list is empty.  
**Issue Type**: Runtime exception (ZeroDivisionError).  
**Notes**: Fails when passed an empty list because it divides by zero without checking list length.

## Bug 2 – bug2.js
**Intended Behavior**: Print numbers from 1 up to and including `n`.  
**Issue Type**: Off-by-one error / Loop logic issue.  
**Notes**: The loop condition `<` causes the function to stop before reaching `n`.

## Bug 3 – bug3.py
**Intended Behavior**: Check if a given string is a valid palindrome (ignoring casing).  
**Issue Type**: Logical error.  
**Notes**: Reverses the string incorrectly due to a misplaced slicing step and comparison logic.

## Bug 4 – bug4.cpp
**Intended Behavior**: Sum all elements in an integer vector and print the result.  
**Issue Type**: Syntax error / Misuse of library type.  
**Notes**: Missing namespace specifier and mismatched vector iterator comparison syntax.

## Bug 5 – bug5.js
**Intended Behavior**: Parse a numeric input string from an API response and double its value.  
**Issue Type**: Misuse of data types.  
**Notes**: Performs string concatenation instead of integer addition due to missing type conversion.
