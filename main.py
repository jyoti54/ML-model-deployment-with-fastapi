# print("Hello")

import uvicorn ##ASGI server for running the FastAPI application
from fastapi import FastAPI

app = FastAPI() #create the app object

@app.get("/") ##index or root endpoint
def index():
    return {"message": "Hello, World!" }

@app.get('/Welcome') ##route with single query parameter
def get_name(name: str):
    return {'welcome to fastapi': f'{name}'}

## Run the api with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

#uvicorn main:app --reload  
