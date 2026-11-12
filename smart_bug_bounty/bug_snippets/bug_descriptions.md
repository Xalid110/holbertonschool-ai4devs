Bug Descriptions
Introduction

This document describes five intentionally buggy code snippets written in four programming languages. Each description matches the corresponding source file and explains its intended behavior, current issue, and suggested fix.

1. bug1.py
Language: Python
Intended Behavior: Return exactly the last n items from a list without modifying the original list.
Current Issue: The slicing expression items[-n-1:] returns one extra element.
Expected Fix: Use items[-n:] to return exactly the requested number of elements. Preserve the special case where n is zero.
2. bug2.js
Language: JavaScript
Intended Behavior: Fetch user information asynchronously and return the user's name.
Current Issue: The function getUserName() calls fetchUser() without awaiting its Promise. Therefore, user.name is undefined.
Expected Fix: Use await fetchUser(userId) before accessing the user's properties.
3. bug3.java
Language: Java
Intended Behavior: Calculate and return the sum of all elements in an integer array.
Current Issue: The loop uses i <= numbers.length, which attempts to access an array element outside its valid index range.
Expected Fix: Change the loop condition to i < numbers.length.
4. bug4.cpp
Language: C++
Intended Behavior: Find and return the maximum integer value in a vector.
Current Issue: The loop uses i <= numbers.size(), causing an out-of-range vector access. The function also assumes the vector is not empty.
Expected Fix: Change the loop condition to i < numbers.size() and check whether the vector is empty before accessing its first element.
5. bug5.py
Language: Python
Intended Behavior: Calculate the arithmetic average of all numbers in a list.
Current Issue: The calculation divides the sum by len(numbers) + 1 instead of the actual number of elements.
Expected Fix: Divide the sum by len(numbers). Keep the empty-list check to avoid division by zero.
Summary
File	Language	Bug Type
bug1.py	Python	Off-by-one slicing error
bug2.js	JavaScript	Missing await
bug3.java	Java	Array boundary error
bug4.cpp	C++	Vector boundary error
bug5.py	Python	Incorrect average calculation
Conclusion

These five code snippets demonstrate common programming errors in Python, JavaScript, Java, and C++.

Each example has a clearly defined expected behavior and a specific bug that can be investigated and corrected using AI-assisted debugging techniques.
