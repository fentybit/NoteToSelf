from cs50 import SQL
from flask import Flask, render_template
from flask_session import Session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///notetoself.db")

@app.route("/")
def index():
  return render_template("index.html")