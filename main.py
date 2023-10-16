from typing  import List
from fastapi import FastAPI, HTTPException
from models  import User, Gender, Role, UserUpdateRequest
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


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist!"
    )


@app.put("/api/v1/users/{user_id}")
async def modify_user(new_data: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if new_data.first_name is not None:
                user.first_name = new_data.first_name
            if new_data.last_name is not None:
                user.last_name = new_data.last_name
            if new_data.gender is not None:
                user.gender = new_data.gender
            if new_data.roles is not None:
                user.roles = new_data.roles
            return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist!"
    )


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=6102, log_level="info", log_config="log_config//log_config.yaml")
    server = uvicorn.Server(config)
    server.run()
