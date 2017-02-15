from datetime import datetime

#Mensaje bienvenida
print('''
    RobotPortero 2.0v
''')
'''anyo_nacimiento = int(input('Dime tu año de nacimiento: '))
EDAD_LIMITE = 18
anyo_actual = datetime.now().year
if (anyo_actual - anyo_nacimiento) >= EDAD_LIMITE:
    print('Puedes pasar')
else:
    print('Vete niño')'''

# Pro
anyo_nacimiento = int(input('Dime tu año de nacimiento: '))
mes_nacimiento = int(input('Dime tu mes de nacimiento: '))
dia_nacimiento = int(input('Dime tu dia de nacimiento: '))
EDAD_LIMITE = 18
anyo_actual = datetime.now().year
mes_actual = datetime.now().month
dia_actual = datetime.now().day
if (anyo_actual - anyo_nacimiento) > EDAD_LIMITE:
    print('Puedes pasar')
else:
    if (anyo_actual - anyo_nacimiento) == EDAD_LIMITE:
        if mes_nacimiento < mes_actual:
            print('Puedes pasar')
        else:
            if mes_nacimiento == mes_actual and dia_nacimiento <= dia_actual:
                print('Puedes pasar')
            else:
                print('Vete ya')
    else:
        print('vete ya')