import json 
import time
import sys
from funciones import *

with open('futbol.json', 'r') as archivo:
    datos = json.load(archivo)

equipos = datos['equipos']

menu = '''
1.Listar equipos
2.Mostrar equipos y jugadores
3.Filtrar jugadores por su posición
4.Buscar información de un equipo y su capitán
5.Buscar jugadores por dorsal
6.Salir del programa
Ingrese una opción: '''

opcion = -1

while opcion != 0:
    opcion = int(input(menu))
    if opcion == 1:
        listar_equipos(equipos)
    elif opcion == 2:
        mostrar_jugadores(equipos)
    elif opcion == 3:
        filtrar_posicion(equipos)
    elif opcion == 4:
        capitan(equipos)
    elif opcion == 5:
        buscar_dorsal(equipos)
    elif opcion == 6:
        salir()
    else:
        print("Por favor, introduzca un número correcto(1-6): ")
