from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv('DB_CONFIG.env', override=True)

app = FastAPI()

DATABASE_URL = os.getenv("DB_URL") # Is in the DB_CONFIG.env file as DB_URL, insert your own to make this code work.
API_KEY = os.getenv("DB_KEY") # Is in the DB_CONFIG.env file as DB_KEY, insert your own to make this code work.

class Query(BaseModel):
    username: str
    score: int


def get_headers():
    return {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }


@app.get("/")
def frontend():
    return FileResponse("index.html")


@app.get("/api/scores")
def get_score():
    response = requests.get(
        DATABASE_URL,
        headers=get_headers(),
        params={"select": "username,score"}
    )

    if not response.ok:
        raise HTTPException(status_code=502, detail=response.text)

    return response.json()


@app.post("/api/post")
def create_row(data: Query):
    response = requests.post(
        DATABASE_URL,
        headers={
            **get_headers(),
            "Prefer": "return=representation"
        },
        json={
            "username": data.username,
            "score": data.score
        }
    )

    if not response.ok:
        raise HTTPException(status_code=502, detail=response.text)

    return response.json()
