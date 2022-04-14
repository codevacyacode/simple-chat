# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:07:35 2022

@author: codevacyacode
"""
from datetime import datetime
import hashlib

from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(bytes(user.password, 'utf-8'))
    db_user = models.User(email = user.email, 
                          hashed_password = hashed_password,
                          nickname = user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()


def create_message(db: Session, message: schemas.MessageCreate, 
                   time: datetime):
    db_message = models.Message(**message.dict(), time = time)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message