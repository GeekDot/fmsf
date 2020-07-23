#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask_restplus import Namespace, fields


class UserDTO(object):

    api = Namespace('用户管理', description='用户相关操作')

    add_user_input = api.model('新增用户', {
        'phone': fields.String(required=True, description='电话'),
        'username': fields.String(required=True, description='姓名'),
        'mail': fields.String(required=False, description='邮箱')
    })

    get_user_output = api.model('获取用户', {
        'id': fields.Integer(required=True, description='用户id'),
        'phone': fields.String(required=True, description='电话'),
        'username': fields.String(required=True, description='姓名'),
        'mail': fields.String(required=True, description='邮箱')
    })
