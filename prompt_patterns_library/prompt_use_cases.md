# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Expected output**: Optimized code + explanation
- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Unformatted code block
  - **Expected output**: Rewritten code with consistent style
- **Code Review**
  - **Goal**: Detect potential anti-patterns and performance bottlenecks
  - **Input**: Code snippet or pull request diff
  - **Expected output**: Detailed review with suggested improvements

## Debugging

- **Error Analysis**
  - **Goal**: Explain stack traces and suggest fixes
  - **Input**: Error message and surrounding code
  - **Expected output**: Root cause identification + solution steps
- **Edge Case Identification**
  - **Goal**: Find unhandled scenarios in code logic
  - **Input**: Function logic and expected behavior
  - **Expected output**: List of missing validations or edge cases
- **Performance Profiling**
  - **Goal**: Identify memory leaks and slow execution paths
  - **Input**: Execution logs and algorithm logic
  - **Expected output**: Recommendations for resource optimization

## Documentation

- **Docstring Generation**
  - **Goal**: Create standardized comments and API signatures
  - **Input**: Function or class definition
  - **Expected output**: Comprehensive docstrings (e.g., JSDoc, Google Python style)
- **README File Writing**
  - **Goal**: Produce clear project setup instructions
  - **Input**: Project structure and setup commands
  - **Expected output**: Structured README.md file
- **API Documentation**
  - **Goal**: Write endpoint specifications and request/response payloads
  - **Input**: Controller code or route definitions
  - **Expected output**: OpenAPI/Swagger standard documentation

## Testing

- **Unit Test Generation**
  - **Goal**: Create test suites covering happy and failure paths
  - **Input**: Target function code
  - **Expected output**: Runnable unit test cases (e.g., pytest, Jest)
- **Mock Data Creation**
  - **Goal**: Generate realistic test payloads
  - **Input**: Database schema or JSON structure
  - **Expected output**: Sample datasets in JSON or SQL format
- **Integration Test Planning**
  - **Goal**: Outline end-to-end integration flows
  - **Input**: System architecture and service interaction flow
  - **Expected output**: Step-by-step integration test scenarios
