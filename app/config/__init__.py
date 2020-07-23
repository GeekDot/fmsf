#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from app.config.dev_config import DevConfig
from app.config.test_config import TestConfig
from app.config.prod_config import ProdConfig
from app.config.unit_config import UnitConfig


def read_config(config_name):

    if config_name == 'dev':
        return DevConfig

    if config_name == 'test':
        return TestConfig

    if config_name == 'prod':
        return ProdConfig

    if config_name == 'unit':
        return ProdConfig
