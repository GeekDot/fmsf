# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import read_config


# 创建 app
app = Flask(__name__)

# 创建 db
db = SQLAlchemy()


def create_app(env):

    # 读取环境变量
    app.config.from_object(read_config(env))

    # 日志配置
    app.logger.setLevel(app.config['LOG_LEVEL'])

    # 注册 db
    db.init_app(app)

    return app
