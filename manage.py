# __author__ == ''
# -*- coding: utf-8 -*-

# 项目的外部脚本管理文件

from app import app
from app.models import Todo
from flask.ext.script import Manager

manager = Manager(app)

@manager.command
def save():
    todo = Todo(content = 'kobebryant')
    todo.save()

@manager.command
def fetch():
    todos = Todo.objects.all()
    for todo in todos:
        print todo.content


if __name__ == '__main__':
    manager.run()
