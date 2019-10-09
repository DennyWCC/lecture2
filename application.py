from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#print Hello World in webpage
'''@app.route("/")
def index():
    return "Hello World!"
'''

#dynamic function
'''@app.route("/<string:name>")
def hello(name):
    name = name.capitalize() #capitalize first letter
    return f"Hello {name}!"
'''
