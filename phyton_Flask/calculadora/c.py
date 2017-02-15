print('Bienvenidos a la Calculadora 2.0v')
#Variables
play = True

while play:
    print('Primer número: ')
    num_1 = int(input(''))
    print('Seleccione unos de estos operadores: + - x / %')
    operador = str(input(''))
    if operador == '%':
        print('Introduzca el porcentaje a calcular')
    else:
        print('Segundo número: ')
    num_2 = int(input())
    if operador == '+':
        resultado = num_1 + num_2
        print('El resultado es: ', resultado)
    elif operador == '-':
        resultado = num_1 - num_2
        print('El resultado es: ', resultado)
    elif operador == 'x':
        resultado = num_1 * num_2
        print('El resultado es: ', resultado)
    elif operador == '/':
        resultado = num_1 / num_2
        print('El resultado es: ', resultado)
    elif operador == '%':
        resultado = (num_1 * num_2)/100
        resultado_2 = resultado + num_1
        print('El porcentaje es: ', resultado)
        print('Y el total sumado es: ', resultado_2)
    print('¿Quieres salir? Y/N')
    salir = str(input())
    if salir == 'Y' or salir == 'y':
        play = False
        print('Gracias por confiar en nosotros')
    else:
        print('\n' * 100)