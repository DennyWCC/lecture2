import datetime

from flask import Flask, render_template

app = Flask(__name__)

#dynamic content based on given url
#html dynamic url use case example
'''@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")
'''

#dynamic content based on 'htmlnames' variable
#html loop use case example
'''@app.route("/")
def index():
    names = ["A", "B", "3"]
    return render_template("index.html", htmlnames=names)
'''

#dynamic content based on 'new_year' variable
#html conditional use case example
'''@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", htmlnew_year=new_year)
'''

#dynamic content based on 'headline' variable
'''@app.route("/")
def index():
    headline = "Hello World!"
    return render_template("index.html", htmlheadline=headline)
'''

#dinamic content for "/bye" route based on 'headline' variable
'''@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", htmlheadline=headline)
'''

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
