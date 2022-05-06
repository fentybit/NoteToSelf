import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required
from datetime import datetime, timezone

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

@app.route("/login", methods={"GET", "POST"})
def login():
  session.clear()

  if request.method == "POST":
    if not request.form.get("username"):
      return apology("User must provide password")
    elif not request.form.get("password"):
      return apology("User must provide password")

    rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
      return apology("Invalid username and/or password")

    session["user_id"] = rows[0]["id"]

    return redirect("/")
  
  else:
    return render_template("login.html")
    

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    if username == "" or len(db.execute("SELECT username FROM users WHERE username = ?", username)) > 0:
      return apology("Invalid Username: Blank, or already exists")
    if password == "" or password != confirmation:
      return apology("Invalid Password: Blank, or does not match")

    db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

    rows = db.execute("SELECT * FROM users WHERE username = ?", username)

    session["user_id"] = rows[0]["id"]

    return redirect("/")

  else:
    return render_template("register.html")