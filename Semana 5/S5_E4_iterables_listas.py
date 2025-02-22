#Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index , element_list in enumerate (my_list):
    if (my_list[index] %2 == 1 ):
        my_list.pop(index)

print (my_list)