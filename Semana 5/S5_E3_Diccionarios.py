# Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys = [
    'access_level', 
    'age'
    ]
employee = {
    'name': 'John', 
    'email': 'john@ecorp.com', 
    'access_level': 5, 
    'age': 28
    }

for index in range(0, len(list_of_keys)):
    borrar = list_of_keys[index]
    employee.pop(borrar)
print (employee)