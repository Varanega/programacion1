# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
from random import randint
app = Flask(__name__)
bola = ('Yo que tu saldria a la calle', 'No lo dudes', 'Hoy la suerte esta de tu parte', 'No tengo la respuesta')

@app.route("/")
def index():
    return render_template('items/info.html')

@app.route("/info")
def info():
    return bola[randint(0, len(bola) - 1)]

if __name__ == "__main__":
    app.debug = True
    app.run()