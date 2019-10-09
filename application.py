from flask import Flask

app = Flask(__name__)

#print Hello World in webpage
'''@app.route("/")
def index():
    return "Hello World!"
'''

#dynamic function
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello {name}!"
