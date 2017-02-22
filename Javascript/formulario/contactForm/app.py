from flask import Flask, render_template, request
from flask_mail import Mail, Message
import configparser
app = Flask(__name__)

config = configparser.ConfigParser()
config.read('.env')
app.config['SECRET_KEY'] = config['DEFAULT']['SECRET_KEY']
app.config['MAIL_SERVER'] = config['DEFAULT']['EMAIL_HOST']
app.config['MAIL_PORT'] = config['DEFAULT']['EMAIL_PORT']
app.config['MAIL_USE_SSL'] = config['DEFAULT']['EMAIL_SSL']
app.config['MAIL_USERNAME'] = config['DEFAULT']['EMAIL_USER']
app.config['MAIL_PASSWORD'] = config['DEFAULT']['EMAIL_PASSWORD']

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['name']
        edad = request.form['edad']
        email = request.form['email']
        mensaje = request.form['mensaje']

        msg = Message("Nuevo mensaje de web",
                      sender="varanegadesign@gmail.com",
                      recipients=["varanegadesign@gmail.com"])
        msg.body = render_template('mailing/mailing.txt', nombre=nombre, edad=edad, email=email, mensaje=mensaje)
        msg.html = render_template('mailing/mailing.html', nombre=nombre, edad=edad, email=email, mensaje=mensaje)
        mail.send(msg)
    return render_template('contactForm.html')

if __name__ == '__main__':
    app.debug = True
    app.run()