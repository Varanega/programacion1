# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from Heroe import Heroe
app = Flask(__name__)

lista_heroes = [Heroe('Batman', 'El Millonario aburrido',2), Heroe('Torrente', 'El brazo especial de la ley',2), Heroe('Wonderwoman', 'Un látigo con clase',1)]

@app.route("/")
def index():
    return render_template('lista_superheroes.html', heroes=lista_heroes)

@app.route("/guardar", methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    sexo = request.form['sexo']
    lista_heroes.append(Heroe(nombre,descripcion, int(sexo)))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
