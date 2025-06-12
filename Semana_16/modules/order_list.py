# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.


def convert_string_to_list (string):
    list_of_words = []
    string_aux = ''
    for index in range (0, len(string)):
        if (string [index] == '-'):
            list_of_words.append (string_aux)
            string_aux = ''
        else:
            string_aux = string_aux + string [index]
    list_of_words.append (string_aux)
    print (f'Esta es la lista: {list_of_words}')
    return list_of_words


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
    
    print(f'Esta es el string ordenado: {aux_list}')
    return aux_list


def generate_new_list (string) :
    list_variable = convert_string_to_list (string)
    new_list = order_list (list_variable)
    return new_list

string = "python-house-1-car-dog-56788-children-book"
generate_new_list (string)