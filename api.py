from fastapi import FastAPI
from database import get_observations

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Fauna!"}

@app.get("/observations")
def get_all_observations():
    return get_observations()
