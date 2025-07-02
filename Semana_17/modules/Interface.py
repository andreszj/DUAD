import os
import logic
import FreeSimpleGUI as sg
import data


# Data loading and setup functions:

categories = logic.DataList()
categories.data_list = data.import_list('categories.csv')

file_list = logic.DataList()
file_list.data_list = data.import_list('list_of_files.csv')

file_path = 'last_activity.csv'
data_imported = data.import_account_activity(file_path)

account = logic.decode_imported_account_activity(data_imported, file_path)


# GUI Windows:

def is_not_a_number_window():

    sg.theme('Reddit')

    layout= [
    [sg.Text('The amount must be entered in')],
    [sg.Text('numeric format.')],
    [sg.Button('Accept', size = (15,1),pad=(1,10),key="-ACCEPT BUTTON-")],
    ]
    
    window = sg.Window("Error", layout,finalize=True, size=(300,120))    

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == '-ACCEPT BUTTON-':            
            break

    window.close()


def category_exception_window():

    sg.theme('Reddit')

    layout= [
    [sg.Text('Selecting a category is a requirement')],
    [sg.Text('to add a new income or expense.')],
    [sg.Button('Accept', size = (15,1),pad=(1,10),key="-ACCEPT BUTTON-")],
    ]
    
    window = sg.Window("Error", layout,finalize=True, size=(300,120))    

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == '-ACCEPT BUTTON-':            
            break

    window.close()


def new_user_window():

    sg.theme('Reddit')

    layout= [
    [sg.Text('Name: '),sg.Input(s=35,key="-NAME-")],
    [sg.Text('Account Number: '),sg.Input(s=20,key="-ACCOUNT-")],
    [sg.Button('Accept', size = (15,1),pad=(1,10),key="-ACCEPT BUTTON-")],
    ]
    
    window = sg.Window("Add new user", layout,finalize=True, size=(300,120))    

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == '-ACCEPT BUTTON-':

            data.save_files_and_activity(file_list, account)

            customer =  values ['-NAME-']
            number_of_processes = values ['-ACCOUNT-']
            account.reset(customer,number_of_processes,0)
            
            break

    window.close()


def open_file_window():

    sg.theme('Reddit')

    list_files = logic.decode_list_to_print(file_list.data_list)

    layout= [
    [sg.Combo(list_files, size=(35,1), k='-COMBO-')],
    [sg.Button('Accept', size = (15,1),pad=(1,10),key="-ACCEPT BUTTON-"),sg.Button('Cancel', size = (15,1),pad=(1,10),key="-CANCEL BUTTON-")],
    ]
    
    window = sg.Window("Open File", layout,finalize=True, size=(300,100))

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '-CANCEL BUTTON-':
            break
        elif event == '-ACCEPT BUTTON-':

            data.save_files_and_activity(file_list, account)
            
            file_name = values ['-COMBO-'][0]
            file_path = file_name + '_activity.csv'
            
            data_imported = data.import_account_activity(file_path)

            aux_account = logic.decode_imported_account_activity(data_imported,file_path)

            account.reset(aux_account.customer,aux_account.number_of_processes,aux_account.balance)
            account.transaction = data_imported

            break
    
    window.close()


def category_window():
    
    sg.theme('Reddit')
    
    list_categories = categories.data_list

    layout= [
    [sg.Input(s=15,key="-NEW CATEGORY-"),sg.Button("+", size = (2,1), key= "-ADD BUTTON-"),sg.Table(list_categories, ['   Categories   '], cols_justification='center',size=(1,1),num_rows=5,key="-TABLE-")],
    [sg.Button('Accept', size = (15,1),pad=(1,10),key="-ACCEPT BUTTON-")],
    ]
    
    window = sg.Window("Categories", layout,finalize=True, size=(500,200))
    
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == '-ADD BUTTON-':

            new_category = values ['-NEW CATEGORY-']
            
            categories.add_new_data(new_category)
            categories.sort_data_list()

            list_categories = logic.decode_list_to_print(categories.data_list)
        
            window['-TABLE-'].update(list_categories) 
            window['-NEW CATEGORY-'].update('')
        
        elif event == '-ACCEPT BUTTON-':

            data.export_category_list(categories.data_list)
            break

    window.close()


def save_window():

    sg.theme('Reddit')

    layout= [
    [sg.Text('Document saved.')],
    [sg.Button('Accept', size = (15,1),pad=(1,10),key="-ACCEPT BUTTON-")],
    ]
    
    window = sg.Window("Save", layout,finalize=True, size=(300,120))    

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == '-ACCEPT BUTTON-':            
            break

    window.close()


