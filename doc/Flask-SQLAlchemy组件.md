<h2 align= center> Flask-SQLAlchemy 组件 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2020-08-17 </p>

### 一、ORM

要了解 `ORM` 首先了解以下概念。

#### 1. 什么是持久化

持久化 `(Persistence)`，即把数据（如内存中的对象）保存到可永久保存的存储设备中（如磁盘）。持久化的主要应用是将内存中的数据存储在关系型的数据库中，当然也可以存储在磁盘文件中、`XML` 数据文件中等等。

#### 2. 什么是持久层

持久层 `(Persistence Layer)`，即专注于实现数据持久化应用领域的某个特定系统的一个逻辑层面，将数据使用者和数据实体相关联。

#### 3. 什么是 ORM

`ORM``(Object Relation Mapping)`，对象关系映射。主要实现模型对象到关系数据库数据的映射。

优点：

- 只需要面向对象编程，统一风格，不需要使用 `SQL` 语言。

- 实现数据模型和数据库的解藕，及不用关心是什么数据库，更改简单配置即可更换数据库。

缺点：

- 有部分性能损耗

### 二、SQLAlchemy

`SQLAlchemy` 是 `Python` 语言开发的 `ORM` 框架，是 `ORM` 具体实现的实例。

`SQLAlchemy中文文档`：[https://www.osgeo.cn/sqlalchemy/](https://www.osgeo.cn/sqlalchemy/)

### 三、Flask-SQLAlchemy

`Flask-SQLAlchemy` 是基于 `SQLAlchemy` 进行高度封装、简化，适用于 `Flask` 矿建的 `Flask` 组件。

`Flask-SQLAlchemy` 中文文档：[http://www.pythondoc.com/flask-sqlalchemy/](http://www.pythondoc.com/flask-sqlalchemy/)

### 三、基本配置

#### 1. 安装 flask_sqlalchemy
	
	pip install flask_sqlalchemy

#### 2. 连接 MySQL 数据库	

    SQLALCHEMY_DATABASE_URI = 'mysql://root:g3nt00567@127.0.0.1:3306/vnet_user_dev'
    
默认情况下，`MySQL` 使用的是 `mysqlclient` 驱动。当然也可以使用其他驱动，如：`mysqldb`、`pymysql` 等。

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:g3nt00567@127.0.0.1:3306/vnet_user_dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:g3nt00567@127.0.0.1:3306/vnet_user_dev'
    
#### 3. 连接其他数据库

**_oracle_**

    SQLALCHEMY_DATABASE_URI = 'oracle://root:g3nt00567@127.0.0.1:3306/vnet_user_dev'

**_mssql_**

    SQLALCHEMY_DATABASE_URI = 'mssql://root:g3nt00567@127.0.0.1:3306/vnet_user_dev'
    
**_sqlite_**

	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

**_redis_**

	REDIS_URL = 'redis://127.0.0.1:6379/1'

#### 4. 其他配置

	# 输出原始 SQL
	SQLALCHEMY_ECHO = False
	# 数据库连接池的大小
	SQLALCHEMY_POOL_SIZE = 1000
	# 动态追踪修改设置
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
更多配置请参考官方链接：[http://www.pythondoc.com/flask-sqlalchemy/config.html](http://www.pythondoc.com/flask-sqlalchemy/config.html)

### 四、模型定义

#### 1. 字段类型

| 类型名 | 说明 |
|---|---|
| Integer | 普通整数，一般是32位 |
| SmallInteger | 取值范围小的整数，一般是16位 |
| BigInteger | 不限制精度的整数 |
| Float | 浮点数 |
| Numeric | 普通整数，一般是32位 |
| String | 变长字符串 |
| Text | 变长字符串，对较长或不限长度的字符串做了优化 |
| JSON | JSON 数据|
| Unicode | 变长 Unicode 字符串 |
|UnicodeText | 变长 Unicode 字符串，对较长或不限长度的字符串做了优化 |
| Boolean | 布尔值 |
| Date | 日期 |
| Time | 时间 |
| DateTime | 日期和时间 |
| LargeBinary | 二进制文件 |

#### 2. 类型属性

| 属性名 | 说明 |
|---|---|
| primary_key | 如果为True，代表表的主键 |
| unique | 如果为True，代表这列不允许出现重复的值 |
| index | 如果为True，为这列创建索引，提高查询效率 |
| nullable | 如果为True，允许有空值，如果为 False，不允许有空值 |
| default | 为这列定义默认值 |

#### 3. 示例代码

	#!/usr/bin/env python3
	# -*- coding: UTF-8 -*-
	
	from app import db
	from app.lib.datetimeLib import dt
	

	# 用户表
	class Users(db.Model):
	
	    __tablename__ = 'users'
	
	    # id
	    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	    # 电话
	    phone = db.Column(db.String(11), unique=True, index=True)
	    # 邮箱
	    mail = db.Column(db.String(64), nullable=True, default=None)
	    # 用户
	    username = db.Column(db.String(128), nullable=True, default=None)
	    # 密码
	    password = db.Column(db.String(128), nullable=False)
	    # token
	    token = db.Column(db.String(256), unique=True)
	    # 盐值
	    salt = db.Column(db.String(32), nullable=False)
	    # 用户状态
	    status = db.Column(db.Integer, nullable=False, default=True)
	    # 创建时间
	    create_time = db.Column(db.DateTime, default=dt.datetime_orm)
	    # 修改时间
	    update_time = db.Column(db.DateTime, default=dt.datetime_orm, onupdate=dt.datetime_orm)
	    # 乐观锁
	    version = db.Column(db.BigInteger, nullable=False)
	
	    __mapper_args__ = {
	        "version_id_col": version
	    }
	
	    def __repr__(self):
	        return "<User (%s)>" % self.id

### 四、模型操作

#### 1. 过滤器

| 过滤器 | 说明 |
|---|---|
| filter() | 把过滤器添加到原查询上，返回一个新查询 |
| filter_by() | 把等值过滤器添加到原查询上，返回一个新查询 |
| limit() | 使用指定的值限定原查询返回的结果 |
| offset() | 偏移原查询返回的结果，返回一个新查询 |
| order_by() | 根据指定条件对原查询结果进行排序，返回一个新查询 |
| group_by() | 根据指定条件对原查询结果进行分组，返回一个新查询 |

#### 2. 执行器

| 执行器 | 说明 |
|---|---|
| all() | 以列表形式返回查询的所有结果 |
| first() | 返回查询的第一个结果，如果未查到，返回 None |
| get() | 返回指定主键对应的行，如不存在，返回 None |
| count() | 返回查询结果的数量 |
| paginate() | 返回一个 Paginate 对象，它包含指定范围内的结果 |

#### 3. 新增

	user = Users(username=username, password=password)
	db.session.add(user)
	db.session.commit()
	
先将对象添加到数据库的会话中，然后在提交到数据库，具体细节请参考对应的数据库。

如果，我们想立即返回刚刚新建数据的 `id` 该如何实现呢？其实也有简单的方法，通过 `flush` 即可。

	db.session.add(user)
	db.session.flush()
	user_id = user.id
	db.session.commit()

在提交之前，预先将任何剩余的状态刷新到数据库，这样数据库是不可见的，但是数据已经存在了，等拿到 `id` 之后再提交。

#### 4. 删除

删除记录是十分类似的，使用 `delete()` 实现删除功能。

	db.session.delete(user)
	db.session.commit()

#### 5. 修改

修改很简单，只需要将旧值替换为新值，然后提交就可以了。
	
	user = Users.query.get(1)
	user.username = 'new user'
	db.session.commit()

#### 6. 查询

- 查询所有用户数据

		Users.query.all()
		
- 查询有多少个用户

		Users.query.count()
		
- 查询第一个用户

		Users.query.first()		

- 查询 `id` 为 `1` 的用户

		Users.query.get(1)
		Users.query.filter(Users.id == 1).first()
		Users.query.filter_by(id=1).first()

- 查询名字结尾字符为 `vnet` 的所有数据

		Users.query.filter(Users.name.endswith('vnet')).all()

- 查询名字开始字符为 `vnet` 的所有数据
        
        	Users.query.filter(Users.name.startswith('vnet')).all()
        
- 查询名字包含字符为 `vnet` 的所有数据
        
		Users.query.filter(Users.name.contains('vnet')).all()

- 查询名字不等于 `vnet` 的所有数据
	
		Users.query.filter(not_(Users.name == 'vnet')).all()
		Users.query.filter(Users.name != 'vnet').all()

- 查询名字和邮箱都以 `vnet` 开头的所有数据

		Users.query.filter(and_(Users.name.startswith('vnet'), Users.email.startswith("li"))).all()
		Users.query.filter(Users.name.startswith('vnet'), Users.email.startswith('vnet')).all()

- 查询 `id` 为 `[1, 3, 5, 7, 9]` 的用户列表
   
		Users.query.filter(Users.id.in_([1, 3, 5, 7, 9])).all()

- 查询所有用户数据，并以邮箱正序排序
   
		Users.query.order_by(Users.email).all()

- 查询所有用户数据，并以邮箱倒序排序		
		
		Users.query.order_by(Users.email.desc()).all()  

- 查询指定每页 `3` 条，属于第 `2` 页的数据

		Users.query.paginate(2, 3, False).items
        		    
- 主键查询

		Users.query.get(1)
		
- 精确查询

		Users.query.filter_by(name='vnet').all()

- 模糊查询

		Users.query.filter(Users.name.contains('vnet')).all()

- 返回查询到第一个对象

		Users.query.filter_by(name='vnet').first()

- 返回查询到所有的对象
		
		Users.query.filter_by(name='vnet').all()

- 逻辑非查询	

		Users.query.filter(Users.name!='vnet').all()
	
- 逻辑与查询	

		from sqlalchemy import and_
		
		Users.query.filter(and_(Users.name!='vnet', Users.email.endswith('163.com'))).all()

- 逻辑或查询

		from sqlalchemy import or_
	
		Users.query.filter(or_(Users.name!='vnet', Users.email.endswith('163.com'))).all()

- 取反查询

		from sqlalchemy import not_
	
		Users.query.filter(not_(Users.name=='vnet')).all()
