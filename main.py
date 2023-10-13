from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
from uuid import uuid4


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Kan",
        last_name="Wong",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Manda",
        last_name="Alpha",
        gender=Gender.female,
        roles=[Role.student, Role.user]
    ),
]


@app.get("/")
async def root():
    return {"Hello": "Kannis"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
