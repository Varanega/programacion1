print('Calculadora de IVA')

#obtener informacion
num_1 = input('Cifra a calcular ')
num_2 = 0.21

#Obtener la información
num_total = float(num_1) * float(num_2) + float(num_1)

#imprimir el resultado
print(num_total)

#Pro
num_1 = input('Cifra a calcular ')
num_2 = 0.21
num_total = float(num_1) * float(num_2) + float(num_1)
print('Tu producto sin iva {num_1}€ y con iva {num_total}€'.format(num_1=num_1, num_total=num_total))