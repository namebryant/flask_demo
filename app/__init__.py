# __author__ == ''
# -*- coding: utf-8 -*-

#app目录是来存放应用的
#static是存放js,css等文件
#template存放html,模板生成文件
#__init__ models是数据模型 views是视图相关的

#做为一个python的包,主要开发的地方

from flask import Flask
from flask.ext.mongoengine import MongoEngine
import pymongo

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

from app import models,views
