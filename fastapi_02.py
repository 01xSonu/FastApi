from fastapi import FastAPI
app=FastAPI()

#user route(dynamic)
@app.get('/users/{user_id}')
def user(user_id:int):
    return {"user_id":user_id}