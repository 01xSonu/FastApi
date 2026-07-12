from fastapi import FastAPI
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    pin:int 

class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address

app=FastAPI()
@app.post("/create_user")
def user(user:User):
    return user