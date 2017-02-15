#Variables
tareas = ['Comprar', 'Correr', 'Beber']
play= True

while play:
    print('\n' * 100)
    print('TO DO')
    print('-----------------------')
    for tarea in tareas:
        print('- {tarea}'.format(tarea=tarea))
    print('-----------------------')
    print('1. Nueva')
    print('2. Modificar')
    print('3. Eliminar')
    print('4. Salir')
    print('Elige la opción deseada: ')
    opcion = int(input(''))

    if opcion == 1:
        #Anyadimos
        nueva_tarea = input('Escribela: ')
        tareas.append(nueva_tarea)
        print('\u2764 Añadida \u2764')
    elif opcion == 2:
        #Modificamos
        tarea_mod = input('Dime el nuevo texto: ')
        pos_mod = int(input('Que posición: '))
        tareas[pos_mod] = tarea_mod
    elif opcion == 3:
        pos_eli = int(input('Que posición esta: '))
        tareas.pop(pos_eli)
    elif opcion == 4:
        play = False

print('Have a nice day')