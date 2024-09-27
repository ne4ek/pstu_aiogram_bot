from flask import Flask
from flask import render_template

app = Flask(__name__)

from views import *



if __name__ == "__main__":
    app.run(port=3333)
    
    
