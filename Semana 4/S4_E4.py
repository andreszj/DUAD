#Cree un programa que le pida tres números al usuario y muestre el mayor.

numero_uno = int (input ('Ingrese numero 1: '))
numero_dos = int (input ('Ingrese numero 2: '))
numero_tres = int (input ('Ingrese numero 3: '))
if (numero_uno >= numero_dos and numero_uno >= numero_tres):
    print (f'El numero mayor es {numero_uno}')
elif (numero_dos >= numero_uno and numero_dos >= numero_tres):
    print (f'El numero mayor es {numero_dos}')
else:
    print (f'El numero mayor es {numero_tres}')
