from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, FileField
from wtforms.validators import InputRequired, Length, NumberRange
class NewForm(Form):
   nombre = StringField('Nombre', validators=[InputRequired('Obligatorio')])
   precio = IntegerField('Precio', validators=[InputRequired('Obligatorio'), NumberRange(1, 10000, 'Debe ser entre 1 y 10000')])
   descripcion = TextAreaField('Descripción',validators=[InputRequired('Necesitamos una descripción')])
   imagen = FileField('Imagen', validators=[InputRequired('Una imagen por favor')])
   submit = SubmitField('Enviar')