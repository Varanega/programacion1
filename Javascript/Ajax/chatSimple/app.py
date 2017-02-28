# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

mensajes = 'texto cualquiera<br>funciona'

@app.route("/")
def index():
    return render_template('items/chat.html')

@app.route("/mensajes")
def get():

    return mensajes

@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        mensajes += request.form['mensaje_nuevo'] + mensajes
    return 'ok'

if __name__ == "__main__":
    app.debug = True
    app.run()