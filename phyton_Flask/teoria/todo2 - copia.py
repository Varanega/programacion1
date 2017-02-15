 -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    class Tarea(object):
        def __init__(self, texto, prioridad):
            self.texto = texto
            self.prioridad = prioridad
            self.equivalencias = ('Alta', 'Media', 'Baja')

        def texto_prioridad(self):
            return self.equivalencias[self.prioridad - 1]

    list_tareas = [Tarea('fregar', 3), Tarea('pagar recibo', 1)]

    #Imprimimos
    html = ''
    for item in list_tareas:
        if item.prioridad == 1:
            print(f'"{item.texto}"({item.texto_prioridad()})')
    for item in list_tareas:
        if item.prioridad == 2:
            print(f'"{item.texto}"({item.texto_prioridad()})')
    for item in list_tareas:
        if item.prioridad == 3:
            print(f'"{item.texto}"({item.texto_prioridad()})')

if __name__ == "__main__":
    app.debug = True
    app.run()
