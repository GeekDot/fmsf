#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import unittest

from app import create_app, db
from app.urls import blueprint

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


env = os.getenv('RUNTIME_ENV') or 'dev'
app = create_app(env)
app.register_blueprint(blueprint)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    """ runs user permission and auth service """
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)


@manager.command
def create():
    """ runs create db all data """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    """ runs the unit tests """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
