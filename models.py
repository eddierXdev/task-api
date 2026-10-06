from pydantic import BaseModel

class Task(BaseModel):
    id:int
    title: str
    description: str
    completed: bool

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool

class TaskResponse(BaseModel):
    message:str
    task:Task

class DeleteResponse(BaseModel):
    message:str
    id_task:int