
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("============= Menu principal =============")
            print("1. Crear Jugador")
            print("2. Listar datos Jugador Completo")
            print("3. Listar  Jugador sin contraseña")
            print("4. Actualizar todo menos la puntuacion")
            print("5. Actualizar la puntuacion")
            print("6. Eliminar Jugador")
            print("7. Salir Jugador")
            print("============================================")

            opcion = int(input("Seleccione una opcion: "))
        
            if opcion < 1 or opcion > 7:
                print("Opcion incorrecta, ingrese nuevamente")
            elif opcion == 7:
                continuar = False
                print("Gracias por usar este sistema!!")
                break
            else:
                preguntasCategoriaUno, preguntasCategoriaDos, preguntasCategoriaTres, preguntasCategoriaCuatro, preguntasCategoriaCinco = funciones.clasificarListaPreguntas()

                opcionCorrecta = True

menuPrincipal()