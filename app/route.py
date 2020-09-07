# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Blueprint
from flask_restplus import Api

from app.config.base_config import api_config
from app.controller.user_controller import api as user


# 创建蓝图
blueprint = Blueprint('api', __name__)
# 创建 REST API
api = Api(blueprint, **api_config)

# 注册路由
api.add_namespace(user, path='/user')
