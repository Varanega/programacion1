
# Del 1 al 10
for i in range(10):
    print(i + 1)

# Del 60 al 70
for i in range(60, 71):
    print(i)

# Del 20 al 1
for i in range(20, 0, -1):
    print(i)
# Del 1 al 1000
for i in range(1, 1001):
    print(i)
# La tabla del 5
numeral = 0
for i in range(0, 51, 5):
    print('5 x {numeral} = {resultado}'.format(numeral=numeral, resultado=i))
    numeral += 1