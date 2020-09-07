#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bcrypt
import hashlib
import base64 as b64


class EncryptLib(object):

    @staticmethod
    def _init_(data):
        return data.encode(encoding='UTF-8')

    def md5(self, data):
        return hashlib.md5(self._init_(data)).hexdigest()

    def sha1(self, data):
        return hashlib.sha1(self._init_(data)).hexdigest()

    def sha224(self, data):
        return hashlib.sha224(self._init_(data)).hexdigest()

    def sha256(self, data):
        return hashlib.sha256(self._init_(data)).hexdigest()

    def sha384(self, data):
        return hashlib.sha384(self._init_(data)).hexdigest()

    def sha512(self, data):
        return hashlib.sha512(self._init_(data)).hexdigest()

    def base64(self, data):
        return str(b64.b64encode(self._init_(data)), 'UTF-8')

    @staticmethod
    def generate_salt():
        return str(bcrypt.gensalt(), 'UTF-8')

    @staticmethod
    def generate_password_hash(password, salt, rounds=8):

        if not password or not salt:
            raise ValueError('Password and salt must be non-empty.')

        if isinstance(password, str):
            password = bytes(password, 'UTF-8')

        if isinstance(salt, str):
            salt = bytes(salt, 'UTF-8')

        return str(bcrypt.hashpw(password + salt, bcrypt.gensalt(rounds)), 'UTF-8')

    @staticmethod
    def check_password_hash(password, salt, pw_hash):

        if isinstance(password, str):
            password = bytes(password, 'UTF-8')

        if isinstance(salt, str):
            salt = bytes(salt, 'UTF-8')

        if isinstance(pw_hash, str):
            pw_hash = bytes(pw_hash, 'UTF-8')

        return bcrypt.checkpw(password+salt, pw_hash)


et = EncryptLib()
