# -*- coding: utf-8 -*-
'''
Created on Tue Apr 12 18:07:35 2022

@author: codevacyacode
'''
# from datetime import datetime
import hashlib

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_

from . import models, schemas


'''
async def get_user(db: AsyncSession, user_id: int):
    query = select(models.User).where(models.User.id==user_id)
    result = await db.fetch_one(query)
    return result
'''

# Функции, обращающиеся к  таблице с пользователями чата 
async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(bytes(user.password, 'utf-8'))
    hash_str = hashed_password.hexdigest()
    new_user = models.User(email=user.email, hashed_password=hash_str,
                          nickname=user.nickname, online=False)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_email(db: AsyncSession, email: str):
    stmt = select(models.User).where((models.User).email==email)
    result = await db.execute(stmt)
    return result.scalars().one_or_none()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 20):
    query = select(models.User).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


# Функции, обращающиеся к таблице с сообщениями
async def get_all_messages(db:AsyncSession, skip: int = 0, limit: int = 20):
    stmt = select(models.Message).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_their_messages(db:AsyncSession, user_id: int, skip: int = 0,
                             limit: int = 20):
    stmt = select(models.Message).where(or_(
        models.Message.receiver_id==user_id,
        models.Message.sender_id==user_id
        )).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def create_message(db: AsyncSession, message: schemas.MessageCreate):
    new_message = models.Message(text=message.text, 
                                 sender_id=message.sender_id, 
                                 receiver_id=message.receiver_id,
                                 read=False)
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message