# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/circo") # Cualquier cosa
def circo():
    return "<h1>Bienvenido</h1>"

@app.route("/ciudad/<nombre>") # Cualquier cosa
def ciudad(nombre):
    return f"<h1>Bienvenido a {nombre}</h1>"

@app.route("/habitantes/<int:personas>") # numeros enteros
def habitantes(personas):
    return f"<h1> En mi ciudad hay {personas} personas</h1>"

@app.route("/habitante/<float:persona>") # decimales
def habitante(persona):
    return f"<h1> En mi ciudad hay {persona} personas</h1>"

@app.route("/ruta/<path:ruta>") # Cualquier cosa
def ruta(ruta):
    return ruta
    return ruta

if __name__ == "__main__":
    app.debug = True
    app.run()