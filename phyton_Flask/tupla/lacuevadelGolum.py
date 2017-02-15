import random

oportunidades = 3
respuesta = random.randint(0, 10)
play = True
while play > 0:
    mensaje = int(input('Dime un número entre el 1 y el 10: '))

    if mensaje == respuesta:
        play = False
        print('Te salvaste')
    else:
        oportunidades -= 1
        print('Has fallado. Te quedan {oportunidades} oportunidades'.format(oportunidades=oportunidades))

    if oportunidades == 0:
        play = False

print('Game over')
#cambiar numero por letra