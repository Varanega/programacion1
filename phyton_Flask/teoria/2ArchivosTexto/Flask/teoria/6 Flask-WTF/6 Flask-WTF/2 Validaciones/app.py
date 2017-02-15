# -*- coding: utf-8 -*-
from flask import Flask, render_template, render_template, request
from form_escuela_lectura import RegistroForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Flask-WTF'

@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegistroForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return 'Todo ha ido bien'
        else:
            return 'Algo estaba mal'
    else:
        return render_template('formulario.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
