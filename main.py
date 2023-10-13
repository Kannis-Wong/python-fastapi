from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
from uuid import UUID


app = FastAPI()

db: List[User] = [
    User(
        id=UUID("f9e682b1-8ef3-422e-b208-921399cc9064"),
        first_name="Kan",
        last_name="Wong",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("03ea79bb-21f8-41bd-bdda-cd9adb6eb68e"),
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
