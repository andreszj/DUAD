# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

my_list = []

for index in range (0 , 10):
    my_list.append(int (input(f'Ingrese numero {index+1}: ')))

print (f' Lista de datos: {my_list}')
print (f' El más alto fue: {max (my_list)}')