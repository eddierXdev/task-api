from fastapi import HTTPException
from database import connection
from models import Task,TaskCreate

def get_tasks():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows=cursor.fetchall()
    tasks=[]
    for row in rows:
        new_task=Task(
                id=row[0],
                title=row[1],
                description=row[2],
                completed=row[3]    
        )
        tasks.append(new_task)    
        
    return tasks       

def create_task(task:TaskCreate):
    cursor = connection.cursor()
    cursor.execute(
            "INSERT INTO tasks (title,description,completed) VALUES (?, ?, ?)",
            (task.title,task.description,task.completed)       
        )
    connection.commit()
    
    new_id=cursor.lastrowid
    
    new_task=Task(
        id=new_id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )    
    return  {
        "message":"Task created successfully",
        "task":new_task
          }
    
def get_task(task_id:int):
    cursor=connection.cursor()
    cursor.execute(
            "SELECT * FROM tasks WHERE id=?",
            (task_id,)   
        )
    row=cursor.fetchone()  
    if row is None:
            raise HTTPException(
                status_code=404,
                detail="Task not Found"
            )
    task=Task(
            id=row[0],
            title=row[1],
            description=row[2],
            completed=row[3]
        )
    return task  

def update_task(task_id:int,task_data:TaskCreate):
    cursor=connection.cursor()
    cursor.execute(
    """
    UPDATE tasks
    SET title=?,description=?,completed=?
    WHERE id=?
    """,
        (
        task_data.title,
        task_data.description,
        task_data.completed,
        task_id
        )
    )
    if cursor.rowcount==0:
        raise HTTPException(
            status_code=404,
            detail="Task not Found"
        )
    connection.commit()      
    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    )
    row=cursor.fetchone()
    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    task = Task(
    id=row[0],
    title=row[1],
    description=row[2],
    completed=row[3]
)
    return task

def delete_task(task_id:int):
    cursor=connection.cursor()
    cursor.execute(
       "DELETE FROM tasks WHERE id=?",
       (task_id,)
    )
    if cursor.rowcount==0:
           raise HTTPException(
               status_code=404,
               detail="Task not Found"
           )
    connection.commit()
    
    return{
        "message":"Task deleted",
        "id_task":task_id
    }    