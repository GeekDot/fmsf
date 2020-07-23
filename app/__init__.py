# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import read_config


app = Flask(__name__)
db = SQLAlchemy()


def create_app(env):

    app.config.from_object(read_config(env))

    db.init_app(app)

    return app
