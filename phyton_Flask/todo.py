
# TO Do terminal v1.0

#Objetos
class Important(object):

    def __init__(self, text):
        self.text = text

# Variables
play = True
list_very_important = [Important('Comprar comida'), Important('Entregar trabajo')]
list_important = [Important('Sacar al perro')]
list_less_important = [Important('Regar las plantas')]

while play:

    print('-----To do-----')
    print('-----------------')
    print('Very important')
    for pos, tarea in enumerate(list_very_important):
        print(f'{pos} "{tarea.text}"\n')
    print('-----------------')
    print('Important')
    for pos, tarea2 in enumerate(list_important):
        print(f'{pos} "{tarea2.text}"\n')
    print('-----------------')
    print('Less important')
    for pos, tarea3 in enumerate(list_less_important):
        print(f'{pos} "{tarea3.text}"\n')
    print('1. Nuevo')
    print('2. Modificar')
    print('3. Eliminar')
    print('4. Salir')
    opcion = input()

    #Anayadir tarea
    if opcion == '1':
        print('Tarea: ')
        tarea_nueva = input()
        print('1. Muy importante')
        print('2. Importante')
        print('3. No importante')
        important_op = input()
        if important_op == '1':
            list_very_important.append(Important(tarea_nueva))
            print('Añadida')
        elif important_op == '2':
            list_important.append(Important(tarea_nueva))
            print('Añadida')
        elif important_op == '3':
            list_less_important.append(Important(tarea_nueva))
    #Modificar Tarea
    elif opcion == '2':
        print('1. Muy importante')
        print('2. Importante')
        print('3. No importante')
        important_op = input()
        if important_op == '1':
            tarea_mod = input('Dime el nuevo texto: ')
            pos_mod = int(input('Que posición: '))
            object = list_very_important.pop(pos_mod)
            object.text = tarea_mod
            list_very_important.insert(pos_mod,object)
        elif important_op == '1':
            tarea_mod = input('Dime el nuevo texto: ')
            pos_mod = int(input('Que posición: '))
            object = list_important.pop(pos_mod)
            object.text = tarea_mod
            list_important.insert(pos_mod,object)
        elif important_op == '1':
            tarea_mod = input('Dime el nuevo texto: ')
            pos_mod = int(input('Que posición: '))
            object = list_less_important.pop(pos_mod)
            object.text = tarea_mod
            list_less_important.insert(pos_mod,object)
    #Eliminar
    elif opcion == '3':
        print('1. Muy importante')
        print('2. Importante')
        print('3. No importante')
        important_op = input()
        if important_op == '1':
            pos_mod = int(input('Que posición: '))
            list_very_important.pop(pos_mod)
        elif important_op == '2':
            pos_mod = int(input('Que posición: '))
            list_important.pop(pos_mod)
        elif important_op == '3':
            pos_mod = int(input('Que posición: '))
            list_less_important.pop(pos_mod)
    #Salir
    elif opcion == '4':
        play = False
        print('Have a nice day')