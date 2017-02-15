# -*- coding: utf-8 -*-
from flask import Flask, render_template, render_template
from form_escuela_lectura import RegistroForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/")
def index():
    form = RegistroForm()
    return render_template('formulario.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
