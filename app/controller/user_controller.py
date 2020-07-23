#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import request
from flask_restplus import Resource

from app.dto.user_dto import UserDTO
from app.service.user_service import add_user, get_user


api = UserDTO.api
add_user_input = UserDTO.add_user_input
get_user_output = UserDTO.get_user_output


# 用户相关操作
@api.route('')
@api.response(200, 'SUCCESS')
@api.response(400, 'BAD REQUEST')
@api.response(401, 'NOT AUTHORIZED')
@api.response(404, 'NOT FOUND')
class Users(Resource):

    @api.expect(add_user_input, validate=True)
    def post(self):
        """ 新增用户 """
        data = add_user(request.json)
        return data

    @api.param('phone', '电话')
    @api.marshal_with(get_user_output)
    def get(self):
        """ 获取用户 """
        data = get_user(request.args)
        return data
