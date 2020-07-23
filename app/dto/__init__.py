#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask_restplus import fields


def get_parser(api):
    parser = api.parser()
    parser.add_argument('Authorization', location='headers', help='token=xxxxxx;appKey=xxx')

    return parser


def return_value_dto(api):

    return_value = api.model('返回值', {
        'status': fields.Integer(required=True, description='返回值状态'),
        'message': fields.String(required=True, description='返回值消息'),
    })

    return return_value
