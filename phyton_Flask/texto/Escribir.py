# Definimos ruta
ruta = 'libros.txt'
#leer contenido
contenido = open(ruta).read()
# Abrimos archivos
archivo = open(ruta,'w')
# Pedir al usuario el nuevo texto
nuevo_texto = input('Dime tu libro favorito: ')
# Escribimos el contenido
archivo.write(contenido + '/n' + nuevo_texto)
# Libreamos el archivo
archivo.close()
#informamos
print('Todo bien :)')