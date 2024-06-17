import random

def mostrar_tablero(tablero):
    """ Función para mostrar el tablero actual """
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--|---|--")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--|---|--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print("\n")

def verificar_victoria(tablero, jugador):
    """ Función para verificar si hay un ganador """
    # Combinaciones ganadoras en el tablero
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for comb in combinaciones_ganadoras:
        if all(tablero[i] == jugador for i in comb):
            return True
    return False

def movimiento_computadora(tablero, jugador_computadora):
    """ Función para el movimiento de la computadora """
    disponibles = [i for i, v in enumerate(tablero) if v == " "]
    indice = random.choice(disponibles)
    tablero[indice] = jugador_computadora
    return indice

def juego_gato():
    """ Función principal que ejecuta el juego de gato """
    tablero = [" "] * 9
    jugadores = ["X", "O"]
    turno_actual = 0
    ganador = None
    
    print("¡Bienvenido al juego de Gato!\n")
    
    while True:
        mostrar_tablero(tablero)
        jugador_actual = jugadores[turno_actual % 2]
        
        if jugador_actual == "X":
            print("Turno del jugador 1 (X)")
        else:
            print("Turno del jugador 2 (O)")
        
        if jugador_actual == "X":
            indice = movimiento_jugador(tablero, "X")
        else:
            indice = movimiento_computadora(tablero, "O")
        
        if verificar_victoria(tablero, jugador_actual):
            ganador = jugador_actual
            break
        
        if " " not in tablero:
            break
        
        turno_actual += 1
    
    mostrar_tablero(tablero)
    
    if ganador:
        print(f"¡El jugador {ganador} ha ganado!")
    else:
        print("¡Empate!")
    
    print("Gracias por jugar.\n")

def movimiento_jugador(tablero, jugador):
    """ Función para el movimiento del jugador """
    while True:
        try:
            indice = int(input("Selecciona una casilla (1-9): ")) - 1
            if indice < 0 or indice > 8 or tablero[indice] != " ":
                print("Casilla inválida. Intenta de nuevo.")
            else:
                tablero[indice] = jugador
                break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número del 1 al 9.")
    
    return indice

def menu_principal():
    """ Función para mostrar el menú principal """
    while True:
        print("----- MENÚ -----")
        print("1. Nueva partida (Player 1 VS COM)")
        print("2. Versus (P1 VS P2)")
        print("3. Salir")
        opcion = input("Selecciona una opción (1/2/3): ")
        
        if opcion == "1":
            juego_gato()  # Iniciar nueva partida contra la computadora
        elif opcion == "2":
            juego_gato_versus()  # Iniciar modo versus (jugador vs jugador)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
