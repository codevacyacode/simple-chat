# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:06:28 2022

@author: codevacyacode
"""
from datetime import datetime
from typing import List

from pydantic import BaseModel


class MessageBase(BaseModel):
# Базовый класс для сообщения
    sender_id: int
    text: str
    receiver_id: int


class MessageCreate(MessageBase):
# Класс используется при создании сообщения
    pass


class Message(MessageBase):
# Класс используется при чтении
    id: int
    time: datetime
    read: bool
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    nickname: str


class UserCreate(UserBase):
# Поле для пароля не будет доступно другим классам
    password: str


class User(UserBase):
    id: int
    online: bool
    inbox: List[Message] = []
    outbox: List[Message] = []

    class Config:
        orm_mode = True