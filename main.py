from flask import Flask, render_template
import os
from pathlib import Path


app = Flask(__name__)

@app.route("/")
def loading():
    return render_template("loading.html")


def get_file_names_for_menu():
    cwd = os.getcwd()
    directory = '/static/img/menu'
    full_path = Path(cwd + directory)
    grid_items = [file.name for file in full_path.iterdir() if file.is_file()]
    print(cwd, full_path)
    return grid_items

@app.route("/menu")
def menu():
    return render_template("menu.html", grid_items=get_file_names_for_menu())

if __name__ == "__main__":
    app.run(port=3333)
    
    
