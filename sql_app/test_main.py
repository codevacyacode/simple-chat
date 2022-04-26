# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:27:48 2022

@author: codevacyacode
"""
from fastapi.testclient import TestClient

from .main import app


client = TestClient(app)


def test_check_their_messages():
    response = client.get(
        '/messages/1'
    )
    assert response.status_code == 200
    
    
def test_create_message():
    response = client.post(
        '/send-message/',
        json={'sender_id': 1, 'text': 'А я раньше зарегался', 'receiver_id': 2} 
    )
    assert response.status_code == 200 