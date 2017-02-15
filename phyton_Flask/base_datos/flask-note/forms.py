from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length

class NewForm(Form):
    title = StringField('Titulo', validators=[InputRequired('Debe introducir un título'), Length(1, 100, 'Su título es demasiado largo')])
    note = TextAreaField('Nota', validators=[InputRequired('No puede hacer una nota vacía')])
    submit = SubmitField('Crear')


class EditForm(Form):
    title = StringField('Titulo', validators=[InputRequired('Debe introducir un título'), Length(1, 100, 'Su título es demasiado largo')])
    note = TextAreaField('Nota', validators=[InputRequired('No puede hacer una nota vacía')])
    submit = SubmitField('Editar')