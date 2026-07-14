from fastapi import FastAPI 
from pydantic import BaseModel 
app=FastAPI()
todos=[]

class Todo(BaseModel):
    id:int
    task:str
    completed:bool
#Create 
@app.post("/Todo")
def todo(todo:Todo):
    todos.append(todo)
    return{
        "message":"TASK created",
        'Your TODO LIST':todo
    }

#Read
@app.get("/Todo/{task_id}")
def todo(task_id:int):
    for todo in todos:
        if todo.id==task_id:
            return todo
    return{"message":"error"} 

#Update
@app.put("/Todo/{task_id}")
def todo(task_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==task_id:
            todos[index]=updated_todo
            return updated_todo    
#DELETE
@app.delete("/Todo/{task_id}")
def delete(task_id:int):
      
      for index, todo in enumerate(todos):

        if todo.id==task_id:

            todos.pop(index)
            return{"error":"data deleted"}
