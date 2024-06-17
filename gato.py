import random


def imprimir_tablero(tablero):
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")


def hay_ganador(tablero, jugador):
    o
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    
    for comb in combinaciones_ganadoras:
        if all(tablero[pos] == jugador for pos in comb):
            return True
    return False


def tablero_lleno(tablero):
    return all(cell != ' ' for cell in tablero)


print("¡Bienvenido al juego GATO!")


while True:
   
    print("\nMENU:")
    print("1. Nueva partida (Player 1 VS COM)")
    print("2. Versus (P1 VS P2)")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la opción que desea: ")
    
    if opcion == '1':
        
        tablero = [' '] * 9
        turno = 'X'
        print("Nueva partida: Player 1 (X) VS COM (O)")
        print("Player 1 empieza primero (X)")
        imprimir_tablero(tablero)
        
        while True:
            
            print("\nTurno de Player 1 (X)")
            jugada = int(input("Ingrese la posición (1-9): ")) - 1
            if tablero[jugada] == ' ':
                tablero[jugada] = 'X'
                imprimir_tablero(tablero)
                
                if hay_ganador(tablero, 'X'):
                    print("¡Player 1 (X) ha ganado!")
                    break
                elif tablero_lleno(tablero):
                    print("¡Es un empate!")
                    break
                
              
                print("\nTurno de COM (O)")
                while True:
                    jugada_com = random.randint(0, 8)
                    if tablero[jugada_com] == ' ':
                        tablero[jugada_com] = 'O'
                        imprimir_tablero(tablero)
                        if hay_ganador(tablero, 'O'):
                            print("¡COM (O) ha ganado!")
                            break
                        break
            else:
                print("¡Posición ocupada! Intente de nuevo.")
    
    elif opcion == '2':
       
        tablero = [' '] * 9
        turno = 'X'
        print("Versus: Player 1 (X) VS Player 2 (O)")
        print("Player 1 empieza primero (X)")
        imprimir_tablero(tablero)
        
        while True:
            print(f"\nTurno de Player {turno} ({turno})")
            jugada = int(input("Ingrese la posición (1-9): ")) - 1
            if tablero[jugada] == ' ':
                tablero[jugada] = turno
                imprimir_tablero(tablero)
                
                if hay_ganador(tablero, turno):
                    print(f"¡Player {turno} ({turno}) ha ganado!")
                    break
                elif tablero_lleno(tablero):
                    print("¡Es un empate!")
                    break
                
               
                turno = 'O' if turno == 'X' else 'X'
            else:
                print("¡Posición ocupada! Intente de nuevo.")
    
    elif opcion == '3':
    
        print("¡Gracias por jugar!")
        break
    
    else:
        print("Opción inválida. Por favor, elija una opción válida (1-3).")
        print("Opción inválida. Intente de nuevo.")
