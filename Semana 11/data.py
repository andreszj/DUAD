import os
import csv

class Student:
    def __init__(self, name, section, spanish, english, history, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.history = history
        self.sciences = science
        self.average = ((spanish + english + history + science)/4)

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
        print ('File does not exist')
    else:
        data = read_csv_file(file_path)
        print (f'Imported data: {data}')
    
    student_list = []

    for item in data:
        new_student = Student (item ['Full name'], item ['Section'], int(item ['Spanish grade']), int(item ['English grade']), int(item ['History grade']), int(item ['Science grade']))  
        student_list.append (new_student)
    return student_list


def export_csv (file_path, students_list):
    student_header = {
    'Full name' : '',
    'Section' : '',
    'Spanish grade' : 0,
    'English grade' : 0,
    'History grade' : 0,
    'Science grade' : 0,
    'Average' : 0
    }

    
    new_list = []
    for item in students_list:
        student_dictionary = {
            'Full name' : item.name ,
            'Section' : item.section ,
            'Spanish grade' : item.spanish ,
            'English grade' : item.english ,
            'History grade' : item.history ,
            'Science grade' : item.science ,
            'Average' : item.average ,
            }
        new_list.append (student_dictionary) 

    create_empty_csv (file_path)
    write_csv_file (file_path, new_list, student_header)