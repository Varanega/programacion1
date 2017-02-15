def imprimir_nombre():
    '''
    Funcion que imprime un nombre
    '''
    print('Soy una funcion')

# ejecuta nuestri codigo
imprimir_nombre()

def poner_mayusculas(texto):
    print(texto.upper())

poner_mayusculas('me gusta conducir')
poner_mayusculas('volar')

def poner_muchas_mayusculas(texto, texto2):
    print(texto.upper() + texto2)

poner_muchas_mayusculas('solarium ', 'playa')
poner_muchas_mayusculas('gato ', 'perro')

def multiple(*texto):
    print(len (texto))
    print(texto[1])

multiple('rato', 'largo', 'avion')

def sumar(num1, num2):
    print(num1 + num2)