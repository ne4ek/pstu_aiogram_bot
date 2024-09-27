from flask import render_template
from main import app

@app.route("/")
def loading():
    return render_template("loading.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")



@app.route("/menu/naprvlenia")
def napravlenia():
    return render_template("napravlenia.html")

@app.route("/menu/stoimost")
def stoimost():
    return render_template("stoimost.html")

@app.route("/menu/obshejitie")
def obshejitie():
    return render_template("obshejitie.html")

@app.route("/menu/contacti")
def contacti():
    return render_template("contacti.html")

@app.route("/menu/anketi")
def anketi():
    return render_template("anketi.html")

@app.route("/menu/eksameni")
def eksameni():
    return render_template("eksameni.html")

@app.route("/menu/postuplenie")
def postuplenie():
    return render_template("postuplenie.html")

@app.route("/menu/ligoti")
def ligoti():
    return render_template("ligoti.html")

@app.route("/menu/o_vuse")
def o_vuse():
    return render_template("o_vuse.html")