# FastAPI Employee CRUD API

A beginner-friendly CRUD API built using FastAPI, Pydantic, SQLAlchemy, and SQLite.

This project demonstrates:
- REST API development with FastAPI
- Data validation using Pydantic
- Database integration using SQLAlchemy ORM
- SQLite database connectivity
- CRUD operations (Create, Read, Update, Delete)
- Dependency Injection with FastAPI
- 
## Tech Stack

- FastAPI
- Python
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Features

- Create employees
- Get all employees
- Get employee by ID
- Update employee details
- Partially update employee details
- Delete employees
- Persistent database storage using SQLite

## Project Structure

```bash
FASTAPI/
│
├── web.py          # Main FastAPI application
├── schemas.py      # Pydantic schemas
├── models.py       # SQLAlchemy models
├── database.py     # Database configuration
├── requirements.txt
└── .gitignore

### Installation

Clone the repository:

```
git clone <your-repo-link>
cd <repo-name>
```

Create virtual environment:

```
python -m venv env
```

Activate virtual environment:

### Windows

```
env\Scripts\activate
```

### Linux / Mac

```
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn web:app --reload
```
## API Documentation

Swagger UI: http://127.0.0.1:8000/docs 
ReDoc: http://127.0.0.1:8000/redoc
## Author
Suryansh Sharma
