from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie"]
    games =["Dota 2", "Fortnite", "Fifa 20", "Pubg"]
    return render_template("index.html", names=names, games = games)
