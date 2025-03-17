import json
import sys

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
    pos = input("Ingrese una posición: ")
    for equipo in equipos:
        numero_jugadores = len(equipos[equipo]['jugadores'])
        for jugador in equipos[equipo]['jugadores']:
            if jugador['detalles']['posicion'] == pos:
                posiciones.append(jugador['nombre'])
    for posicion in posiciones:
        print(f"{posicion}")
    print(f"Hay {numero_jugadores} jugadores con la posición {pos} en la liga.")

def capitan(equipos):
    encontrado = False
    capitan = input("Ingresa el capitán de un equipo: ")
    for equipo in equipos:
        for jugador in equipos[equipo]['jugadores']:
            if jugador['nombre'] == capitan and jugador['detalles']['capitan']:
                for dorsal in jugador['detalles']['dorsales']:
                    dorsal = jugador['detalles']['dorsales']
                print(f"Dorsales: {dorsal[0]}, {dorsal[1]}, {dorsal[2]}, Equipo: {equipo}")
                encontrado = True
    if encontrado:
        print("Saliendo al menú principal...")
    else:
        print(f"{capitan} no es el capitán de ningún equipo o no existe.")
            
def buscar_dorsal(equipos):
    encontrado = False
    eq = input("Ingrese un equipo: ")
    if eq in equipos:
            for jugador in equipos[eq]['jugadores']:
                nombre = jugador['nombre']
                dorsal = jugador['detalles']['dorsales']
                print(f"Jugador: {nombre}, Dorsales: {dorsal[0]}, {dorsal[1]}, {dorsal[2]}")

            try:
                pedir_dorsal = int(input("Ingrese el dorsal de un jugador de dicho equipo: "))
            except ValueError:
                print("Por favor, ingrese un número válido. Vuelve a introducir el equipo primero.")
                return buscar_dorsal(equipos)
            
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
                        if capi:
                            print(f"Jugador: {nombre2}, Nacionalidad: {nacionalidad}, Fecha: {fecha}, Valor: {valor}, Posición: {posicion}, Pierna Hábil: {pie_bueno}, Altura: {altura}, Capitán: Sí")
                        else:
                            print(f"Jugador: {nombre2}, Nacionalidad: {nacionalidad}, Fecha: {fecha}, Valor: {valor}, Posición: {posicion}, Pierna Hábil: {pie_bueno}, Altura: {altura}, Capitán: No")
                        encontrado = True

            if encontrado:
                print("Saliendo al menú principal...")
            else:
                print(f"El dorsal número {pedir_dorsal} no existe o no lo utiliza ningún futbolista de este equipo: {eq}")
    else:       
        print(f"El equipo: {eq}, no existe o no está en la liga.")


