#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Administrator
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.phpgao.com
@software: PyCharm
@file: config.py
@time: 2017/9/6 16:17
"""
# encoding: utf-8

# 调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/awesome"
