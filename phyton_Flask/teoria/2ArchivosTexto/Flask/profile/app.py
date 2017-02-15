from flask import Flask, render_template, redirect, url_for, request
from Item import Item
from forms import NewForm

app = Flask(__name__)
# codificacion
app.secret_key = 'secret'

perfil = Item('Veronica','Aranega Ferreres','Diseñadora gráfica', 'img/1.jpg')

@app.route("/")
def index():
    #Imprimimos
    return render_template('items/index.html', perfil=perfil)

@app.route("/new")
def new():
    form = NewForm()
    return render_template('items/edit.html', form=form,  todos_errores=form.errors.items())


@app.route("/new_product", methods=['POST'])
def new_product():
    form = NewForm()
    if form.validate_on_submit():
        # Guarda la imagen
        f = request.files['imagen']
        nombre = str(int(time())) + f.filename
        nombre_con_hora = secure_filename(nombre)
        # Parche para Pycharm
        import os, sys
        base_dir = sys.path[0]
        f.save(os.path.join(base_dir, 'static/img/' + nombre_con_hora))
        # Crea el producto
        return redirect(url_for('index'))
    else:
        return render_template('items/edit.html', form=form, todos_errores=form.errors.items())

if __name__ == '__main__':
    app.debug = True
    app.run()
