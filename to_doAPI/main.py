from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #Instance of app

@app.get("/") #GET endpoint
def read_root():
    return {"message": "This is the To-Do List API, version 1.0."} #Welcome message, displays at the app startup

class Task(BaseModel): #Basic task class, defines key properties of a task
    id: int
    title: str
    description: str
    completed: bool = False

tasks = []

@app.post("/tasks/") #Basic POST operation to create a task
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/") #Basic GET operation to get list of tasks
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}") #Basic PUT operation to update a task
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    return {"error": "Task not found"}
        
@app.delete("/tasks/{task_id}") #Basic DELETE operation to delete a task
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted"}
