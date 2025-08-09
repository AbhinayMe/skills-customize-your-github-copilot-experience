# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. You will create a simple API for managing a collection of resources, practicing endpoint creation, request handling, and response formatting.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI Application

#### Description
Set up a new FastAPI project and implement a basic API with endpoints to create, read, update, and delete (CRUD) items in a collection (e.g., books, users, or tasks).

#### Requirements
Completed program should:

- Use FastAPI to define an API application
- Implement endpoints for listing all items, retrieving a single item by ID, creating a new item, updating an item, and deleting an item
- Use Pydantic models for request and response validation
- Return appropriate HTTP status codes and JSON responses

### 🛠️	Add Data Persistence and Error Handling

#### Description
Enhance your API by adding in-memory data storage and robust error handling for invalid requests.

#### Requirements
Completed program should:

- Store items in a Python dictionary or list (no database required)
- Handle cases where an item is not found (return 404)
- Validate input data and return clear error messages for invalid requests
- (Optional) Add support for filtering or searching items via query parameters
