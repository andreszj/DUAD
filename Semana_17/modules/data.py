import os
import csv

def write_csv_file (file_path, data, headers):
    
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def read_csv_file(file_path):

    list_movement = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_movement.append(row)
        return list_movement


def create_empty_csv (file_path):

    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        pass


def import_csv (file_path):

    data = []
    if not os.path.exists(file_path):
        print ('Data does not exist')
    else:
        data = read_csv_file(file_path)
        print ('Data imported')
        return data


def export_csv (file_path, list_to_export, header):

    create_empty_csv (file_path)
    write_csv_file (file_path, list_to_export, header)


# Functions to import and export data specifically:

def export_category_list (list_of_categories):

    file_path = 'categories.csv'
    header = {
        'Category' : '',
        }
    list_to_export = []

    for item in list_of_categories:
        header['Category'] = item
        aux_dictionary = header.copy()
        list_to_export.append(aux_dictionary)

    export_csv(file_path,list_to_export,header)


def export_file_list (list_of_files):

    file_path = 'list_of_files.csv'
    header = {
        'File Name' : '',
        }
    list_to_export = []

    for item in list_of_files:
        header['File Name'] = item
        aux_dictionary = header.copy()
        list_to_export.append(aux_dictionary)

    export_csv(file_path,list_to_export,header)


def export_account_activity(list_to_export):

    file_path = 'last_activity.csv'
    header = {
        'Name' : '',
        'Account Number' : '',
        '#' : 0,
        'Category' : '',
        'Title' : '',
        'Expense' : 0,
        'Income' : 0,
        }
    name = list_to_export[0]['Name']
    backup_file_path = name+'_activity.csv'
    export_csv (file_path, list_to_export, header)
    export_csv (backup_file_path, list_to_export, header)

    return


def import_list(file_path):
    
    categories = import_csv (file_path)
    list_to_import = []
    
    if os.path.exists(file_path):
        for index in range(0, len(categories)):
            for value in categories[index].values():
                list_to_import.append(value)
    
    return list_to_import


def import_account_activity(file_path):

    activity = import_csv (file_path)
    list_to_import = []

    if os.path.exists(file_path):
        return activity
    
    return list_to_import


def save_files_and_activity(file_list, account):

    file_list.add_new_data(account.customer)
    file_list.sort_data_list()
    export_file_list(file_list.data_list)
    export_account_activity(account.transaction)  