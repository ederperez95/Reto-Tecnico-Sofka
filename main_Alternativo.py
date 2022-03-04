import funciones_Alternativo
import Clases




funciones_Alternativo.limpiarPantalla()
opcionCorrecta = False
continuar = True
Menu = Clases.Menu
while(continuar):
    while(not opcionCorrecta):
        #menu para seleccionar si crear jugador o uno ya existente
        Menu.menuInicial()
        opcion = int(input("Seleccione una opcion: "))

        
        if opcion < 1 or opcion > 3:
            print("Opcion incorrecta, ingrese una opcion nuevamente")

        #Opcion 1 Seleccionar jugador para posteriormente jugar con ese usuario
        elif opcion == 1:

            nuevoJugador = Clases.Jugador()
            listaJugadores = nuevoJugador.listarJugadores(nombreArchivoJugadores = "jugadores.txt")
            opcionCorrecta = False
            continuar = True
            while(continuar):
                while(not opcionCorrecta):
                    opcionJugadorSeleccionado = int(input("Seleccione un jugador para empezar el juego: "))
                    if opcionJugadorSeleccionado < 1 or opcionJugadorSeleccionado > len(listaJugadores):
                        print("Opcion incorrecta, ingrese una opcion nuevamente")
                    else:
                        jugadorSeleccionado = listaJugadores[opcionJugadorSeleccionado - 1]
                        continuar = False
                        break
                        
            #Empieza el menu de juego nuevo 
            opcionCorrecta = False
            continuar = True
            while(continuar):
                while(not opcionCorrecta):
                    
                    funciones_Alternativo.limpiarPantalla()
                    Menu.menuNuevoJuego()
                    opcion = int(input("Seleccione una opcion: "))
                    
                    if opcion < 1 or opcion > 2:
                        print("Opcion incorrecta, ingrese una opcion nuevamente")
                    elif opcion == 1:
                        funciones_Alternativo.nuevo_juego()
                    elif opcion == 2:
                        print("De regreso al menu anterior")
                        input("Presione cualquier tecla para continuar")
                        continuar = False
                        break   

        #Opcion 2 creaar jugador para posteriormente jugar con ese usuario
        elif opcion == 2:
            nuevoJugador = Clases.Jugador()
            jugador = nuevoJugador.crearJugador(nombreArchivoJugadores = "jugadores.txt")
            #Empieza el menu de juego nuevo 
            opcionCorrecta = False
            continuar = True
            while(continuar):
                while(not opcionCorrecta):
                    
                    funciones_Alternativo.limpiarPantalla()
                    Menu.menuNuevoJuego()
                    opcion = int(input("Seleccione una opcion: "))
                    
                    if opcion < 1 or opcion > 2:
                        print("Opcion incorrecta, ingrese una opcion nuevamente")
                    elif opcion == 1:
                        funciones_Alternativo.nuevo_juego()

                    elif opcion == 2:
                        print("De regreso al menu anterior")
                        input("Presione cualquier tecla para continuar")
                        continuar = False
                        break   

        #Opcion 3 Salir del juego
        elif opcion == 3:
            print("Gracias por jugar!!")
            input("Presione cualquier tecla para continuar")
            continuar = False
            break


        funciones_Alternativo.limpiarPantalla()
