# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:08:45 2022

@author: codevacyacode
"""
from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model = schemas.User)
async def create_user(user: schemas.UserCreate, 
                      db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email = user.email)
    if db_user:
        raise HTTPException(status_code = 400, 
                            detail = "Email already registered")
    return crud.create_user(db=db, user = user)


@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, 
                     limit: int = 100, 
                     db: AsyncSession = Depends(get_db)):
    users = await crud.get_users(db, skip = skip, limit = limit)
    return users


@app.get("/users/{user_id}", response_model = schemas.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    return db_user


@app.post("/users/{user_id}/messages/", response_model = schemas.Message)
async def create_message(
    time: datetime, 
    message: schemas.MessageCreate, 
    db: AsyncSession = Depends(get_db)
):
    result = await crud.create_message(db = db, message = message, time = time)
    return result


@app.get("/messages/", response_model = List[schemas.Message])
async def read_messages(skip: int = 0, 
                        limit: int = 100, 
                        db: AsyncSession = Depends(get_db)):
    messages = await crud.get_messages(db, skip = skip, limit = limit)
    return messages