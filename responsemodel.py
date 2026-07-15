from fastapi import FastAPI
from pydantic import BaseModel 

app =FastAPI()
class User(BaseModel):
    id:int
    name:str
    password:str

class Response(BaseModel):
    id:int
    name:str

@app.get("/user",response_model=Response)
def get_user():
    return {
        "id":"123",
        "name":"sonu"
        
    }
