Bug Descriptions
Introduction

This document describes five intentionally buggy code snippets written in different programming languages. Each snippet contains a programming error that should be identified and fixed during the AI debugging exercise.

1. bug1.py
Language: Python
Intended Behavior: Return the last n items from a list.
Current Issue: The slicing expression uses -n-1, returning one extra element.
Expected Fix: Use items[-n:] to return exactly n elements.
2. bug2.js
Language: JavaScript
Intended Behavior: Fetch user information asynchronously and return the user's name.
Current Issue: The Promise is not awaited before accessing the user's name.
Expected Fix: Use await fetchUser(userId) before accessing the user object.
3. bug3.java
Language: Java
Intended Behavior: Calculate the sum of all elements in an integer array.
Current Issue: The loop condition uses i <= numbers.length, causing an array index out-of-bounds exception.
Expected Fix: Change the condition to i < numbers.length.
4. bug4.cpp
Language: C++
Intended Behavior: Find and return the maximum value in a vector.
Current Issue: The loop accesses an invalid vector index because it uses i <= numbers.size().
Expected Fix: Change the condition to i < numbers.size() and handle empty vectors.
5. bug5.py
Language: Python
Intended Behavior: Calculate the arithmetic average of a list of numbers.
Current Issue: The denominator incorrectly adds 1 to the number of elements.
Expected Fix: Divide the total by len(numbers).
Summary
File	Language	Bug Type
bug1.py	Python	Off-by-one slicing error
bug2.js	JavaScript	Missing await
bug3.java	Java	Array index error
bug4.cpp	C++	Vector boundary error
bug5.py	Python	Incorrect average calculation
Conclusion

These five examples demonstrate common programming mistakes across multiple languages. They can be used to evaluate AI debugging capabilities, identify root causes, and generate corrected implementations.
