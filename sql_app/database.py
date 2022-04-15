# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:42:27 2022

@author: codevacyacode
"""
import os

import databases
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base


"""
    Получаем корневую директорию проекта 
    и забираем из файла .env ссылку для подключения к БД
"""
load_dotenv(find_dotenv())
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')

database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base()