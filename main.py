from fastapi import FastAPI
app=FastAPI()

#Home route 
@app.get('/')
def home():
    return {'message: Hello my name is sonu'}

#About Route 
@app.get('/about')
def about():
    return {"message : Welcome to about  page..."}

#User Route 
@app.get('/users')
def user():
    return {
    "user_1":"abc" ,
    "user_2":"def"
    }
