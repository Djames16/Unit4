from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    user_name="UnsealedThyme44"
    return render_template(
        "home.html.jinja",
        user_name=user_name
    )

@app.route('/Ping')
def Ping():
    return "<p>Pong</p>"

@app.route('/hello/<name>')
def Name(name):
    return "Hello"+name