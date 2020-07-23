#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest

from app.test import BaseTestCase
from app.service.user_service import add_user, get_user


class TestUser(BaseTestCase):

    # 新增用户正向测试
    def test_positive_add_user(self):

        test_data = {
            'phone': '13800001111',
            'username': '极客点儿',
            'mail': '13800001111@jk.com'
        }

        positive_add = add_user(test_data)
        self.assertEqual(positive_add[0], True)

    # 新增用户反向测试
    def test_negative_add_user(self):

        test_data = {}

        negative_add = add_user(test_data)
        self.assertEqual(negative_add[0], False)

    # 获取用户正向测试
    def test_positive_get_user(self):

        test_data = {
            'phone': '13800001111',
            'username': '极客点儿',
            'mail': '13800001111@jk.com'
        }
        add_user(test_data)

        positive_set = get_user({'phone': '13800001111'})
        self.assertEqual(positive_set[1], 200)

    # 获取用户反向测试
    def test_negative_get_user(self):

        test_data = {
            'phone': '13800001111',
            'username': '极客点儿',
            'mail': '13800001111@jk.com'
        }
        add_user(test_data)

        negative_set = get_user({'phone': '13800001112'})
        self.assertEqual(negative_set[0], False)


if __name__ == '__main__':
    unittest.main()
