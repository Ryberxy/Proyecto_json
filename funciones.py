import json
import time
import sys

def salir():
    print("Saliendo del programa...⏳")
    time.sleep(3)
    sys.exit(1)
    
def listar_equipos(equipos):
    for equipo in equipos: 
        print(equipo)
    print(f"Hay {len(equipos)} equipos en la liga.")

def mostrar_jugadores(equipos):
    print(f"{'Equipos':<20}{'Numero de jugadores':<10}")
    for equipo in equipos:
        numero_jugadores = len(equipos[equipo]['jugadores'])
        print(f"{equipo:<20}{numero_jugadores:<10}")

def filtrar_posicion(equipos):
    posiciones = []
    numero_jugadores = 0
    pos = input("Ingrese una posición: ")
    for equipo in equipos:
        for jugador in equipos[equipo]['jugadores']:
            if jugador['detalles']['posicion'] == pos:
                posiciones.append(jugador['nombre'])
                numero_jugadores += 1
    for posicion in posiciones:
        print(f"{posicion}")
    print(f"Hay {numero_jugadores} jugadores con la posición {pos} en la liga.")

def capitan(equipos):
    encontrado = False
    capitan = input("Ingresa el capitán de un equipo🥇: ")
    for equipo in equipos:
        for jugador in equipos[equipo]['jugadores']:
            if jugador['nombre'] == capitan and jugador['detalles']['capitan']:
                for dorsal in jugador['detalles']['dorsales']:
                    dorsal = jugador['detalles']['dorsales']
                print(f"Dorsales: {dorsal[0]}, {dorsal[1]}, {dorsal[2]}, Equipo: {equipo}")
                encontrado = True
    if encontrado:
        print("Saliendo al menú principal...⏳")
        time.sleep(3)
    else:
        print(f"{capitan} no es el capitán de ningún equipo o no existe.")
            
def buscar_dorsal(equipos):
    encontrado = False
    eq = input("Ingrese un equipo: ")
    print(f"{'-'*45}")
    print(f"{'Jugador':<20} {'Dorsales':<10}")
    print(f"{'-'*45}")
    if eq in equipos:
            for jugador in equipos[eq]['jugadores']:
                nombre = jugador['nombre']
                dorsal = jugador['detalles']['dorsales']
                print(f"{nombre:<20} {dorsal[0]:<10}{dorsal[1]:<11}{dorsal[2]:<12}")
                print(f"{'-'*45}")

            try:
                pedir_dorsal = int(input("Ingrese el dorsal de un jugador de dicho equipo: "))
            except ValueError:
                print("Por favor, ingrese un número válido. Vuelve a introducir el equipo primero.")
                return buscar_dorsal(equipos)
            print("-" * 115)  
            print(f"{'Jugador':<20} {'Nacionalidad':<15} {'Fecha':<15} {'Valor':<10} {'Posición':<15} {'Pierna Hábil':<15} {'Altura':<10} {'Capitán':<10}")
            print("-" * 115)  


            for jugador in equipos[eq]['jugadores']:
                if pedir_dorsal in jugador['detalles']['dorsales']:
                    nombre2 = jugador['nombre']
                    nacionalidad = jugador['nacionalidad']
                    fecha = jugador['fechaNacimiento']
                    valor = jugador['detalles']['valor']
                    posicion = jugador['detalles']['posicion']
                    pie_bueno = jugador['detalles']['pieHabil']
                    altura = jugador['detalles']['altura']
                    capi = jugador['detalles']['capitan']
                    capitan = "Sí" if capi else "No"
                    
                    # Imprimir los detalles en la tabla
                    print(f"{nombre2:<20} {nacionalidad:<15} {fecha:<15} {valor:<10} {posicion:<15} {pie_bueno:<15} {altura:<10} {capitan:<10}")
                    print("-" * 115)
                    encontrado = True

            if encontrado:
                print("Saliendo al menú principal...⏳")
                time.sleep(3)
            else:
                print(f"El dorsal número {pedir_dorsal} no existe o no lo utiliza ningún futbolista de este equipo: {eq}")
    else:       
        print(f"El equipo: {eq}, no existe o no está en la liga.")

