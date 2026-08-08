# To-Do List Application with Basic CRUD Operations

This project implements a simple To-Do list application using FastAPI, providing basic Create, Read, Update, and Delete (CRUD) operations. The tasks are managed in a SQLite database, ensuring that data persists across application restarts.

## Features

-   **Create Task**: Add new tasks to the list.
-   **Read Tasks**: Retrieve all tasks or a specific task by its ID.
-   **Update Task**: Modify an existing task.
-   **Delete Task**: Remove a task from the list.

## Technologies Used

-   FastAPI
-   Pydantic
-   SQLite

## Database Configuration

**Why SQLite was chosen:**
SQLite was chosen for its simplicity and zero-configuration setup. It stores the entire database in a single local file, making it ideal for a lightweight To-Do application without the overhead of setting up a separate database server.

**Where the database file is stored:**
The database is stored locally in the root directory of the project in a file named `tasks.db`.

## Database Viewer

Here is a screenshot of the database viewer showing the tasks:

![Database Viewer](db_viewer_screenshot.png)

### Example SQL Query Executed

```sql
SELECT * FROM tasks WHERE completed = 1;
```

## How to Run

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Install dependencies**:
    ```bash
    pip install "fastapi[all]" uvicorn
    ```
3.  **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

The API documentation (Swagger UI) will be available at `http://127.0.0.1:8000/docs`.

## API Endpoints

-   `GET /`: Root endpoint.
-   `GET /health`: Health check endpoint.
-   `GET /task/{id}`: Retrieve a specific task.
-   `POST /tasks`: Create a new task.
-   `PUT /tasks/{id}`: Update an existing task.
-   `DELETE /tasks/{id}`: Delete a task.
