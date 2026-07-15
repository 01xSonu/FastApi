from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

users=[]

class User(BaseModel):
    id:int
    name:str
    age:int

@app.post("/create_user")
def create_user(user:User):
    users.append(user)
    return user    

@app.put("/create_user/{user_id}")
def update_user(user_id: int, updated_user: User, notify: bool = False):

    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {
                "message": "User updated",
                "notify": notify,
                "data": updated_user
            }

    return {"error": "User not found"}

    