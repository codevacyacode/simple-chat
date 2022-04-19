# -*- coding: utf-8 -*-
'''
Created on Tue Apr 12 17:57:46 2022

@author: codevacyacode
'''
from sqlalchemy import Column, ForeignKey 
from sqlalchemy import Integer, String, Boolean, DateTime

from .database import Base


class User(Base):
    __tablename__ = 'chat_user'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nickname = Column(String(32), index=True)
    hashed_password = Column(String)
    online = Column(Boolean, default=False)
    
    
class Message(Base):
    __tablename__ = 'message'
    
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime)
    sender_id = Column(Integer, ForeignKey('chat_user.id'))
    receiver_id = Column(Integer, ForeignKey('chat_user.id'))
    text = Column(String, nullable=False, index=True)
    read = Column(Boolean, default=False)