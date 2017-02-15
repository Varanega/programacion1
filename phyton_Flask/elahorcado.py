import random
# Ahorcado v1.0

list_palabras = ['habitacion', 'telesilla', 'avion', 'enano', 'circo']
intentos = 5
solucion_palabra = list_palabras[random.randint(0, len(list_palabras) - 1)]
list_solucion = []
play = True
for pos in range(len(solucion_palabra)):
    list_solucion.append('_')


while play:
    print('\n' * 100)
    print(' '.join(list_solucion))
    print(f'Tienes {intentos} intentos')

    letra = input('Letra: ')

    #Comprobamos cuantas letras ha dado el jugador
    if len(letra) >1:
        print('Solo puedes introducir una letra a la vez')
    else:
        #Verificamos si la palabra esta
        if letra in solucion_palabra:
            # Ha acertado
            for index, letra_solucion in enumerate(solucion_palabra):
                if letra == letra_solucion:
                    list_solucion[index] = letra
        else:
            # Ha fallado
            intentos -= 1
    #Comprobamos si ha terminado el juego
    if intentos == 0:
        play = False
        print('\n' * 100)
        print('Has perdido')
    elif ''.join(list_solucion) == ''.join(solucion_palabra):
        play = False
        print('\n' * 100)
        print('Has ganado')

print(f'La solucion es: {"".join(solucion_palabra)}')
