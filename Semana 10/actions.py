import os

def is_not_integer (number):
    error_int = True
    while (error_int):
        try:
            number = int (number)
            if (number.is_integer()):
                return number
                error_int = False

        except ValueError:
            # os.system('cls')
            number = input (f'[   {number}   ] Opción inválida 1, ingrese nuevamente el numero >>>   ')

def is_not_valid_grade (grade):
    error_grade = True
    while (error_grade):
        try:
            if (0 <= grade <= 100):
                return grade
                error_grade = False
            else:
                raise ValueError ('Nota inválida 2, ingrese nota nuevamente >>>   ')
        except ValueError as ex: 
            grade = input (ex)
            grade = is_not_integer(grade)

def is_not_valid_menu_option (number):
    error_option = True
    while (error_option):
        try:
            if (1 <= number <= 7):
                return number
                error_option = False
            else:
                raise ValueError ('Opción inválida 3, ingrese opcion nuevamente >>>   ')
        except ValueError as ex:
            number = input (ex)
            number = is_not_integer(number)

def add_info (student_header) :
    new_student = {}
    for key in student_header.keys ():
        if (key == 'Nota Espanol' or key == 'Nota Ingles' or key == 'Nota Sociales' or key == 'Nota Ciencias'):
            info_aux = input(f'Ingrese {key} del estudiante: ')
            info_aux = is_not_integer(info_aux)
            info_aux = is_not_valid_grade (info_aux)
            new_student[key] = info_aux
        else:
            new_student[key] = input(f'Ingrese {key} del estudiante: ')
    return new_student


def calculate_average (students_list):
    average_list = []

    for index in range (0 , len (students_list)):
        student_average = {
            'Nombre completo' : students_list[index]['Nombre completo'],
            'Promedio de Notas' : (int(students_list[index]['Nota Espanol']) + int(students_list[index]['Nota Ingles']) + int(students_list[index]['Nota Sociales']) + int(students_list[index]['Nota Ciencias']))/4,
        }
        average_list.append(student_average)
    return average_list


def calculate_total_average (average_list) :
    total_average = 0
    qty = len (average_list)
    for index in range (0 , qty):
        total_average = average_list[index]['Promedio de Notas'] + total_average
    total_average = total_average / qty
    print (f'PROMEDIO DE PROMEDIOS: {total_average}')
    return total_average 


def top_students (average_list):
    aux_list = []
    top_list = []
    for item in average_list:
        inserted = False
        for index in range (0, len(aux_list)):
            if item['Promedio de Notas'] > aux_list[index]['Promedio de Notas']:
                aux_list.insert(index, item)
                inserted = True
                break
        if not inserted:
            aux_list.append(item)
    top_list.extend([aux_list[0], aux_list[1], aux_list[2]])
    print(f'Este es TOP3: ')
    print ('----------------------')
    for item in top_list:
        for key in item:
            print (f'{key} : {item[key]}')
        print ('----------------------')