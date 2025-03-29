import actions
import data

def print_menu() :

    print ('===================MENU======================')

    print ('''
    1. Add new student
    2. Show Students information
    3. Show Top 3 
    4. Show average grades
    5. Export data
    6. Import data
    7. Exit''')

    print ('=============================================')

def menu_options ():
    Again = True
    file_path = 'students.csv'
    students_list = []    

    while (Again):
        option = input ('Enter a menu option: ')
        option = actions.is_not_integer(option)
        option = actions.is_not_valid_menu_option (option)

        # average_list = actions.calculate_average (students_list)

        if (option == 1):
            students_list.append(actions.add_info ())
        elif (option == 2):
            for item in students_list:
                print (f'Name: {item.name}')
                print (f'Section: {item.section}')
                print (f'Spanish grade {item.spanish}')
                print (f'English grade: {item.english}')
                print (f'History grade: {item.history}')
                print (f'Science grade: {item.science}')
                print ('----------------------')
            input ('Push [ENTER] to continue ')

        elif (option == 3):
            actions.top_students (students_list)
            input ('Push [ENTER] to continue ')
        elif (option == 4):
            actions.calculate_total_average (students_list)
            input ('Push [ENTER] to continue ')
        elif (option == 5):
            data.export_csv(file_path, students_list)
            input ('Data exported... Push [ENTER] to continue')
        elif (option == 6):
            students_list.extend(data.import_csv(file_path))
            input ('Data imported... Push [ENTER] to continue')
        elif (option == 7):
            Again = False
        
        print_menu()