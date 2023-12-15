from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/chapter1")
def firstChapter():
    return render_template("chapter1.html")
