# Definimos ruta
ruta = 'ejercicio1.txt'
contenido = open(ruta).read()
# Abrimos archivos
archivo = open(ruta,'a')
# Pedir al usuario el nuevo texto
nuevo_texto = input('Dime tu tarea: ') + '\n'
# Escribimos el contenido
archivo.write(contenido + '\n' + nuevo_texto)
# Libreamos el archivo
archivo.close()
#informamos
print(contenido + nuevo_texto)