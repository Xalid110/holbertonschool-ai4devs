# Reflection on AI-Assisted Debugging

## Introduction
Throughout this project, I used an AI assistant to identify, diagnose, and resolve standard bugs across five code snippets written in Python, JavaScript, and C++. The goal was to evaluate how effectively AI can accelerate the debugging workflow, assess the accuracy of its recommendations, and determine where human expertise remains indispensable during automated validation and test environment construction.

## AI Strengths
The AI demonstrated strong diagnostic speed when handling localized runtime errors and syntax mismatches. For straightforward bugs—such as the Python `ZeroDivisionError` in `bug1.py`, the JavaScript off-by-one loop boundary in `bug2.js`, and the string concatenation issue in `bug5.js`—the AI provided immediate, highly accurate solutions.

For instance, in `bug5.js`, the AI correctly identified that string concatenation was occurring instead of numeric addition and provided a clean fix:

```javascript
// AI-suggested fix
let processedValue = Number(rawAmountString);
let doubledValue = processedValue + processedValue;
