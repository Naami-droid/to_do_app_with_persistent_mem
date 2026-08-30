import os
import psycopg
from psycopg.rows import dict_row
from schema import TaskSchema

class TaskRepository:
    def __init__(self):
        self.conn_str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")

    def get_connection(self):
        return psycopg.connect(self.conn_str, row_factory=dict_row)

    def get_task(self, task_id: int):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, title, completed FROM tasks WHERE id = %s", (task_id,))
                return cur.fetchone()

    def create_task(self, task: TaskSchema):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO tasks (title, completed) VALUES (%s, %s) RETURNING id",
                    (task.title, task.completed)
                )
                new_id = cur.fetchone()['id']
                conn.commit()
                return new_id

    def update_task(self, task_id: int, task: TaskSchema):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE tasks SET title = %s, completed = %s WHERE id = %s",
                    (task.title, task.completed, task_id)
                )
                conn.commit()
                return cur.rowcount

    def delete_task(self, task_id: int):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
                conn.commit()
                return cur.rowcount
