<h2 align= center> Flask-Migrate 组件 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2020-08-22 </p>

### 一、Migrate 简介

`Migrate` 类似于 `Django` 中的 `manager.py` 的 `migrate`，它的作用是将 `ORM` 对象进行生成、迁移、更新到数据库的操作。

### 二、迁移顺序

1. 使用 `init` 初始化，将 `ORM` 对象生成可执行的 `SQL`。

2. 使用 `migrate` 将生成的 `SQL` 迁移到数据库。

3. 使用 `upgrade` 将 `SQL` 表结构更新到数据库中。

`Migrate` 可对标 `Git` 的操作。`init` 相当于 `git add`，`migrate` 相当于 `git commit`，`upgrade` 相当于 `git push`。当时只是作类比方便理解，功能还是不完全一样的。

### 三、示例

**_manager.py_**

	#!/usr/bin/env python3
	# -*- coding: UTF-8 -*-
	
	from flask import Flask
	from flask_sqlalchemy import SQLAlchemy
	from flask_migrate import Migrate, MigrateCommand
	from flask_script import Manager
	
	app = Flask(__name__)
	db = SQLAlchemy(app)
	manager = Manager(app)
	
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:makemoney@127.0.0.1:3306/flask_demo'

	# 第一个参数是 Flask 的实例，第二个参数是 Sqlalchemy 数据库实例
	migrate = Migrate(app, db)
	
	# manager 是 Flask-Script 的实例，这条语句在 Flask-Script 中添加一个 db 命令
	manager.add_command('db', MigrateCommand)
	
	
	if __name__ == '__main__':
	    manager.run()

#### 1. 初始化

	python manager.py db init

#### 2. 迁移数据

	python manager.py db migrate -m "init"
	
#### 3. 更新到数据库

	python manager.py db upgrade

### 四、版本回退

#### 1. 历史记录

可以根据 `history` 命令找到版本号。

	python manager.py db history

#### 2. 回滚到指定版本

使用 `downgrade` 命令可回滚到对应的版本。

	python manager.py db downgrade <版本号>
