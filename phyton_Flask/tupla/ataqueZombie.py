
armas = ('pistola', 'cuchillo', 'impuestos')

texto_armas = ', '.join(armas)

texto_inicio = 'Selecciona un arma: {armas} ---> '.format(armas=texto_armas)

opcion = input(texto_inicio).strip()

if opcion in armas:
    if opcion == armas[-1]:
        print('has ganado')
    else:
        print('Buen intento, pero muy lento')
else:
    print('no encuentras nada > Muerto')