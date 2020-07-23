#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask_testing import TestCase
from app import create_app, db


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        return create_app('dev')

    def setUp(self):
        db.drop_all()
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
