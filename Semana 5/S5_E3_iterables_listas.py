#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]
print (my_list)
tamano_lista = len (my_list)-1

for index , element_list in enumerate (my_list):
    if (index == 0):
        ultimo_lista = element_list
    elif (index == tamano_lista):
        primero_lista = element_list

my_new_list = my_list

print (my_list)

my_new_list [0] = primero_lista
my_new_list [tamano_lista] = ultimo_lista

print (my_new_list)