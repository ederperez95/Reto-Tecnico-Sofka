import csv
import random
import funciones

################################################################################################################
class Categoria:
    def __init__(self):
        self.preguntasCategoria = []

    def categoria(self, nombreArchivoPreguntas, categoriaDeseada):
        with open(nombreArchivoPreguntas, mode='r', encoding='utf-8') as archivoPreguntas:

            listaPreguntas = csv.reader(archivoPreguntas, delimiter = ';')
            for Pregunta in listaPreguntas:

                categoriaActual = Pregunta[0]
                if categoriaActual == categoriaDeseada:

                    self.preguntasCategoria.append(Pregunta)

    def getListaPreguntasPorCategoria(self):
        return self.preguntasCategoria

################################################################################################################
class Premio:
    def __init__(self):
        self.premioActual = 0
        
    def premioCategoria(self, categoria, premioAcumuladoActual):
        if categoria == "Categoria 1":
            self.premioActual = 100000 + premioAcumuladoActual
        elif categoria == "Categoria 2":
            self.premioActual = 200000 + premioAcumuladoActual   
        elif categoria == "Categoria 3":
            self.premioActual = 300000 + premioAcumuladoActual  
        elif categoria == "Categoria 4":
            self.premioActual = 500000 + premioAcumuladoActual   
        elif categoria == "Categoria 5":
            self.premioActual = 1000000 + premioAcumuladoActual   

    def mostrarPremio(self, resultado, premioAcumuladoActual):
        if resultado == "Perdio":
            print("\nDebido a que respondiste mal tu premio tiene un valor de 0 pesos.\n".format(self.premioActual))
            input("Presione cualquier tecla para continuar")
        elif resultado == "Acerto":
            print("\nFelicidades su premio hasta el momento es de {0} pesos!!!\n".format(self.premioActual))
            input("Presione cualquier tecla para continuar")
        elif resultado == "Deserto":
            print("\nFelicidades su premio debido a que se retiro es de {0} pesos!!!\n".format(premioAcumuladoActual))
            input("Presione cualquier tecla para continuar")

    def getPremio(self):
        return self.premioActual


################################################################################################################
class Pregunta:
    def __init__(self):
        self.preguntaAleatoria = []
        self.numeroDePreguntas = 0

    def seleccionPreguntaAleatoria(self, preguntasPorCategoria):
        self.numeroDePreguntas = len(preguntasPorCategoria)
        numeroAleatorio = random.randrange(self.numeroDePreguntas)
        self.preguntaAleatoria = preguntasPorCategoria[numeroAleatorio]

    def mostrarPregunta(self):
        nivel = self.preguntaAleatoria[0]
        pregunta = self.preguntaAleatoria[1]
        opcionUno = self.preguntaAleatoria[2]
        opcionDos = self.preguntaAleatoria[3]
        opcionTres = self.preguntaAleatoria[4]
        opcionCuatro = self.preguntaAleatoria[5]

        enunciado = """\nPara pasar esta ronda responde la pregunta correspondiente a la {0}. la pregunta a responder es:\n\n{1}\nLas opciones son:\n\n1. {2}\n2. {3}\n3. {4}\n4. {5}\n\n5. Recuerda que puedes salir cuando quieras seleccionando la opcion 5.\n"""
        print(enunciado.format(nivel, pregunta, opcionUno, opcionDos, opcionTres, opcionCuatro))


    def getPreguntaAleatoria(self):
        return self.preguntaAleatoria

################################################################################################################
class ValidacionRespuesta:
    def __init__(self):
        self.resultado = "Perdio"
        self.respuestaCorrecta = ""
        self.respuestaSeleccionada = ""

    def validacion(self, preguntaAleatoria, respuestaJugador):
        self.respuestaCorrecta = preguntaAleatoria[6]
        self.respuestaSeleccionada = preguntaAleatoria[respuestaJugador + 1]

        if self.respuestaCorrecta == self.respuestaSeleccionada:
            self.resultado = "Acerto"

    def mostrarResultado(self):
        
        if self.resultado == "Acerto":
            print("\nEnhorabuena la respuesta es correcta!!!\n")

        else:
            print("\nLa respuesta es incorrecta, pero no te desanimes puedes empezar una nueva partida!!!\n")
 
    
    def getResultado(self):
        return self.resultado

################################################################################################################    
class Menu:
    def menuInicial():
        print("============= Menu de Inicio =============")
        print("1. Seleccionar Jugador")
        print("2. Crear Jugador")
        print("3. Salir del Juego")
        print("============================================")

    def menuNuevoJuego():
        print("============= Menu principal =============")
        print("1. Nuevo Juego")
        print("2. Volver al menu inicial")
        print("============================================")


################################################################################################################    
class Jugador:
    def __init__(self):
        
        self.premio = "0"
        self.categoria = "Categoria 1"
        self.juegosGanados = "0"
        self.jugadorExistente = False
        self.nombreJugadorEnLista = ""
        self.listaDeJugadores = []
        self.contador = 1

    def crearJugador(self, nombreArchivoJugadores):
        with open(nombreArchivoJugadores, mode='r+', encoding='utf-8') as archivoJugadores:
            self.nombre = input("ingrese el nombre del jugador: ")
            listaJugadores = csv.reader(archivoJugadores, delimiter = ';')
            for jugador in listaJugadores:
                self.nombreJugadorEnLista = jugador[0]
            
                if self.nombreJugadorEnLista == self.nombre:
                    print("""El jugador {0} ya ha sido creado, en adelante este usuario se usara para registrar su puntaje en el juego \n""".format(self.nombre))
                    input("Presione cualquier tecla para continuar")
                    self.jugadorExistente = True
                    break
            if not self.jugadorExistente:
                archivoJugadores.write("\n" + self.nombre + ";" + self.premio + ";" + self.categoria + ";" + self.juegosGanados)
                print("jugador creado exitosamente")
                input("Presione cualquier tecla para continuar")
        return [self.nombre, self.premio, self.categoria, self.juegosGanados]

    def listarJugadores(self, nombreArchivoJugadores):
        with open(nombreArchivoJugadores, mode='r+', encoding='utf-8') as archivoJugadores:
            listaJugadores = csv.reader(archivoJugadores, delimiter = ';')
            print("\nla Lista de jugadores es:\n")
            for jugador in listaJugadores:
                print("{0}. ".format(self.contador) + jugador[0])
                self.listaDeJugadores.append(jugador[0])
                self.contador += 1
        return self.listaDeJugadores