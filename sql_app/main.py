# -*- coding: utf-8 -*-
'''
Created on Tue Apr 12 18:08:45 2022

@author: codevacyacode
'''
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import database, crud, schemas


app = FastAPI()

# Dependency
async def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        await db.close()


@app.on_event('startup')
async def startup():
    async with (database.engine).begin() as conn:
        await conn.run_sync((database.Base).metadata.create_all)


'''    
@app.on_event('shutdown')
async def shutdown():
    await (database.database).disconnect()
'''


@app.post('/users/', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, 
                      db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, 
                            detail='Email уже зарегистрирован')
    else:
        result = await crud.create_user(db=db, user=user)
    result = await crud.create_user(db=db, user=user)
    return result


@app.get('/users/', response_model=List[schemas.User])
async def read_users(db: AsyncSession = Depends(get_db),
                     skip: int = 0, 
                     limit: int = 100):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users

'''
@app.get('/users/{user_email}', response_model = schemas.User)
async def read_email_user(user_email: str, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return db_user


@app.get('/users/{user_id}', response_model = schemas.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return db_user


@app.post('/users/{user_id}/messages/', response_model=schemas.Message)
async def create_message(
    message: schemas.MessageCreate, 
    db: AsyncSession = Depends(get_db)
):
    await crud.create_message(db=db, message=message)
    return message.receiver_id
'''


@app.get('/messages/', response_model=List[schemas.Message])
async def read_messages(skip: int = 0, 
                        limit: int = 100, 
                        db: AsyncSession = Depends(get_db)):
    messages = await crud.get_messages(db, skip=skip, limit=limit)
    return messages