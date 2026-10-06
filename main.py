from fastapi import FastAPI
from models import Task,TaskCreate,TaskResponse,DeleteResponse
import crud

app = FastAPI()

@app.get("/")
async def welcome():
    return "Task Api"

@app.post("/tasks",response_model=TaskResponse)
async def create_task(task: TaskCreate):   

    return crud.create_task(task)
    
@app.get("/tasks",response_model=list[Task])
async def get_all_tasks():
    
    return crud.get_tasks()    
                            
@app.get("/tasks/{task_id}",response_model=Task)
async def get_task(task_id:int):

    return crud.get_task(task_id)
        
@app.put("/tasks/{task_id}",response_model=Task)
async def update_task(task_id:int, task_data: TaskCreate):
    
    return crud.update_task(task_id,task_data)

@app.delete("/tasks/{task_id}",response_model=DeleteResponse)
async def delete_task(task_id:int):

    return crud.delete_task(task_id)