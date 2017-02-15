from sys import argv

script, rutaTXT = argv

archivoTXT = open(rutaTXT)

def leerTodo(inFile):
    """Imprime todo el texto del archivo
    
    Keyword arguments:
    inFile -- Archivo
    """
    print (inFile.read())

def cambiarPosicion(inFile, iniPos = 0):
    """Cambia la posición del cursor en el archivo
    
    Keyword arguments:
    inFile -- Archivo
    iniPos -- Posición del caracter (default 0)
    """
    inFile.seek(iniPos)

def leerLinea(inFile):
    """Devuelve una línea
    
    Keyword arguments:
    inFile -- Archivo
    """
    return inFile.readline()

sLinea = leerLinea(archivoTXT)
print(sLinea)
sLinea = leerLinea(archivoTXT)
print(sLinea)
cambiarPosicion(archivoTXT)
sLinea = leerLinea(archivoTXT)
print(sLinea)
