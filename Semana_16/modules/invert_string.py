#Cree una función que le de la vuelta a un string y lo retorne.


def invert_string (string) :
    invert=''
    for index in range ((len (string)-1) , -1 , -1):
        invert = invert + string[index]
    return invert


def main () :
    imprimir = invert_string ('Hola mundo')
    print (imprimir)

main ()