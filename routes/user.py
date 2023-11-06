from fastapi import APIRouter
from config.db import connection
from models.index import users
from schemas.user import User
from fastapi import HTTPException

user = APIRouter()

@user.get("/")
async def read_data():
    return connection.execute(users.select().fetchall())

@user.get("/{id}")
async def read_data(id: int):
    data = connection.execute(users.select().where(user.c.id == id).fetchall())
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data


@user.post("/")
async def write_data(user: User):
    existing_user = connection.execute(users.select().where(users.c.email == user.email)).fetchone()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    connection.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    )).fetchall()

@user.put("/{id}")
async def update_data(id: int, user: User):
    existing_user = connection.execute(users.select().where(users.c.id == id)).fetchone()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    connection.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return connection.execute(users.select()).fetchall()

@user.delete("/{id}")
async def delete_data(id: int):
    existing_user = connection.execute(users.select().where(users.c.id == id)).fetchone()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    connection.execute(users.delete().where(users.c.id == id))
    return connection.execute(users.select()).fetchall()