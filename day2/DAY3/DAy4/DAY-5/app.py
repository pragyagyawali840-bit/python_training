#import flask
from flask import Flask, render_template, request

#initiate flask
app = Flask( __name__)

#define routes
@app.route('/')
def home():
    return"Web development in python updated 123"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello ,{name}!"

@app.route("/add/<int:a>/<int:b>")
def add (a,b):
    return f"{a}+{b} = {a + b}"

@app.route("/sub/<int:a>/<int:b>")
def sub (a,b):
    return f"{a}-{b} = {a - b}"

@app.route("/template")
def template():
    return render_template("index.html", 
    name = "Hello cosmos")

@app.route("/submit", methods=["GET" ,"POST"])
def submit():
    if request.method =="POST":
        name = request.form["name"]
        return f"Hello , {name}!"
    return render_template("form.html")

@app.route("/newtemplate")
def newtemplate():
    return render_template("page.html")

@app.route('/page-form', methods =['GET',
'POST'])
def page_form():
    if request.method =="POST":
        name=request.form['name']
        return f"Name:{name}"
    return render_template("page-form.html")

# run the app
if __name__=="__main__":
    app.run(debug=True)