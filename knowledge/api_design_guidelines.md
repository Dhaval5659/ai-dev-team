# API Design Guidelines

## Naming

Good:

GET /users
POST /users
GET /users/{id}

Bad:

GET /getUsers
POST /createUser

## Status Codes

200 - Success
201 - Created
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Internal Server Error

## Response Format

{
"success": true,
"message": "User created successfully",
"data": {}
}

## Versioning

Use:

/api/v1/users

instead of:

/users
