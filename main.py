from fastapi import FastAPI, HTTPException
import pydantic
from schema import TaskSchema
from creating_table import get_db_connection

app=FastAPI()

@app.get("/")
def read_root():
    return({"message":"A TO-DO list built with FastAPI"})

@app.get("/health")
def return_health():
    return({"status":"good"})

@app.get("/task/{id}", response_model=TaskSchema)
def return_task(id:int):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks WHERE id =?", (id ,))
    task=cursor.fetchone()
    conn.close()
    if task:
        return {
            'id': task["id"],
            'title':task['title'],
            'completed': bool(task['completed'])
        }
    raise HTTPException(status_code=404, detail="Task not Found!")


@app.post("/tasks", status_code=201)
def create_task(task:TaskSchema)->TaskSchema:
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tasks (title, completed) VALUES(?,?)",
                    (task.title, int(task.completed)))
    conn.commit()
    new_id=cursor.lastrowid
    conn.close()
    return TaskSchema(id=new_id, title=task.title, completed=task.completed)
@app.put("/tasks/{id}", response_model=TaskSchema)
def update_task(id:int,newTask:TaskSchema):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE tasks SET title = ?, completed =? WHERE id= ?",
                    (newTask.title, int(newTask.completed), id))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    if rows_affected == 0:
        raise HTTPException(status_code=404, detail="TASK NOT FOUND!")
    return TaskSchema(id=id, title=newTask.title, completed=bool(newTask.completed))

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id:int):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?" ,(id,))
    conn.commit()
    rows_affected=cursor.rowcount
    if rows_affected == 0:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    return None
