# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_file_and_save_list(path):
    song_list = []
    with open(path) as file:
        for line in file.readlines():
            song_list.append (line)
    return song_list


def order_list (list_variable):
    aux_list = []
    for item in list_variable:
        inserted = False
        for index in range (0, len(aux_list)):
            if item < aux_list[index]:
                aux_list.insert(index, item)
                inserted = True
                break
        if not inserted:
            aux_list.append(item)
    
    return aux_list


def write_file(path, log):
    with open(path, 'w') as file:
        file.writelines(log)
    print ('Documento guardado')


def main () :
    list_of_songs = open_file_and_save_list ('canciones.txt')
    list_of_songs = order_list (list_of_songs)
    write_file('canciones2.txt', list_of_songs)


main ()