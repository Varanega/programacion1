from flask import Flask, render_template, flash, url_for, redirect, request, session
from models import db, Experiencia, User
from forms import ExperienciaForm, UserForm
from functools import wraps
import hashlib

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


#Decorador - Para aplicar en varias app
def login_required(f):
    # Decoration: check login in session
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/dashboard")
@login_required
def index():
    if 'email' in session:
        my_experiencia = Experiencia.query.order_by(Experiencia.anyo_salida.desc())
        return render_template('items/login.html', experiencia=my_experiencia)
    else:
        return redirect(url_for('login'))


@app.route("/experiencia/<int:id>")
@login_required
def borrar_experiencia(id):
    my_experiencia = Experiencia.query.filter_by(id=id).first()
    db.session.delete(my_experiencia)
    try:
        db.session.commit()
        flash('Experiencia borrada', 'success')
    except:
        db.session.rollback()
        flash('Ha ocurrido un error', 'danger')
    return redirect(url_for('index'))

@app.route("/new", methods=['GET','POST'])
@login_required
def add():
    form = ExperienciaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Guardamos en la base de datos
            flash('Guardado bien', 'success')
            my_experiencia = Experiencia(request.form['empresa'], request.form['puesto'], request.form['anyo_inicio'],
                                         request.form['anyo_salida'])
            db.session.add(my_experiencia)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            #Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/new.html', form=form, )

@app.route("/", methods=['GET','POST'])
def login():
    form = UserForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            session['email'] = email
            return redirect(url_for('index'))
        else:
            flash('Su email o su password no es correcto', 'danger')
    return render_template('items/register.html', form=form)

@app.route("/signup", methods=['GET','POST'])
def signup():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Guardamos en la base de datos
            if request.form['password'] == request.form['password2']:
                flash('Creado usuario correctamente ', 'success')
                my_user = User(request.form['name'], request.form['email'], request.form['password'])
                db.session.add(my_user)
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                return redirect(url_for('login'))
            else:
                flash('Las contraseñas no coinciden', 'danger')
        else:
            #Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/signup.html', form=form, )

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()