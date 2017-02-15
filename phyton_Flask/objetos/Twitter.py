
# Twitter terminal v1.0

class Tweet(object):

    def __init__(self, text):
        self.like = 0
        self.text = text

    def aumentar_like(self):
        self.like += 1

LIMIT = 140
list_tweets = [Tweet('me encanta'), Tweet('me voy')]
play = True
error = False
mensaje_error = ''
buscar = False
buscar_palabra = ''

while play:
    print('\n' * 100)
    print('-----TWITTER-----')
    print('-----------------')
    for pos, tweet in enumerate(list_tweets):
        if (buscar and tweet.text.find(buscar_palabra) >= 0) or not buscar:
            print(f'\u2605{tweet.like}\n'
                  f'{pos} "{tweet.text}"\n'
                  f'-----------------')
    print('1. Nuevo')
    print('2. Like')
    print('3. Buscar')
    print('4. Salir')
    if error:
        print(mensaje_error)
        error = False
    opcion = input()
    if opcion == '1':
        texto = input('Mensaje: ')
        if len(texto) <= LIMIT:
            list_tweets.append(Tweet(texto))
        else:
            mensaje_error = f'No puede añadir más de {LIMIT} carácteres'
            error = True
    elif opcion == '2':
        pos_like = int(input('Posicion: '))
        list_tweets[pos_like].aumentar_like()
    elif opcion == '3':
        buscar_palabra = input('Buscar: ')
        buscar = True
    elif opcion == '4':
        play = False

