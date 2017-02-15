# -*- coding: utf-8 -*-
from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return f'''
    <form method="GET" action="{url_for('finalizar_comprar')}">
        <input type="text" name="reloj">
        <input type="submit" value="comprar">
    </form>
    '''
@app.route("/thx")
def finalizar_compra():
    nombre_reloj = ''
    if request.args.get('reloj'):
        nombre_reloj = request.args.get('reloj')
    return f'Gracias por comprar un {nombre_reloj}'

if __name__ == "__main__":
    app.debug = True
    app.run()