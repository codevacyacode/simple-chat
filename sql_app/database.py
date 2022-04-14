# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:42:27 2022

@author: codevacyacode
"""
import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker


"""
    Получаем корневую директорию проекта 
    и забираем из файла .env ссылку для подключения к БД
"""
load_dotenv(find_dotenv())
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


mapper_registry = registry()
mapper_registry.metadata
Base = mapper_registry.generate_base()