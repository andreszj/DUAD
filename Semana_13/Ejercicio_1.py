# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def decorator(func):
    def wrapper(*args):
        print(f'Parameters added: {args}')
        func(*args)
        print(func(*args))

    return wrapper

@decorator
def get_average_grade (spanish_grade, english_grade, japanese_grade):
    average = (spanish_grade+english_grade+japanese_grade)/3
    return average

get_average_grade (80,90,75)