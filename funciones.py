import csv
import random

def clasificarListaPreguntas():
    preguntasNivelUno = []
    preguntasNivelDos = []
    preguntasNivelTres = []
    preguntasNivelCuatro = []
    preguntasNivelCinco = []

    with open(r'preguntas.txt', mode='r') as preguntas:
        listaPreguntas = csv.reader(preguntas, delimiter = ';')
        for Pregunta in listaPreguntas:

            Nivel = Pregunta[0]

            if Nivel == 'Nivel_1':
                preguntasNivelUno.append(Pregunta)
            elif Nivel == 'Nivel_2':
                preguntasNivelDos.append(Pregunta)
            elif Nivel == 'Nivel_3':
                preguntasNivelTres.append(Pregunta)
            elif Nivel == 'Nivel_4':
                preguntasNivelCuatro.append(Pregunta)
            elif Nivel == 'Nivel_5':
                preguntasNivelCinco.append(Pregunta)

    return preguntasNivelUno, preguntasNivelDos, preguntasNivelTres, preguntasNivelCuatro, preguntasNivelCinco  

def seleccionPreguntaRandom(listaPreguntasPorNivel):

    numeroDePreguntas = len(listaPreguntasPorNivel)
    numeroRandom = random.randrange(numeroDePreguntas)
    preguntaRandom = listaPreguntasPorNivel[numeroRandom]

    return preguntaRandom

