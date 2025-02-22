# Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = [
    'first_name', 
    'last_name', 
    'role']
list_b = [
    'Alek', 
    'Castillo', 
    'Software Engineer'
    ]

diccionario = {}

longitud_listas = len(list_a)

for index in range (0, longitud_listas):
    diccionario[list_a[index]] = list_b[index]

print (diccionario)