# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:07:35 2022

@author: codevacyacode
"""
from datetime import datetime
import hashlib

from databases import Database

from . import models, schemas


def get_user(db: Database, user_id: int):
    query = (models.User).filter(models.User.id==user_id).first()
    result = await db.fetch_one(query)
    return result

async def get_user_by_email(db: Database, email: str):
    query = (models.User).filter(models.User.email==email).first()
    result = await db.fetch_one(query)
    return result

async def get_users(db: Database, skip: int = 0, limit: int = 100):
    query = (models.User).offset(skip).limit(limit).all()
    result = await db.fetch_all(query)
    return result


async def create_user(db: Database, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(bytes(user.password, 'utf-8'))
    query = (models.User).insert().values(email=user.email, 
                                          hashed_password=hashed_password,
                                          nickname=user.nickname)
    result = await db.execute(query)
    return result


async def get_messages(db: Database, skip: int = 0, limit: int = 100):
    query = (models.Message).offset(skip).limit(limit).all()
    result = await db.fetch_all(query)
    return result


async def create_message(db: Database, message: schemas.MessageCreate, 
                   time: datetime):
    time = datetime.now()
    db_message = models.Message(**message.dict(), time=time)
    query = (models.Message).insert().values(db_message)
    await db.execute(query)
    return db_message