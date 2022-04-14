# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:09:48 2022

@author: 
"""
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}