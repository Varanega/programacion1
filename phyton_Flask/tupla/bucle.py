'''armas = ('pistola', 'cuchillo', 'impuestos')

for item in armas:
    print('En mi bolsillo tengo un ' + item)

for i in range(4):
    print(i)

for i in range(4, 9):
    print(i)

for i in range(0, 100, 7):
    print(i)
'''
num = 0
for i in range(0, 201, 2):
    texto = '2 x {numeral} = {resultado}'.format(numeral=num, resultado=i)
    num += 1
    print(texto)

planetas = ('Mercurio', 'Venus', 'Tierra')
for key, value in enumerate(planetas):
    print(value + ' esta en la pos ' + str(key))
    
lNum = []
i = 0
while i < 100:
    lNum.append(i)
    i += 1

print(lNum)