def income_window():
    
    sg.theme('Reddit')

    list_categories = logic.decode_list_to_print(categories.data_list)

    layout_buttons= [
    [sg.Text('          Title                       Category                      Amount')],
    [sg.Input(s=15, key="-TITLE INPUT-"),sg.Combo(list_categories, size=(15,1), k='-COMBO-'), sg.Input(0.00,s=15, key="-AMOUNT INPUT-")],
    [sg.Button("Add Income", size = (15,1),pad=(1,40),key="-INCOME BUTTON-"),sg.Button("Cancel", size = (15,1),key='-CANCEL BUTTON-')],
    ]
    
    window = sg.Window("Add Income", layout_buttons,finalize=True, size=(450,200))

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '-CANCEL BUTTON-':
            break
        elif event == '-INCOME BUTTON-':
            try:
                title = values ['-TITLE INPUT-']
                category = values ['-COMBO-'][0]
                amount = float(values ['-AMOUNT INPUT-'])
                account.add_income(amount,category,title)
                break
            except IndexError:
                category_exception_window()
            except ValueError:
                is_not_a_number_window()

    window.close()


def expense_window():
    
    sg.theme('Reddit')

    list_categories = logic.decode_list_to_print(categories.data_list)

    layout_buttons= [
    [sg.Text('          Title                       Category                      Amount')],
    [sg.Input(s=15,key='-TITLE INPUT-'), sg.Combo(list_categories, size=(15,1), k='-COMBO-'), sg.Input(0.00,s=15,key='-AMOUNT INPUT-')],
    [sg.Button("Add Expense", size = (15,1),pad=(1,40),key='-EXPENSE BUTTON-'),sg.Button("Cancel", size = (15,1),key='-CANCEL BUTTON-')],
    ]
    
    window = sg.Window("Add Expense", layout_buttons,finalize=True, size=(450,200))

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == '-CANCEL BUTTON-':
            break

        elif event == '-EXPENSE BUTTON-':
            try:
                title = values ['-TITLE INPUT-']
                category = values ['-COMBO-'][0]
                amount = float(values ['-AMOUNT INPUT-'])
                account.add_expense(amount,category,title)
                break
            except IndexError:
                category_exception_window()
            except ValueError:
                is_not_a_number_window()

    window.close()


def main_window():


    sg.theme('Reddit')

    if not os.path.exists('last_activity.csv'):
        new_user_window()

    list_to_print = logic.decode_transactions_to_print(account.transaction)

    layout_buttons= [
    [sg.Button("Income", pad = (25,1), size = (15,1))],
    [sg.Button("Expense", pad = (25,1), size = (15,1))],
    ]

    layout_table1= [
    [sg.Table([[account.balance]], ['                Total Amount ($)             '], hide_vertical_scroll=True, cols_justification='center',size=(1,1),row_height=30,key="-BALANCE-")],
    ]

    layout_table2= [
    [sg.Table(list_to_print, ['#  ','Category','    Title   ','Expense ($)','Income ($)'], pad = (213,5), num_rows= 10, key="-MAIN TABLE-")],
    ]

    layout = [
    [sg.MenubarCustom([['File', ['New','Open','Save','Exit']], ['Add', ['Categories', ]]],bar_background_color="#D3D3D3")],
    [sg.Text(account.customer, text_color= "#000000", pad = (25,20), size=(15,1), background_color="#FEFEFE", justification=('center'),key="-NAME-"),sg.Text("Account number: "+account.number_of_processes, text_color= "#000000", pad = (25,20), background_color="#FEFEFE",key="-ACCOUNT NUMBER-")],
    [sg.Col(layout_buttons,background_color="#FEFEFE"), sg.Col(layout_table1, background_color="#FEFEFE")],
    [layout_table2],
    ]

    window = sg.Window("Management Account", layout,finalize=True, size=(1050,400))

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            if account.transaction == []:
                break
            else:
                data.save_files_and_activity(file_list, account)
                save_window()
                break

        elif event == 'Income':

            income_window()
            list_to_print = logic.decode_transactions_to_print(account.transaction)
            logic.update_main_window(window,account,list_to_print)

        elif event == 'Expense':

            expense_window()
            list_to_print = logic.decode_transactions_to_print(account.transaction)
            logic.update_main_window(window,account,list_to_print)

        elif event == 'Categories':

            category_window()

        elif event == 'New':

            new_user_window()
            list_to_print = logic.decode_transactions_to_print(account.transaction)
            logic.update_main_window(window,account,list_to_print)

        elif event == 'Open':

            open_file_window()
            list_to_print = logic.decode_transactions_to_print(account.transaction)
            logic.update_main_window(window,account,list_to_print)
        
        elif event == 'Save':

            if account.transaction != []:
                    
                save_window()
                data.save_files_and_activity(file_list, account)

        elif event == 'Exit':
            if account.transaction == []:
                break
            else:
                data.save_files_and_activity(file_list, account)
                save_window()
                break

    window.close()


main_window()