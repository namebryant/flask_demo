# __author__ == ''
# -*- coding: utf-8 -*-


from app import app
from models import Todo
from flask import render_template,request

@app.route('/')
def index():
   todos = Todo.objects.all()

   for todo in todos:
      print todo.time

   return render_template('index.html',todos)

@app.route('/add_todo',methods=['POST'])
def add():
   form = request.form
   content = form['content']
   todo = Todo(content = content)
   todo.save()

   todos = Todo.objects.all()
   return render_template("index.html",todos)