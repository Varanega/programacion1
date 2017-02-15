# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "<h1>Recibo cosas</h1>"
    else:
        return "<h1>No me das ni un triste dato<form method='post'><input type='submit' name='boton'></form></h1>"

if __name__ == "__main__":
    app.run(debug=True)
