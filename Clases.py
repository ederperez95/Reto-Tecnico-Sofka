import csv
import random

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

    def mostrarPremio(self):
        print("\nFelicidades su premio hasta el momento es de {0} pesos!!!\n".format(self.premioActual))

    def getPremio(self):
        return self.premioActual


################################################################################################################
class Pregunta:
    def __init__(self):
        self.preguntaAleatoria = []
        self.numeroDePreguntas = 0

    def seleccionPreguntaAleatoria(self, preguntasPorCategoria):
        self.numeroDePreguntas = len(preguntasPorCategoria)
        numeroAleatorio = random.randrange(self.preguntaAleatoria)
        self.preguntaAleatoria = preguntasPorCategoria[numeroAleatorio]

    def mostrarPregunta(self):
        nivel = self.preguntaAleatoria[0]
        pregunta = self.preguntaAleatoria[1]
        opcionUno = self.preguntaAleatoria[2]
        opcionDos = self.preguntaAleatoria[3]
        opcionTres = self.preguntaAleatoria[4]
        opcionCuatro = self.preguntaAleatoria[5]

        enunciado = """\nPara pasar esta ronda responde la pregunta correspondiente a la {0}. 
        la pregunta a responder es:\n\n{1}\nLas opciones son:\n\n1. {2}\n2. {3}\n3. {4}\n4. {5}\n\n
        5. Recuerda que puedes salir cuando quieras seleccionando la opcion 5.\n"""
        print(enunciado.format(nivel, pregunta, opcionUno, opcionDos, opcionTres, opcionCuatro))

    def getPreguntaAleatoria(self):
        return self.preguntaAleatoria

################################################################################################################
class ValidacionRespuesta:
    def __init__(self):
        self.resultado = False
        self.respuestaCorrecta = ""
        self.respuestaSeleccionada = ""

    def validacion(self, preguntaAleatoria, respuestaJugador):
        self.respuestaCorrecta = preguntaAleatoria[6]
        self.respuestaSeleccionada = preguntaAleatoria[respuestaJugador]

        if self.respuestaCorrecta == self.respuestaSeleccionada:
            self.resultado = True

    def mostrarResultado(self):
        
        if self.resultado:
            print("\nEnhorabuena la respuesta es correcta!!!\n")
        else:
            print("\nLa respuesta es incorrecta, pero no te desanimes puedes empezar una nueva partida!!!\n")
    
    def getResultado(self):
        return self.resultado

################################################################################################################    

