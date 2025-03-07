#5. Dada `n` cantidad de notas de un estudiante, calcular:
#    1. Cuantas notas tiene aprobadas (mayor a 70).
#    2. Cuantas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.

contador_de_nota = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0
total_de_notas = int (input ('Ingrese la cantidad de notas: '))
while (contador_de_nota <= total_de_notas):
    print (f'Ingrese la nota numero {contador_de_nota}')
    nota_actual = int (input ())
    contador_de_nota = contador_de_nota + 1
    if (nota_actual  < 70):
        cantidad_de_notas_desaprobadas =  cantidad_de_notas_desaprobadas + 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
    promedio_de_notas_total = promedio_de_notas_total + (nota_actual // total_de_notas)
promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas
print (f'El estudiante tiene esta cantidad de notas aprobadas {cantidad_de_notas_aprobadas}')
print (f'Este es el promedio de notas aprobadas {promedio_de_notas_aprobadas}')
print (f'El estudiante tiene esta cantidad de notas desaprobadas {cantidad_de_notas_desaprobadas}')
print (f'Este es el promedio de notas desaprobadas {promedio_de_notas_desaprobadas}')
print (f'Este es el promedio total de notas {promedio_de_notas_total}')