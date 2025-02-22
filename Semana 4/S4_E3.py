#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
numero_aleatorio = random.randint(1 , 10)
numero_usuario = int (input('Ingrese un número: '))
while (numero_aleatorio != numero_usuario):
    numero_usuario = int (input('Ingrese un número: '))
print ('Adivinó número!')