import csv
import random

def menuPrincipal(ListaDePreguntasClasificadasPorNivel):

    opcionCorrecta = False
    while(not opcionCorrecta):
        print("============= Menu principal =============")
        print("1. Iniciar Juego")
        print("2. Salir del Juego")
        print("============================================")

        opcion = int(input("Seleccione una opcion: "))
    
        if opcion < 1 or opcion > 2:
            print("Opcion incorrecta, ingrese una opcion nuevamente")
        elif opcion == 2:
            print("Gracias por jugar!!")
            break
        else:
            Preguntas(ListaDePreguntasClasificadasPorNivel)

            opcionCorrecta = True

def Preguntas(ListaDePreguntasClasificadasPorNivel):
    nivelDeDificultad = len(ListaDePreguntasClasificadasPorNivel)
    for nivel in range(nivelDeDificultad):
        listaPreguntasPorNivel = ListaDePreguntasClasificadasPorNivel[nivel]
        pregunta = seleccionPreguntaRandom(listaPreguntasPorNivel)
        mostrarPregunta(pregunta)
        print(pregunta)
        opcion = int(input("Seleccione una opcion: "))
        esSiguienteNivel = validaRespuesta(pregunta, opcion)
        if not esSiguienteNivel:
            break
    print("Enhorabuena, has logrado superar todas las preguntas!!!")


def validaRespuesta(pregunta, opcion):
    respuestaCorrecta = pregunta[6]
    respuestaUsuario = pregunta[opcion + 1]
    esRespuestaCorrecta = False
    if respuestaCorrecta == respuestaUsuario:
        esRespuestaCorrecta = True
    print(respuestaCorrecta)
    print(respuestaUsuario)
    return esRespuestaCorrecta

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

            if Nivel == 'Nivel 1':
                preguntasNivelUno.append(Pregunta)
            elif Nivel == 'Nivel 2':
                preguntasNivelDos.append(Pregunta)
            elif Nivel == 'Nivel 3':
                preguntasNivelTres.append(Pregunta)
            elif Nivel == 'Nivel 4':
                preguntasNivelCuatro.append(Pregunta)
            elif Nivel == 'Nivel 5':
                preguntasNivelCinco.append(Pregunta)

    ListaDePreguntasClasificadasPorNivel = [preguntasNivelUno, preguntasNivelDos, preguntasNivelTres, preguntasNivelCuatro, preguntasNivelCinco]
    return ListaDePreguntasClasificadasPorNivel

def mostrarPregunta(preguntaYRespuestas):

    nivel = preguntaYRespuestas[0]
    pregunta = preguntaYRespuestas[1]
    opcionUno = preguntaYRespuestas[2]
    opcionDos = preguntaYRespuestas[3]
    opcionTres = preguntaYRespuestas[4]
    opcionCuatro = preguntaYRespuestas[5]
    enunciado = "\nResponde esta pregunta correspondiente al {0} para pasar a la siguiente ronda. La pregunta es:\n\n {1}\n1. {2}\n2. {3}\n3. {4}\n4. {5}\n"
    print(enunciado.format(nivel, pregunta, opcionUno, opcionDos, opcionTres, opcionCuatro))



def seleccionPreguntaRandom(listaPreguntasPorNivel):

    numeroDePreguntas = len(listaPreguntasPorNivel)
    numeroRandom = random.randrange(numeroDePreguntas)
    preguntaRandom = listaPreguntasPorNivel[numeroRandom]

    return preguntaRandom

