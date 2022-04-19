# -*- coding: utf-8 -*-
'''
Created on Tue Apr 12 18:07:35 2022

@author: codevacyacode
'''
from datetime import datetime
import hashlib

from databases import Database
from sqlalchemy import insert, select

from . import models, schemas


async def get_user(db: Database, user_id: int):
    query = select(models.User).where(models.User.id==user_id)
    result = await db.fetch_one(query)
    return result

async def get_user_by_email(db: Database, email: str):
    query = select(models.User).where(models.User.email==email)
    result = await db.fetch_one(query)
    return result

async def get_users(db: Database, skip: int = 0, limit: int = 100):
    query = select(models.User).offset(skip).limit(limit)
    result = await db.fetch_all(query)
    return result


async def create_user(db: Database, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(bytes(user.password, 'utf-8'))
    hash_str = hashed_password.hexdigest()
    query = insert(models.User).values(email=user.email, 
                                       hashed_password=hash_str,
                                       nickname=user.nickname,
                                       online=False)
    await db.execute(query)
    return user.email


async def get_messages(db: Database, skip: int = 0, limit: int = 100):
    query = select(models.Message).offset(skip).limit(limit)
    result = await db.fetch_all(query)
    return result


async def create_message(db: Database, message: schemas.MessageCreate):
    time = datetime.now()
    query = insert(models.Message).values(text=message.text, 
                                          sender_id=message.sender_id, 
                                          receiver_id=message.receiver_id, 
                                          time=time, 
                                          read=False)
    await db.execute(query)
    return message.sender_id # TODO: возвращать schemas.Message