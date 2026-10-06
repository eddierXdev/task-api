import sqlite3

connection=sqlite3.connect("task.db")

cursor=connection.cursor()

cursor.execute(
    """
    CREATE TABLE  IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    completed INTEGER    
    )
    """
)
connection.commit()
