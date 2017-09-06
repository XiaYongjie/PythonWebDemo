#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Administrator
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.phpgao.com
@software: PyCharm
@file: runserver.py
@time: 2017/9/6 16:15
"""
from flask import app


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
