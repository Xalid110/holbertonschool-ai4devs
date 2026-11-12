Benchmark Tasks
Task 1 - CRUD User Endpoint
Estimated Time: 20–30 minutes

Requirements:

Implement a REST API endpoint to create a new user.
Validate user input.
Ensure email addresses have a valid format.
Return appropriate HTTP status codes.
Inputs:


json
{
  "name": "John Doe",
  "email": "john@example.com"
}
Outputs:


json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
Acceptance Criteria:

Returns HTTP 201 when a user is successfully created.
Returns HTTP 400 when required fields are missing.
Returns HTTP 400 when the email format is invalid.
Each user receives a unique ID.
Task 2 - To-Do List Application
Estimated Time: 15–25 minutes

Requirements:

Implement functionality to add new tasks.
Allow users to view all tasks.
Allow users to mark tasks as completed.
Allow users to delete tasks.
Validate task descriptions.
Inputs:


json
{
  "title": "Complete GitHub assignment",
  "completed": false
}
Outputs:


json
{
  "id": 1,
  "title": "Complete GitHub assignment",
  "completed": false
}
Acceptance Criteria:

Users can successfully create new tasks.
Users can retrieve the complete task list.
Users can update task completion status.
Users can delete existing tasks.
Empty task titles are rejected with an appropriate error.
Task 3 - Password Strength Validator
Estimated Time: 15–20 minutes

Requirements:

Create a function that validates password strength.
Require a minimum password length of 8 characters.
Require at least one uppercase letter.
Require at least one lowercase letter.
Require at least one number.
Require at least one special character.
Inputs:

Example password:


text
MyPassword123!
Outputs:


json
{
  "valid": true,
  "message": "Password meets all security requirements."
}
Invalid password example:


text
password123
Expected output:


json
{
  "valid": false,
  "message": "Password must contain an uppercase letter and a special character."
}
Acceptance Criteria:

Accepts passwords that satisfy all requirements.
Rejects passwords shorter than 8 characters.
Rejects passwords without uppercase letters.
Rejects passwords without lowercase letters.
Rejects passwords without numbers.
Rejects passwords without special characters.
Returns clear validation messages for invalid passwords.
Summary

Task	Description	Estimated Time
Task 1	CRUD User Endpoint	20–30 minutes
Task 2	To-Do List Application	15–25 minutes
Task 3	Password Strength Validator	15–20 minutes
Total Estimated Time: 50–75 minutes
