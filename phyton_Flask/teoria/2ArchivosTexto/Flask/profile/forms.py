from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, FileField
from wtforms.validators import InputRequired, Length, NumberRange

class NewForm(Form):
   nombre = StringField('Name', validators=[InputRequired('Obligatorio')])
   apellido = StringField('Surname', validators=[InputRequired('Obligatorio')])
   titulo = StringField('Title', validators=[InputRequired('Obligatorio')])
   descripcion = TextAreaField('Personal Profile')
   educacion = TextAreaField('Education')
   idiomas = TextAreaField('Languages')
   experiencia = TextAreaField('Work Experience')
   skills = TextAreaField('Skills')
   contacto = TextAreaField('Contact')
   image = FileField( validators=[InputRequired('Una imagen por favor')])
   submit = SubmitField('Enviar')