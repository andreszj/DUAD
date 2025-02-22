#   calculadora

import os


def print_header ():
    print ('''1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
___________________________
''')


def sum_numbers (actual_number , second_number):
    actual_number = actual_number + second_number
    print (actual_number)
    return actual_number


def subtract_numbers (actual_number , second_number):
    actual_number = actual_number - second_number
    return actual_number


def mult_numbers (actual_number , second_number):
    actual_number = actual_number * second_number
    return actual_number


def div_numbers (actual_number , second_number):
    actual_number = actual_number / second_number
    return actual_number


def is_not_integer (number):
        error_int = True
        while (error_int):
            try:
                actual_number = int (input ('Ingrese numero: '))
                if (actual_number.is_integer()):
                    return actual_number
                    error_int = False
            except ValueError:
                os.system('cls')
                print_header ()
                print (f'[   {number}   ]')
                print (f'Opción inválida, ingrese nuevamente el numero...') 


def main ():

    print_header ()
    print ('[   0   ]')
    actual_number = is_not_integer (0)
    while (True):

        error_op = True
        while (error_op):
            operation = input ('Operador: ')
            try:
                if (operation not in ['1' , '2' , '3' , '4' , '5']):
                    raise ValueError ('Opción inválida, ingrese nuevamente el operador...')
                else:
                    error_op = False
            except ValueError as ex:
                os.system('cls')
                print_header ()
                print (f'[   {actual_number}   ]')
                print (ex)   

        if (operation == '5'):
            actual_number = 0
            os.system('cls')
            print_header ()
            print (f'[   {actual_number}   ]')
            actual_number = is_not_integer (actual_number)
            

        else:
            second_number = is_not_integer (actual_number)
            before_number = actual_number

            if (operation == '1'):
                operator = '+'
                actual_number = sum_numbers (actual_number , second_number)   
            elif (operation == '2'):
                operator = '-'
                actual_number = subtract_numbers (actual_number , second_number)
            elif (operation == '3'):
                operator = '*'
                actual_number = mult_numbers (actual_number , second_number)
            elif (operation == '4'):
                try:
                    if (second_number == 0 ):
                        raise ZeroDivisionError('Error de division entre 0, ingrese nuevamente el numero...')
                except ZeroDivisionError as ex:
                    os.system('cls')
                    print_header ()
                    print (f'[   {actual_number}   ]')
                    print (ex)
                    second_number = is_not_integer (actual_number)
                operator = '/'
                actual_number = div_numbers (actual_number , second_number)   
            
            os.system('cls')
            print_header ()
            print (f'[   {before_number} {operator} {second_number} = {actual_number}   ]')

main()