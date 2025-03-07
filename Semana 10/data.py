import os
import csv


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
        return data


def export_csv (file_path, students_list, student_header):
    create_empty_csv (file_path)
    write_csv_file (file_path, students_list, student_header)