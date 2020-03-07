from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST", "GET"])
def hello():

    if request.method == "GET":
        return "Invalid submission to the webpage, please fill up forms instead"

    else:
        name = request.form.get("name")
        age = request.form.get("age")
        games = request.form.get("games")
        return render_template("hello.html", name=name, age=age, games=games)
