from flask import Flask, render_template, redirect, url_for, request
from Item import Item
from forms import NewForm
from werkzeug import  secure_filename
from time import time

app = Flask(__name__)
# codificacion
app.secret_key = 'secret'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])

list_items = [Item(1, 'Pegatina', 4, 'Es una cosa chula', 'img/pegatina.jpg'),
              Item(2, 'Chocolate', 2, 'Dulce rico', 'img/chocolate.jpg'),
              Item(3, 'Reloj', 10, 'Es un objeto muy bonito', 'img/reloj.jpg'),
              Item(4, 'Tentaculo', 4, 'Alimento del mar', 'img/tentaculo.jpg')]
carrito = []

@app.route("/")
def index():
    total = 0
    # Calculamos el precio final
    for producto in carrito:
        for item in list_items:
            if producto == item.id:
                total += item.precio
    #Imprimimos
    return render_template('items/tienda.html', items=list_items, carrito=carrito, total=total)


@app.route("/add/<int:id>")
def add(id):
    carrito.append(id)
    return redirect(url_for('index'))


@app.route("/new")
def new():
    form = NewForm()
    return render_template('items/new.html', form=form,  todos_errores=form.errors.items())


@app.route("/new_product", methods=['POST'])
def new_product():
    form = NewForm()
    if form.validate_on_submit():
        # Genera la id
        id_end = list_items[-1]
        id_end = int(id_end.id) + 1
        # Guarda la imagen
        f = request.files['imagen']
        nombre = str(int(time())) + f.filename
        nombre_con_hora = secure_filename(nombre)
        # Parche para Pycharm
        import os, sys
        base_dir = sys.path[0]
        f.save(os.path.join(base_dir, 'static/img/' + nombre_con_hora))
        # Crea el producto
        list_items.append(Item(id_end, request.form['nombre'], float(request.form['precio']),
                               request.form['descripcion'],'img/' + nombre_con_hora))
        return redirect(url_for('index'))
    else:
        return render_template('items/new.html', form=form, todos_errores=form.errors.items())


if __name__ == '__main__':
    app.debug = True
    app.run()