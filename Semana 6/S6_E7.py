# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.


def is_prime_number (lista):
    aux_list = []
    for item in lista:
        counter = 0
        for index in range (1, item+1):
            if (item % index == 0) :
                counter = counter + 1
                if (counter > 2 ):
                    break
        if (counter == 2):
            aux_list.append (item)
    print (aux_list)


def main ():
    lista = [1, 4, 6, 7, 13, 9, 67]
    is_prime_number (lista)


main ()