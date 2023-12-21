from flask import Flask, render_template, request

app=Flask(__name__)

todo=["Eat cake","Workout"]


@app.route('/',methods=['Get','Post'])
def index():
    new_todo=request.form["new_todo"]
    todo.append(new_todo)
    return render_template("todo.html.jinja", my_todos=todo)