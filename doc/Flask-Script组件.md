<h2 align= center> Flask-Script 组件 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2020-08-20 </p>

### 一、Script 简介

`Script` 的作用是可以通过命令行的形式来操作 `Python`。例如通过命令启动开发服务器、添加环境变量、设置参数、更改数据库等操作。

和 `Django` 的 `manager.py` 的功能一样，只不过 `Django` 是自动帮我们实现，`Flask` 需要我们自行配置。

### 二、命令的添加方式

1. 使用 `manage.command` 这个方法是用来添加那些不需要传递参数的命令的。

2. 使用 `manage.option` 这个方法是用来添加那些需要传递参数的命令的。有几个参数就需要些使用几个参数器。

3. 如果有一些命令是针对某一功能的，可以加这些命令放在同一个模块里。

### 三、示例

**_manager.py_**

	#!/usr/bin/env python3
	# -*- coding: UTF-8 -*-
	
	from flask import Flask
	from flask_script import Manager
	
	
	# 创建 app
	app = Flask(__name__)
	
	# 创建 manager
	manager = Manager(app)
	
	
	@manager.command
	def init():
	    """初始化"""
	    print('初始化完成!')
	
	
	@manager.command
	def hello():
	    """ Hello """
	    print('Hello World!')
	
	
	@manager.option('-n', '--name', dest='_name')
	def name(_name):
	    """ 参数 -n or --name """
	    print(_name)
	
	
	if __name__ == '__main__':
	    manager.run()

#### 1. 查看所有命令

	MacBook:demo zhangyi$ python manager.py

运行结果：
	 
	usage: manager.py [-?] {init,hello,name,shell,runserver} ...
	
	positional arguments:
	  {init,hello,name,shell,runserver}
	    init                初始化
	    hello               Hello
	    name                参数 -n or --name
	    shell               Runs a Python shell inside Flask application context.
	    runserver           Runs the Flask development server i.e. app.run()
	
	optional arguments:
	  -?, --help            show this help message and exit

#### 2. 执行 init 命令

	MacBook:demo zhangyi$ python manager.py init
		
运行结果：

	初始化完成!

#### 3. 执行 hello 命令

	MacBook:demo zhangyi$ python manager.py
	
运行结果：

	Hello World!

#### 4. 执行 name 命令及参数

	MacBook:demo zhangyi$ python manager.py name
	MacBook:demo zhangyi$ python manager.py name -n GeekDot
	MacBook:demo zhangyi$ python manager.py name --name GeekDot
	
运行结果：

	None
	GeekDot
	GeekDot
	
#### 5. 启动 Python Shell

	MacBook:demo zhangyi$ python manager.py shell
	
运行结果：

	>>> quit()

#### 6. 启动 Flask 服务

	MacBook:demo zhangyi$ python manager.py runserver

运行结果：

	 * Serving Flask app "manager" (lazy loading)
	 * Environment: production
	   WARNING: This is a development server. Do not use it in a production deployment.
	   Use a production WSGI server instead.
	 * Debug mode: off
	 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
