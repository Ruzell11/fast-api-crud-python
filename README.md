# FastAPI Backend

![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Description

The FastAPI Backend provides the backend functionality for a Todo application. It is built using FastAPI, SQLAlchemy for the database ORM, Pytest for testing, MySQL as the database, and Alembic for database migrations.

## Features

- FastAPI Framework: Fast and modern web framework for building APIs.
- SQLAlchemy ORM: Object-Relational Mapping for interacting with the MySQL database.
- Pytest for Testing: Easy and scalable testing.
- MySQL Database: Persistent data storage using MySQL.
- Alembic Migrations: Smooth and automated database migrations.

## Getting Started

### Prerequisites

- Python: Make sure you have Python installed on your machine.
- MySQL: Install and set up a MySQL database server.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Ruzell11/fast-api-crud-python
fast-api-crud-python
```

2. Install dependencies

```bash
pip install -r modules.txt
```

3.Database migration
```bash
alembic upgrade head
```

4.Run the server
```bash
uvicorn server:app --reload
```

5. Run test
```bash
python -m pytest
```
## Happy Coding !!
