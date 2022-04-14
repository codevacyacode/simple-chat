# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:07:35 2022

@author: codevacyacode
"""
from datetime import datetime
import hashlib

from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


def get_user(db: AsyncSession, user_id: int):
    result = await db.query(models.User).filter(
        models.User.id == user_id).first()
    return result

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.query(
        models.User).filter(models.User.email == email).first()
    return result

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.query(models.User).offset(skip).limit(limit).all()
    return result


async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(bytes(user.password, 'utf-8'))
    db_user = models.User(email = user.email, 
                          hashed_password = hashed_password,
                          nickname = user.nickname)
    await db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_messages(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.query(models.Message).offset(skip).limit(limit).all()
    return result


async def create_message(db: AsyncSession, message: schemas.MessageCreate, 
                   time: datetime):
    time = datetime.now()
    db_message = models.Message(**message.dict(), time = time)
    await db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message