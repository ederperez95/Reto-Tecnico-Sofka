import csv
import random
import os


def menuInicioSesion():
    opcionCorrecta = False
    continuar = True
    while(continuar):
        while(not opcionCorrecta):
            print("============= Menu principal =============")
            print("1. Iniciar sesion")
            print("2. Crear cuenta")
            print("3. Salir del Juego")
            print("============================================")

            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 2:
                print("Opcion incorrecta, ingrese una opcion nuevamente")
            elif opcion == 2:
                print("Gracias por jugar!!")
                continuar = False
                break
            else:
                limpiarPantalla() 
                Preguntas(ListaDePreguntasClasificadasPorNivel)

            limpiarPantalla()    


def menuInicioDeJuego(ListaDePreguntasClasificadasPorNivel):

    opcionCorrecta = False
    continuar = True
    while(continuar):
        while(not opcionCorrecta):
            limpiarPantalla()
            print("============= Menu principal =============")
            print("1. Nuevo Juego")
            print("2. Cerrar sesion")
            print("3. Salir del Juego")
            print("============================================")

            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 2:
                print("Opcion incorrecta, ingrese una opcion nuevamente")
            elif opcion == 3:
                print("Gracias por jugar!!")
                continuar = False
                break
            else:
                limpiarPantalla() 
                Preguntas(ListaDePreguntasClasificadasPorNivel)

            limpiarPantalla()   

def Preguntas(ListaDePreguntasClasificadasPorNivel):

    nivelDeDificultad = len(ListaDePreguntasClasificadasPorNivel)
    banderaEsGanadorJuego = True

    for nivel in range(nivelDeDificultad):
        listaPreguntasPorNivel = ListaDePreguntasClasificadasPorNivel[nivel]
        pregunta = seleccionPreguntaRandom(listaPreguntasPorNivel)
        mostrarPregunta(pregunta)
        print("5. Recuerda que puedes salir cuando desees con esta opcion. \n")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 5:
            banderaEsGanadorJuego = False
            break
        else:
            esSiguienteNivel = validaRespuesta(pregunta, opcion)
        if esSiguienteNivel:
            respuestaCorrecta()
        else: 
            respuestaIncorrecta()
            banderaEsGanadorJuego = False
            input("Presione cualquier tecla para continuar")
            limpiarPantalla()
            break
        
        limpiarPantalla()

    if banderaEsGanadorJuego:
        ganadorDelJuego()
        input("Presione cualquier tecla para continuar")

def respuestaIncorrecta():
    print("No es la respuesta correcta pero no te desanimes, Sigue intentado!!\n\n")

def respuestaCorrecta():
    print("La respuesta es correcta y pasaste de ronda, nos vemos en el proximo nivel!!")

def ganadorDelJuego():
    print("Enhorabuena, has logrado superar todas las preguntas!!!")

def validaRespuesta(pregunta, opcion):
    respuestaCorrecta = pregunta[6]
    respuestaUsuario = pregunta[opcion + 1]
    esRespuestaCorrecta = False
    if respuestaCorrecta == respuestaUsuario:
        esRespuestaCorrecta = True
    return esRespuestaCorrecta

def clasificarListaPreguntas():
    preguntasNivelUno = []
    preguntasNivelDos = []
    preguntasNivelTres = []
    preguntasNivelCuatro = []
    preguntasNivelCinco = []

    with open(r'preguntas.txt', mode='r', encoding='utf-8') as preguntas:
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

    enunciado = "\nPara pasar a la siguiente ronda responde la pregunta correspondiente al {0}. la pregunta a responder es:\n\n{1}\n\n1. {2}\n2. {3}\n3. {4}\n4. {5}\n"
    print(enunciado.format(nivel, pregunta, opcionUno, opcionDos, opcionTres, opcionCuatro))

def seleccionPreguntaRandom(listaPreguntasPorNivel):
    numeroDePreguntas = len(listaPreguntasPorNivel)
    numeroRandom = random.randrange(numeroDePreguntas)
    preguntaRandom = listaPreguntasPorNivel[numeroRandom]

    return preguntaRandom

def limpiarPantalla():
    os.system("cls")  