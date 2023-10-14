from typing  import List
from fastapi import FastAPI
from models  import User, Gender, Role
from uuid    import UUID
import uvicorn

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("f9e682b1-8ef3-422e-b208-921399cc9064"),
        first_name="Kan",
        last_name="Wong",
        middle_name=None,
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("03ea79bb-21f8-41bd-bdda-cd9adb6eb68e"),
        first_name="Manda",
        last_name="Alpha",
        middle_name=None,
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


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=6102, log_level="info")
    server = uvicorn.Server(config)
    server.run()
