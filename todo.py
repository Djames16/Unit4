from flask import Flask, render_template, request, redirect
import pymysql
from pprint import pprint as print


app=Flask(__name__)

connect=pymysql.connect(
    database="djames_todos",
    user="djames",
    password="228118717",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

todo=["Eat cake","Workout"]


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        new_todo=request.form["new_todo"]
        todo.append(new_todo)
    cursor=connect.cursor()
    cursor.execute("SELECT `description` FROM `todos`")
    results=cursor.fetchall()
    return render_template("todo.html.jinja", my_todos=results)

@app.route('/delete_todo/<int:todo_index>',methods=['POST'])
def todo_delete(todo_index):
    del todo[todo_index]
    return redirect('/')

