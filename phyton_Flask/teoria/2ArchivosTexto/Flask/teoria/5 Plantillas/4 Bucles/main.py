# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    generos = ('terror', 'drama', 'comedia', 'documental')
    return render_template('inicio.html', generos=generos)

@app.route("/diccionario")
def diccionario():
    generos = {0: 'romantica', 1: 'ciencia ficción'}
    return render_template('diccionario.html', generos=generos)


if __name__ == "__main__":
    app.run(debug=True)
