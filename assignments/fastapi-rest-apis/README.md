# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You will create a comprehensive API application with multiple endpoints, proper request/response handling, and practical deployment considerations.

## 📝 Tasks

### 🛠️ Create a Basic API Server

#### Description
Set up a FastAPI application with a simple endpoint that returns JSON data. Install FastAPI and Uvicorn, then create your first API endpoint that demonstrates how to handle HTTP requests and return structured responses.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn packages
- Create a basic FastAPI application instance
- Define at least one GET endpoint that returns JSON data
- Run the server using Uvicorn on localhost:8000


### 🛠️ Implement CRUD Operations

#### Description
Create endpoints for Create, Read, Update, and Delete operations. Define appropriate HTTP methods (POST, GET, PUT, DELETE) and implement endpoints that manage a simple data resource.

#### Requirements
Completed program should:

- Implement POST endpoint to create new items with request body validation
- Implement GET endpoint to retrieve a single item or all items
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Use Pydantic models for request/response validation


### 🛠️ Add Error Handling and Validation

#### Description
Enhance your API with proper error handling, input validation, and meaningful HTTP status codes. Implement custom error handlers and use FastAPI's built-in validation features.

#### Requirements
Completed program should:

- Validate user input with appropriate error messages
- Return proper HTTP status codes (200, 201, 400, 404, 500)
- Handle edge cases and invalid requests gracefully
- Include at least one custom error handler
