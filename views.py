from flask import render_template
from main import app
from util import *
@app.route("/")
def loading():
    return render_template("loading.html")


@app.route("/menu")
def menu():
    context = {'menu_items':get_all_menu_items(), 'menu_socials':get_all_social_for_menu()}
    return render_template("menu.html", menu_items=get_all_menu_items(), menu_socials=get_all_social_for_menu())



@app.route("/menu/naprvlenia")
def napravlenia():
    
    return render_template("menu-pages/napravlenia.html")

@app.route("/menu/stoimost")
def stoimost():
    images_links = get_all_image_stoimost()
    return render_template("menu-pages/stoimost.html", image_names=get_all_image_stoimost())

@app.route("/menu/obshejitie")
def obshejitie():
    return render_template("menu-pages/obshejitie.html", image_names=get_all_image_obshejitie())

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