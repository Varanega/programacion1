# Funcion sin argumentos
def imprimirHolaMundo():
    print('Hola mundo')

def imprimirHolaMundoConcreto(insPlaneta):
    print('Hola {0}'.format(insPlaneta))

def imprimirHolaMundoConcretoYSatelite(insPlaneta, insSatelite):
    print('Hola {0}, con satélite {1}'.format(insPlaneta, insSatelite))

def imprimirHolaMundoMultiples(*insPlanetas):
    print('Númeor de planetas: {0}'.format(len(insPlanetas)))
    print('Segundo planeta: {0}'.format(insPlanetas[1]))
    #Tres primeros
    sPlaneta1, sPlaneta2, sPlaneta3 = insPlanetas
    print('{0}, {1} y {2}.'.format(sPlaneta1, sPlaneta2, sPlaneta3))

imprimirHolaMundo()
imprimirHolaMundoConcreto('Marte')
imprimirHolaMundoConcretoYSatelite('Júpiter', 'Europa')
imprimirHolaMundoMultiples('Mercurio', 'Venus', 'Tierra')
