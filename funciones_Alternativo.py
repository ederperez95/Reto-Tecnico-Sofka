import os
import Clases

def limpiarPantalla():
    os.system("cls")  

def nuevo_juego():
    categoriasUsadas = ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5"]
    cometioErrores = False
    nuevoPremio = Clases.Premio()
    premioAcumulado = 0
    #Desarrollo del juego. Las preguntas con sus verificaciones
    for categoria in categoriasUsadas:
        limpiarPantalla()
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
