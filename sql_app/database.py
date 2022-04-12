# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:42:27 2022

@author: codevacyacode
"""
import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""
    Получаем корневую директорию проекта 
    и забираем из файла .env ссылку для подключения к БД
"""
load_dotenv(find_dotenv())
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()