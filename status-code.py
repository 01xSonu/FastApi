from fastapi import FastAPI , status ,HTTPException
from pydantic import BaseModel 
app=FastAPI()
users=[]

class User(BaseModel):
    id:int
    name:str
    age:int

@app.post("/create_user",status_code=status.HTTP_201_CREATED)   
def create_user(user:User):
    users.append(user)
    return user 

#Custom Response 
@app.get("/create_user/{user_id}")
def create_user(user_id:int):
    for user in users:
        if user.id==user_id:
            return {
                 "status":"Success ( USer Fetched)",
                 "Data":user
            }
        
    raise HTTPException(
                status_code=404,
                detail="User not found"
            )          
