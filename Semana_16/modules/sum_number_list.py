# Cree una función que retorne la suma de todos los números de una lista.

def sum_number_list (lista) :
    sumatoria = 0
    for number in lista:
        sumatoria=number+sumatoria
    return sumatoria

def main ():
    sumatoria = sum_number_list ([4, 6, 2, 29])
    print (sumatoria)

main ()