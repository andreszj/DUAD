#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = [
    'Hay',
    'en',
    'que',
    'iteracion',
    'indices',
    'muy'
]

second_list = [
    'casos',
    'los',
    'la',
    'por',
    'es',
    'util'
]

rango_uno = len(first_list)
rango_dos = len(second_list)

for index in range (0, max(rango_uno , rango_dos)):
    print (f'{first_list[index]} {second_list [index]}')