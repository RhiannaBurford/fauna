from fastapi import FastAPI
from database import get_observations
from pydantic import BaseModel
from database import add_observation

app = FastAPI()

class Observation(BaseModel):
    species: str
    confidence: float
    date: str
    location: str
    image: str

@app.get("/")
def root():
    return {"message": "Welcome to Fauna!"}

@app.get("/observations")
def get_all_observations():
    return get_observations()

@app.post("/observations")
def create_observation(observation: Observation):
    add_observation(observation.model_dump())


