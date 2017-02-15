# -*- coding: utf-8 -*-
from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method != 'POST':
        return '''
        <h1>Login</h1>
        <form method="post" action="{0}">
            <input type="email" name="email"><br>
            <input type="password" name="contrasenya">
        </form>
        '''.format(url_for('login'))
    else:
        return '<h1>Registrado con el email <strong>{0}</strong> y la contrase&ntilde;a <strong>{1}</strong>.'.format(request.form['email'], request.form['contrasenya']) 

if __name__ == "__main__":
    app.run(debug=True)
