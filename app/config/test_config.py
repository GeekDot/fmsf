#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from app.config.base_config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
