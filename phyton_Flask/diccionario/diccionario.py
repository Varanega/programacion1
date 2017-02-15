alumnos = {
    'Marco': 6,
    'Chris': 4,
    'Estrella': 10,
    'Vero': 9.5,
    'Sara': 9.4,
    'Marc': 2.1,
}
play = True

while play:
    print('+-------+--------+')
    print('+Alumno   +Nota  +')
    for alumno, nota in alumnos.items():
        print('+-------+--------+')
        print(f' |{alumno} | {nota} |')
    print('+-------+--------+')
    opcion = input('1. Modificar \n'
                   '2. Nuevo \n'
                   '3. Borrar \n'
                   '4. Salir \n')
    if opcion == '1':
        alumno_mod = input('Nombre: ')
        if alumno_mod in alumnos:
            nota_mod = input('Nota: ')
            alumnos[alumno_mod] = float(nota_mod)
        else:
            print('No existe')
    elif opcion == '2':
        alumno_nuevo = input('Nomnre: ')
        alumno_nuevo_nota = input('Nota: ')
        alumnos[alumno_nuevo] = float(alumno_nuevo_nota)
    elif opcion == '3':
        alumno_bor = input('Nombre: ')
        del(alumnos[alumno_bor])
    elif opcion == '4':
        play = False
        print('Bye')
