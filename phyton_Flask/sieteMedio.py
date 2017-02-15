#Bibliotecas
import random

#Variables
baraja = [1, 2, 3, 4, 5, 6, 7, 0.5, 0.5, 0.5]
mano = []
play = True
LIMITE = 7.5


#Funciones
def imprimir_mano(mano):
    '''
    Imprime la mano
    :param mano:
    :return:
    '''
    final = ''
    # Recorremos la mano
    for carta in mano:
        #concadenamos con un espacio cada imo de los elementos
        final += str(carta) + ' '
    #imprimimos el resultado
    print(final)

# Para limpiar la consola
def limpiar():
    for i in range(100):
        print()
# bucle
while play:
    opcion = int(input('1) Carta 2) Plantarse: '))
    if opcion == 1:
        #Seleccionamos una carta
        pos_random = random.randint(0, len(baraja) - 1)
        carta = baraja.pop(pos_random)
        #Limpiar
        limpiar()
        #mostramos la carta
        print('Te ha salido ' + str(carta))
        #anyadimos a la mano
        mano.append(carta)
        #imprimimos la mano
        imprimir_mano(mano)
        # Comprobamos si se ha terminado el juego
        suma = 0
        for carta in mano:
            suma += carta
        print('Tienes un total de: ' + str(suma))
        if suma == LIMITE:
            print('Has ganado')
            play = False
        elif LIMITE > 7.5:
            print('Has perdido')
            play = False

    elif opcion == 2:
        play = False

print('Game over')
