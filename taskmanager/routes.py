from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task  # to import from models


@app.route("/")
def home():
    return render_template("base.html")
