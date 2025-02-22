import json
import os


def create_empty_json (file_path):
    datos = []
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = json.dump(datos,file)
        pass


def read_json_file(file_path):
    pokemon_list = []
    with open(file_path, 'r') as file:
        pokemon_list = json.load(file)
        return pokemon_list


def input_name ():
    new_name = {}
    new_name ['english'] = input (f'Ingrese nombre de pokemon: ')
    return new_name


def input_type ():
    new_type = []
    new_type.append (input (f'Ingrese tipo de pokemon: '))
    return new_type


def input_base ():
    base_headers = (
        'HP',
        'Attack',
        'Defense',
        'Sp. Attack',
        'Sp. Defense',
        'Speed',
    )
    new_dictionary = {}
    for record in base_headers:
        new_dictionary [record] = input (f'Ingrese {record} : ')
    return new_dictionary


def write_json_file (file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def main ():

    pokemon_dict = {}
    file_path = 'pokemon.json'
    if not os.path.exists(file_path):
        create_empty_json (file_path)
    pokemon_list = read_json_file(file_path)

    pokemon_dict ['name'] = input_name ()
    pokemon_dict ['type'] = input_type ()
    pokemon_dict ['base'] = input_base ()

    pokemon_list.append(pokemon_dict)

    write_json_file (file_path, pokemon_list)


main()