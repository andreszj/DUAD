import os
import csv

class Student:
    def __init__(self, name, seccion, spanish, english, sociales, ciencias):
        self.name = name
        self.seccion = seccion
        self.spanish = spanish
        self.english = english
        self.sociales = sociales
        self.ciencias = ciencias
        self.average = ((spanish + english + sociales + ciencias)/4)

def write_csv_file (file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def read_csv_file(file_path):
    list_students = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_students.append(row)
        return list_students


def create_empty_csv (file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        pass


def import_csv (file_path):
    data = []
    if not os.path.exists(file_path):
        print ('No existe archivo')
    else:
        data = read_csv_file(file_path)
        print (f'Datos importados: {data}')
    
    student_list = []

    for item in data:
        new_student = Student (item ['Nombre completo'], item ['Seccion'], int(item ['Nota Espanol']), int(item ['Nota Ingles']), int(item ['Nota Sociales']), int(item ['Nota Ciencias']))  ########################VOY POR ACA
        student_list.append (new_student)
    return student_list


def export_csv (file_path, students_list):
    student_header = {
    'Nombre completo' : '',
    'Seccion' : '',
    'Nota Espanol' : 0,
    'Nota Ingles' : 0,
    'Nota Sociales' : 0,
    'Nota Ciencias' : 0,
    'Promedio' : 0
    }

    
    new_list = []
    for item in students_list:
        student_dictionary = {
            'Nombre completo' : item.name ,
            'Seccion' : item.seccion ,
            'Nota Espanol' : item.spanish ,
            'Nota Ingles' : item.english ,
            'Nota Sociales' : item.sociales ,
            'Nota Ciencias' : item.ciencias ,
            'Promedio' : item.average ,
            }
        new_list.append (student_dictionary) 

    create_empty_csv (file_path)
    write_csv_file (file_path, new_list, student_header)