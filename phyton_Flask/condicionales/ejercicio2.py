'''nombre = input('¿Cual es tu nombre? ')
genero = input('¿Cual es tu genero? ')
num_hijos = int(input('¿Cuantos hijos tienes? '))
if genero == 'mujer' and num_hijos > 0:
    print('La señora {nombre} tiene {num_hijos} hijos'.format(nombre=nombre, num_hijos=num_hijos))
else:
    if genero == 'mujer' and num_hijos <= 0:
        print('La señora {nombre} no tiene hijos'.format(nombre=nombre,))
    else:
        if genero == 'hombre' and num_hijos > 0:
            print('El señor {nombre} tiene {num_hijos} hijos'.format(nombre=nombre, num_hijos=num_hijos))
        else:
            print('El señor {nombre} no tiene hijos'.format(nombre=nombre))
'''
#Version 2

nombre = input('Tu nombre: ')
sexo = input('Tu sexo: ')
hijos = int(input('Tus hijos: '))

texto_final = ''

#Genero
if sexo == 'hombre':
    texto_final += 'El señor '
elif sexo == 'mujer':
    texto_final += 'La señora'

#Nombre
texto_final = texto_final + nombre

#hijos
if hijos == 0:
    texto_final += ' no tiene hijos'
else:
    texto_final += ' tiene ' + str(hijos) + ' hijos '

print(texto_final)
