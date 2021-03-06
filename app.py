from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
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
  if session and session["user_id"]:
    todos = db.execute("SELECT * FROM todos WHERE user_id = ?", session["user_id"])
    
    if not todos:
      return render_template("index.html")
    else:
      return redirect("/todos")

  return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")


@app.route("/new", methods=["GET", "POST"])
@login_required
def new():
  if request.method == "POST":
    priority = request.form.get("priority")
    title = request.form.get("title")
    description = request.form.get("description")
    user_id = session["user_id"]

    if not priority:
      return apology("Please include task priority")
    elif title == "":
      return apology("Please include task title")

    db.execute("INSERT INTO todos (user_id, priority, title, description) VALUES (?, ?, ?, ?)", user_id, priority, title, description)

    return redirect("/todos")

  else:
    return render_template("new.html")


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


@app.route("/todos")
@login_required
def todos():
  todos = db.execute("SELECT * FROM todos WHERE user_id = ? ORDER BY priority ASC", session["user_id"])

  return render_template("todos.html", todos=todos)