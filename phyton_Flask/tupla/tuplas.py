''''# Tuplas
planetas = ('Mercurio', 'Venus', 'Tierra')
gravedad = (4, 1, 6, 2)
gravedad_tierra = (9,)

#listas
planetas_lista= list(planetas)

planetas_lista.append('Marte')
planetas_lista.append('Jupiter')

# De un punto al final
print(planetas_lista[1:4])
'''
planetas = ['Mercurio', 'Venus', 'Tierra', 'Venus']
animal = 'perro pajaro delfin'
animal_lista = animal.split('o')
print(planetas.count('Venus'))

planetas.insert(3, 'Saturno')

planetas.remove('Venus')

print(planetas)
fuera = planetas.pop(0)
print(fuera)
print(planetas)
planetas.reverse()
print(planetas)
print(animal_lista)
print(animal[3])
print(' '.join(planetas))