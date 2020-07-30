#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from app import db
from app.model.user_model import Users


# 新增用户
def add_user(data):

    phone = data.get('phone', None)
    username = data.get('username', None)
    mail = data.get('mail', None)

    if phone is not None and username is not None:

        db_data = {
            'phone': phone,
            'username': username,
            'mail': mail,
        }

        db_data = Users(**db_data)
        db.session.add(db_data)
        db.session.commit()

        return True, 201

    else:
        return False, 400


# 获取用户
def get_user(data):

    phone = data.get('phone', None)

    if phone is not None:

        db_data = Users.query.filter(Users.phone == phone).first()

        if db_data is not None:

            re_data = {
                'id': db_data.id,
                'phone': db_data.phone,
                'mail': db_data.mail,
                'username': db_data.username
            }

        else:
            return False, 400

        return re_data, 200

    else:
        return False, 400
