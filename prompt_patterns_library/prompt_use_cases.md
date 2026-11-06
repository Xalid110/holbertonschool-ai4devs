# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation
- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Unformatted code block
  - **Output**: Rewritten code with consistent style
- **Code Review**
  - **Goal**: Detect potential anti-patterns and performance bottlenecks
  - **Input**: Code snippet or pull request diff
  - **Output**: Detailed review with suggested improvements

## Debugging

- **Error Analysis**
  - **Goal**: Explain stack traces and suggest fixes
  - **Input**: Error message and surrounding code
  - **Output**: Root cause identification + solution steps
- **Edge Case Identification**
  - **Goal**: Find unhandled scenarios in code logic
  - **Input**: Function logic and expected behavior
  - **Output**: List of missing validations or edge cases
- **Performance Profiling**
  - **Goal**: Identify memory leaks and slow execution paths
  - **Input**: Execution logs and algorithm logic
  - **Output**: Recommendations for resource optimization

## Documentation

- **Docstring Generation**
  - **Goal**: Create standardized comments and API signatures
  - **Input**: Function or class definition
  - **Output**: Comprehensive docstrings (e.g., JSDoc, Google Python style)
- **README File Writing**
  - **Goal**: Produce clear project setup instructions
  - **Input**: Project structure and setup commands
  - **Output**: Structured README.md file

## Testing

- **Unit Test Generation**
  - **Goal**: Create test suites covering happy and failure paths
  - **Input**: Target function code
  - **Output**: Runnable unit test cases (e.g., pytest, Jest)
- **Mock Data Creation**
  - **Goal**: Generate realistic test payloads
  - **Input**: Database schema or JSON structure
  - **Output**: Sample datasets in JSON or SQL format
