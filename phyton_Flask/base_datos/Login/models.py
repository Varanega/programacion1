from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Encriptar la contraseña
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/login'
db = SQLAlchemy(app)

class Experiencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(80))
    puesto = db.Column(db.String(100))
    anyo_inicio = db.Column(db.Integer)
    anyo_salida = db.Column(db.Integer)

    def __init__(self, empresa, puesto, anyo_inicio, anyo_salida):
        self.empresa = empresa
        self.puesto = puesto
        self.anyo_inicio = anyo_inicio
        self.anyo_salida = anyo_salida

    def __repr__(self):
        return f'<Experiencia { self.empresa }>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(32))


    def __init__(self, nombre, email, password):
        self.name = nombre
        self.email = email
        #contraseña encriptada
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()

    def __repr__(self):
        return f'<User { self.email }>'