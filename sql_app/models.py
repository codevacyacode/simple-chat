# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:57:46 2022

@author: codevacyacode
"""

from sqlalchemy import Column, ForeignKey 
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key = True),
    email = Column(String)
    nickname = Column(String(32))
    hashed_password = Column(String)
    online = Column(Boolean, default = False)
    
    inbox = relationship('Message', back_populates = 'receiver')
    outbox = relationship('Message', back_populates = 'sender')
    
class Message(Base):
    __tablename__ = 'message'
    
    id = Column(Integer, primary_key = True),
    time = Column(DateTime),
    sender_id = Column(Integer, ForeignKey('user.id'))
    receiver_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String, nullable = False)
    read = Column(Boolean, default = False)
    
    sender = relationship('User', foreign_keys = [sender_id],
                          back_populates = 'outbox')
    receiver = relationship('User', foreign_keys = [receiver_id],
                            back_populates = 'inbox')