#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

nombre = input ('Ingrese nombre: ')
apellido = input ('Ingrese apellido: ')
edad = int (input ('Ingrese edad: '))
if (0 <= edad <= 2):
    print ('bebe')
elif (2 < edad <= 9):
    print ('nino')
elif (9 < edad <= 12):
    print ('pre-adolescente')
elif (12 < edad <=19):
    print ('adolescente')
elif (19 < edad <= 35):
    print ('adulto joven')
elif (35 < edad <= 59):
    print ('adulto')
else:
    print ('adulto mayor')