# Cree un diccionario que guarde la siguiente información sobre un hotel:

numero = ''
piso = ''
precio_por_noche = ''

hotel_information = {
    'nombre': '',
    'numero_de_estrellas' : '',
    'habitaciones' : [
        numero,
        piso,
        precio_por_noche,
        ] ,
}

hotel_information['nombre'] = input('Ingrese nombre del hotel: ')
hotel_information['numero_de_estrellas'] = input('Numero de estrellas: ')
hotel_information['habitaciones'][0] = input('Numero de habitacion: ')
hotel_information['habitaciones'][1] = input('Piso: ')
hotel_information['habitaciones'][2] = input('Precio por noche ')

print(hotel_information)
