print('Buscador de parejas v.2.0')

nombre_1 = input('Como te llamas? ')
nombre_2 = input('Nombre de la persona que te gusta ')

print('A {nombre_1} le gusta {nombre_2}'.format(nombre_1=nombre_1, nombre_2=nombre_2))

#Pro
nombre_3 = input('Como te llamas? ')
fecha = input('Fecha de nacimiento')
total = 2017 - int(fecha)
print('Me llamo {nombre_3} y nací el {fecha} por tanto tengo {total}' .format(nombre_3=nombre_3, fecha=fecha, total=total))