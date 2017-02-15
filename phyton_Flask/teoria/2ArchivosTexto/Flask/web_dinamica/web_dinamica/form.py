from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField

class ContactForm(Form):
    name = StringField('Tu nombre')
    email = StringField('Tu email')
    phone = IntegerField('Tu teléfono')
    message = TextAreaField('Mensaje')
    submit = SubmitField('Registrarse')