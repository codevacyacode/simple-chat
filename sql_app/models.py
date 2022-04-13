# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:57:46 2022

@author: codevacyacode
"""

import sqlalchemy as sa

from .database import metadata


users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("email", sa.String),
    sa.Column("nickname", sa.String(32)),
    sa.Column("hashed_password", sa.String),
    sa.Column("online", sa.Boolean, default = False)
)

messages = sa.Table(
    "messages",
    metadata,
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("time", sa.DateTime),
    sa.Column("sender", sa.Integer, sa.ForeignKey("users.id")),
    sa.Column("receiver", sa.Integer, sa.ForeignKey("users.id")),
    sa.Column("text", sa.String, nullable = False)
)