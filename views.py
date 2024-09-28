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
    return render_template("menu-pages/napravlenia.html")

@app.route("/menu/stoimost")
def stoimost():
    return render_template("menu-pages/stoimost.html")

@app.route("/menu/obshejitie")
def obshejitie():
    return render_template("menu-pages/obshejitie.html")

@app.route("/menu/contacti")
def contacti():
    return render_template("menu-pages/contacti.html")

@app.route("/menu/anketi")
def anketi():
    return render_template("menu-pages/anketi.html")

@app.route("/menu/eksameni")
def eksameni():
    return render_template("menu-pages/eksameni.html")

@app.route("/menu/postuplenie")
def postuplenie():
    return render_template("menu-pages/postuplenie.html")

@app.route("/menu/ligoti")
def ligoti():
    return render_template("menu-pages/ligoti.html")

@app.route("/menu/o_vuse")
def o_vuse():
    return render_template("menu-pages/o_vuse.html")