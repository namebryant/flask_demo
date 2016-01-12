# __author__ == ''
# -*- coding: utf-8 -*-

# 项目的
from app import db
import datetime



class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.IntField(default = 0)
