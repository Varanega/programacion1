# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('inicio.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['nombre'] = request.form['nombre']
        return redirect(url_for('perfil'))
    else:
        return render_template('login.html')

@app.route("/perfil")
def perfil():
    if 'nombre' in session:
        return render_template('perfil.html', nombre=session['nombre'])
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('nombre', None)
    return redirect(url_for('index'))

app.secret_key = '\xcb\xdd2\xaf\xee\xb1\xdb\x86+\xd3Oe\x15\x0e\xf2\xd8\x03\x8b\xdc\x93<\x95\xcat'
# import os
# os.urandom(24)

if __name__ == "__main__":
    app.run(debug=True)
