#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

api_config = {
    'title': '用户权限认证服务 API',
    'version': '1.0',
    'description': '所有与用户相关的 RESTful API 服务'
}


class Config(object):

    SECRET_KEY = '5e8bca1c9aaa34aed6d069be3dfccd31'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
