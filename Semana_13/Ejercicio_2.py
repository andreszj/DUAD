# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def decorator(func):
    def wrapper (*args):
        run_function = True
        for item in args:
            try:
                if (float (item)):
                    print (item)
                else:
                    raise ValueError()
            except ValueError:
                run_function = False
                print(f'Parameter is not a number: {item}')
                print('Impossible to execute function')

        if (run_function != False):
            func(*args)
            print(f'AVERAGE: {func(*args)}')

    return wrapper


@decorator
def get_average_grade (spanish_grade, english_grade, japanese_grade):


    average = (spanish_grade+english_grade+japanese_grade)/3
    return average


print ('\n')

get_average_grade (80.0,90.1,'a')

print ('\n')

get_average_grade (80.0,90.1,100)
