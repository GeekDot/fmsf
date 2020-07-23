# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Blueprint
from flask_restplus import Api

from app.controller.user_controller import api as user


blueprint = Blueprint('api', __name__)
crm_user_service = {
    'title': '用户权限认证服务 API',
    'version': '1.0',
    'description': '所有与用户相关的 RESTful API 服务'
}
api = Api(blueprint, **crm_user_service)

api.add_namespace(user, path='/user')
