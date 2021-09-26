from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
import subprocess
import fortune
import cowsay
from contextlib import redirect_stdout
import io

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/sayHi/<name>")
def sayHi(name):
    language = request.args.get('lang','')
    return render_template('say_hi.html', name=name, language=language)

@app.errorhandler(404)
def page_not_found(e):
   phrase = fortune.get_random_fortune("/usr/share/games/fortunes/fortunes")
   return render_template('404.html', random_phrase=phrase),404
