print('Bienvenido a mi Calculadora')
#obtener informacion
num_1 = input('Numero 1: ')
num_2 = input('Numero 2: ')

#Obtener la información
num_total = float(num_1) + float(num_2)

#imprimir el resultado
print('La suma de {num_1} + {num_2} = {num_total}'
      .format(num_1=num_1, num_2=num_2, num_total=num_total))