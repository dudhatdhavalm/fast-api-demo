from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"Message": "Welcome to NobisLabs"}