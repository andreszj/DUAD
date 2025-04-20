# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def decorator(func):
    def wrapper (*args, **kwargs):
        run_function = True
        for item in args:
            try:
                if (isinstance (item, (int, float))):
                    print (item)
                else:
                    raise ValueError()
            except ValueError:
                run_function = False
                print(f'Parameter is not a number: {item}')
                print('Impossible to execute function')

            for key, value in kwargs.items():
                try:
                    if isinstance(value, (int, float)):
                        print(f'{key} : {value}')
                    else:
                        raise ValueError()
                except ValueError:
                    run_function = False
                    print(f'Parameter {key} is not a number: {value}')
                    print('Impossible to execute function')

        if (run_function != False):
            variable_returned = func(*args)
            print(f'AVERAGE: {variable_returned}')

    return wrapper


@decorator
def get_average_grade (spanish_grade, english_grade, japanese_grade):


    average = (spanish_grade+english_grade+japanese_grade)/3
    return average


print ('\n')

get_average_grade (80.0,90.1,'a')

print ('\n')

get_average_grade (80.0,90.1,100)
