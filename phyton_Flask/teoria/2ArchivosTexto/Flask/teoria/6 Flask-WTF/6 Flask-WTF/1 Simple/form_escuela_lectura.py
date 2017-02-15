from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class RegistroForm(Form):
    name = StringField('Nombre')
    age = IntegerField('Edad')
    submit = SubmitField('Registrarse')
