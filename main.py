import funciones
import Clases


categoriasUsadas = ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5"]

funciones.limpiarPantalla()
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
                    
                    funciones.limpiarPantalla()
                    Menu.menuNuevoJuego()
                    opcion = int(input("Seleccione una opcion: "))
                    
                    if opcion < 1 or opcion > 2:
                        print("Opcion incorrecta, ingrese una opcion nuevamente")
                    elif opcion == 1:
                        cometioErrores = False
                        nuevoPremio = Clases.Premio()
                        premioAcumulado = 0
                        #Desarrollo del juego. Las preguntas con sus verificaciones
                        for categoria in categoriasUsadas:
                            funciones.limpiarPantalla()
                            nuevaCategoria = Clases.Categoria()
                            nuevaCategoria.categoria("preguntas.txt", categoria)
                            preguntasCategoria = nuevaCategoria.getListaPreguntasPorCategoria()
                            nuevaPregunta  = Clases.Pregunta()
                            nuevaPregunta.seleccionPreguntaAleatoria(preguntasCategoria)
                            nuevaPregunta.mostrarPregunta()
                            preguntaAleatoria = nuevaPregunta.getPreguntaAleatoria()
                            respuestaJugador = int(input("Seleccione una opcion: "))
                            if respuestaJugador == 5:
                                print("Te has retirado de juego.")
                                resultado = "Deserto"
                                nuevoPremio.mostrarPremio(resultado, premioAcumulado)
                                break
                            nuevaValidacion = Clases.ValidacionRespuesta()
                            nuevaValidacion.validacion(preguntaAleatoria, respuestaJugador)
                            nuevaValidacion.mostrarResultado()
                            resultado = nuevaValidacion.getResultado()
                            nuevoPremio.premioCategoria(categoria, premioAcumulado)
                            nuevoPremio.mostrarPremio(resultado, premioAcumulado)
                            premioAcumulado = nuevoPremio.getPremio()
                            
                            if resultado == "Perdio":
                                break
                        if resultado == "Acerto":
                            print("Felicidades al responder todas las preguntas correctamente de cada categoria has ganago el juego!!!")
                            input("Presione cualquier tecla para continuar")

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
                    
                    funciones.limpiarPantalla()
                    Menu.menuNuevoJuego()
                    opcion = int(input("Seleccione una opcion: "))
                    
                    if opcion < 1 or opcion > 2:
                        print("Opcion incorrecta, ingrese una opcion nuevamente")
                    elif opcion == 1:
                        cometioErrores = False
                        nuevoPremio = Clases.Premio()
                        premioAcumulado = 0
                        #Desarrollo del juego. Las preguntas con sus verificaciones
                        for categoria in categoriasUsadas:
                            funciones.limpiarPantalla()
                            nuevaCategoria = Clases.Categoria()
                            nuevaCategoria.categoria("preguntas.txt", categoria)
                            preguntasCategoria = nuevaCategoria.getListaPreguntasPorCategoria()
                            nuevaPregunta  = Clases.Pregunta()
                            nuevaPregunta.seleccionPreguntaAleatoria(preguntasCategoria)
                            nuevaPregunta.mostrarPregunta()
                            preguntaAleatoria = nuevaPregunta.getPreguntaAleatoria()
                            respuestaJugador = int(input("Seleccione una opcion: "))
                            if respuestaJugador == 5:
                                print("Te has retirado de juego.")
                                resultado = "Deserto"
                                nuevoPremio.mostrarPremio(resultado, premioAcumulado)
                                break
                            nuevaValidacion = Clases.ValidacionRespuesta()
                            nuevaValidacion.validacion(preguntaAleatoria, respuestaJugador)
                            nuevaValidacion.mostrarResultado()
                            resultado = nuevaValidacion.getResultado()
                            nuevoPremio.premioCategoria(categoria, premioAcumulado)
                            nuevoPremio.mostrarPremio(resultado, premioAcumulado)
                            premioAcumulado = nuevoPremio.getPremio()
                            
                            if resultado == "Perdio":
                                break
                        if resultado == "Acerto":
                            print("Felicidades al responder todas las preguntas correctamente de cada categoria has ganago el juego!!!")
                            input("Presione cualquier tecla para continuar")

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


        funciones.limpiarPantalla()
