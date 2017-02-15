# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('web/inicio.html')

@app.route("/final")
def final():
    return render_template('web/final.html')


if __name__ == "__main__":
    app.run(debug=True)
