# Task API

A REST API for task management built with **Python, FastAPI, Pydantic, and SQLite**.

This project implements the basic CRUD operations for creating, retrieving, updating, and deleting tasks. It also uses a separated project structure to keep the code organized and maintainable.

## Technologies

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLite**
* **Uvicorn**

## Project Structure

```text
Task_api/
│
├── main.py        # FastAPI endpoints and application configuration
├── crud.py        # CRUD operations for the database
├── models.py      # Pydantic data models
├── database.py    # Database connection and table creation
├── task.db       # SQLite database (generated locally)
└── README.md
```

## Features

The API allows you to:

* Create tasks
* Retrieve all tasks
* Retrieve a task by ID
* Update a task
* Delete a task
* Validate request data using Pydantic
* Handle errors when a task does not exist

## Task Model

Each task contains:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Practice API development",
  "completed": false
}
```

## Endpoints

| Method | Endpoint           | Description                  |
| ------ | ------------------ | ---------------------------- |
| GET    | `/`                | Checks if the API is running |
| GET    | `/tasks`           | Retrieves all tasks          |
| GET    | `/tasks/{task_id}` | Retrieves a task by ID       |
| POST   | `/tasks`           | Creates a new task           |
| PUT    | `/tasks/{task_id}` | Updates a task               |
| DELETE | `/tasks/{task_id}` | Deletes a task               |

## Create a Task Example

### POST `/tasks`

Request:

```json
{
  "title": "Learn FastAPI",
  "description": "Continue developing the Task API",
  "completed": false
}
```

Response:

```json
{
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Continue developing the Task API",
    "completed": false
  }
}
```

## Error Handling

If you try to access, update, or delete a task that does not exist, the API returns an HTTP `404` error.

Example:

```json
{
  "detail": "Task not Found"
}
```

## Installation

Clone the repository:

```bash
git clone <REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd Task_api
```

Install the dependencies:

```bash
pip install fastapi uvicorn pydantic
```

## Run the API

Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Interactive Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to test all the API endpoints directly from your browser.

## Architecture

The project separates the main responsibilities:

```text
Client
  │
  ▼
main.py
  │
  ▼
crud.py
  │
  ▼
database.py
  │
  ▼
SQLite
```

* `main.py` handles HTTP requests and API endpoints.
* `crud.py` contains the operations performed on tasks.
* `models.py` defines the data models and validation rules.
* `database.py` manages the SQLite connection and table creation.

## Project Goal

This project was developed as a learning project to practice the fundamentals of building **REST APIs with FastAPI**, including CRUD operations, data validation, SQLite databases, and organizing code by responsibility.
