# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, make_response # Importamos make_response
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        resp = make_response(render_template('inicio.html', nombre=nombre))
        resp.set_cookie('nombre', nombre, 100000) # el tercer parametro es opcional. Si no se indica caducará cuando el usuario cierre la sesión o el navegador

        return resp
    else:
        if request.cookies.get('nombre'):
            return render_template('inicio.html', nombre=request.cookies.get('nombre'))
        else:
            return render_template('inicio.html')

if __name__ == "__main__":
    app.run(debug=True)
