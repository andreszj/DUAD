import os

class Student:
    def __init__(self, name, section, spanish, english, history, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.history = history
        self.science = science
        self.average = ((spanish + english + history + science)/4)

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
            number = input (f'[   {number}   ] Invalid option. Please add the number again >>>   ')

def is_not_valid_grade (grade):
    error_grade = True
    while (error_grade):
        try:
            if (0 <= grade <= 100):
                return grade
                error_grade = False
            else:
                raise ValueError ('Invalid Grade. Please add the grade again >>>   ')
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
                raise ValueError ('Invalid option. Please add option again >>>   ')
        except ValueError as ex:
            number = input (ex)
            number = is_not_integer(number)



def add_info () :
    
    name = input('Enter the student s name: ')
    section = input('Enter the student s section: ')
    spanish = input('Enter Spanish grade: ')
    spanish = is_not_integer(spanish)
    spanish = is_not_valid_grade (spanish)
    english = input('Enter English grade: ')
    english = is_not_integer(english)
    english = is_not_valid_grade (english)
    history = input('Enter History grade: ')
    history = is_not_integer(history)
    history = is_not_valid_grade (history)
    science = input('Enter Science grade: ')
    science = is_not_integer(science)
    science = is_not_valid_grade (science)
    new_student = Student (name,section,spanish,english,history,science)
    return new_student


def calculate_total_average (student_list) :
    total_average = 0
    qty = len (student_list)
    for index in range (0 , qty):
        total_average = student_list[index].average + total_average
    total_average = total_average / qty
    print (f'Average of the averages: {total_average}')
    return total_average 


def top_students (student_list):
    aux_list = []
    top_list = []
    for item in student_list:
        inserted = False
        for index in range (0, len(aux_list)):
            if item.average > aux_list[index].average:
                aux_list.insert(index, item)
                inserted = True
                break
        if not inserted:
            aux_list.append(item)
    top_list.extend([aux_list[0], aux_list[1], aux_list[2]])
    print(f'TOP3: ')
    print ('----------------------')
    for item in top_list:
        print (f'Student Name: {item.name} Average: {item.average}')
        print ('----------------------')