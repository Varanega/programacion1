# Definimos ruta
ruta = 'libros.txt'
archivo = open(ruta)

# Leer primera linea
#print(archivo.readline())

#Leer desde una posicion
archivo.seek(8)
texto = archivo.read()
archivo.seek(0)
texto2 = archivo.read()
print(texto)
print(texto2)