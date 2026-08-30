from fastapi import FastAPI, HTTPException
from schema import TaskSchema
from repository import TaskRepository

app = FastAPI()
repo = TaskRepository()

@app.get("/")
def read_root():
    return({"message":"A TO-DO list built with FastAPI"})

@app.get("/health")
def return_health():
    return({"status":"good"})

@app.get("/task/{id}", response_model=TaskSchema)
def return_task(id:int):
    task = repo.get_task(id)
    if task:
        return {
            'id': task["id"],
            'title': task['title'],
            'completed': task['completed']
        }
    raise HTTPException(status_code=404, detail="Task not Found!")


@app.post("/tasks", status_code=201)
def create_task(task:TaskSchema) -> TaskSchema:
    new_id = repo.create_task(task)
    return TaskSchema(id=new_id, title=task.title, completed=task.completed)

@app.put("/tasks/{id}", response_model=TaskSchema)
def update_task(id:int, newTask:TaskSchema):
    rows_affected = repo.update_task(id, newTask)
    if rows_affected == 0:
        raise HTTPException(status_code=404, detail="TASK NOT FOUND!")
    return TaskSchema(id=id, title=newTask.title, completed=newTask.completed)

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id:int):
    rows_affected = repo.delete_task(id)
    if rows_affected == 0:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    return None
