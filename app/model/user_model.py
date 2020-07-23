#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from app import db


# 用户表
class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), unique=True, index=True)
    mail = db.Column(db.String(64), nullable=True, default=None)
    username = db.Column(db.String(128), nullable=True, default=None)
