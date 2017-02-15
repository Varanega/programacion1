from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email

class ExperienciaForm(Form):
    empresa = StringField('Empresa', validators=[InputRequired('Debe introducir una empresa'),
                                                  Length(1, 80, 'El nombre es demasiado largo')])
    puesto = StringField('Puesto', validators = [InputRequired('Debe introducir un cargo'),
                  Length(1, 100, 'El nombre es demasiado largo')])
    anyo_inicio =  IntegerField('Año de inicio', validators = [InputRequired('Debe introducir el año de inicio'),
                                                               NumberRange(1900, 2017,  'El número debe tener 4 digitos')])
    anyo_salida = IntegerField('Año de finalización', validators=[InputRequired('Debe introducir el año de finalización'),
                                                                  NumberRange(1900, 2017, 'El número debe tener 4 digitos')])
    submit = SubmitField('Añadir')

class UserForm(Form):
    name = StringField('Nombre', validators=[InputRequired('Debe introducir un nombre'),
                                                  Length(1, 100, 'El nombre es demasiado largo')])
    email = StringField('E-mail', validators = [InputRequired('Debe introducir un e-mail'),
                  Length(1, 100, 'El e-mail es demasiado largo'), Email('Tu e-mail no tiene una estructura correcta')])
    password =  PasswordField('Contraseña', validators = [InputRequired('Necesitas indicar tu contraseña')])
    password2 = PasswordField('Contraseña', validators=[InputRequired('Repita contraseña')])
    submit = SubmitField('Entrar')

