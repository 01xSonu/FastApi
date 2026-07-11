from fastapi import FastAPI
app=FastAPI()

#Optional parameters 
@app.get('/users')
def users(name:str=None):
    return {'name':name}
#Default values
@app.get('/products')
def users(limit:int=10):
    return {'limit':limit}

#multiple parameters
@app.get('/items')
def users(name: str =None , price:int=0):
    return {'name':name,
            'price':price}
