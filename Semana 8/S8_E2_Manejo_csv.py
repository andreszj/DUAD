# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import os
import csv


def create_empty_csv (file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        pass


def input_function (game_headers, qty_aux):
    new_dictionary = {}

    for record in game_headers:
        new_dictionary [record] = input (f'Ingrese {record} de video juego {qty_aux} : ')
    return new_dictionary


def write_csv_file (file_path, data, headers):
    
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


def read_csv_file(file_path):

    list_games = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            list_games.append(row)
        return list_games


def main ():
    
    qty_games = int (input ('Cuántos juegos desea ingresar? '))
    qty_aux = 1
    game_headers = (
        'nombre',
        'genero',
        'desarrollador',
        'clasificacion ESRB',
    )
    file_path = 'gamesE2.csv'

    while ((qty_games + 1) != qty_aux): 
        print (f'**** VIDEO JUEGO {qty_aux} ****')
        if not os.path.exists(file_path):
            create_empty_csv (file_path)
        data = read_csv_file(file_path)
        data.append(input_function (game_headers , qty_aux))
        write_csv_file (file_path, data, game_headers)
        qty_aux = qty_aux + 1


main()