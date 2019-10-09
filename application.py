from flask import Flask, render_template

app = Flask(__name__)

#dynamic content based on 'headline' variable
@app.route("/")
def index():
    headline = "Hello World!"
    return render_template("index.html", htmlheadline=headline)

#dinamic content for "/bye" route based on 'headline' variable
@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", htmlheadline=headline)

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
