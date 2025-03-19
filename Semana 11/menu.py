import actions
import data

def print_menu() :

    print ('===================MENU======================')

    print ('''
    1. Ingresar nuevo estudiante
    2. Ver informacion de todos los estudiantes
    3. Ver top 3 de estudiantes
    4. Ver promedio de notas
    5. Exportar datos actuales
    6. Importar datos previos
    7. Salir''')

    print ('=============================================')

def menu_options ():
    Again = True
    file_path = 'students.csv'
    students_list = []    

    while (Again):
        option = input ('Ingrese una opcion del menu: ')
        option = actions.is_not_integer(option)
        option = actions.is_not_valid_menu_option (option)

        # average_list = actions.calculate_average (students_list)

        if (option == 1):
            students_list.append(actions.add_info ())
        elif (option == 2):
            for item in students_list:
                print (f'Nombre: {item.name}')
                print (f'Seccion: {item.seccion}')
                print (f'Nota Espanol {item.spanish}')
                print (f'Nota Ingles: {item.english}')
                print (f'Nota Sociales: {item.sociales}')
                print (f'Nota Ciencias: {item.ciencias}')
                # for key in item:
                #     print (f'{key} : {item[key]}')
                print ('----------------------')
            input ('Presionar [ENTER] para continuar ')

        elif (option == 3):
            actions.top_students (students_list)
            input ('Presionar [ENTER] para continuar ')
        elif (option == 4):
            actions.calculate_total_average (students_list)
            input ('Presionar [ENTER] para continuar ')
        elif (option == 5):
            data.export_csv(file_path, students_list)
            input ('Datos exportados... Presionar [ENTER] para continuar')
        elif (option == 6):
            students_list.extend(data.import_csv(file_path))
            input ('Datos importados... Presionar [ENTER] para continuar')
        elif (option == 7):
            Again = False
        
        print_menu()