import funciones
import Clases

opcionCorrecta = False
continuar = True
while(continuar):
    while(not opcionCorrecta):
        Clases.Menu.menuInicial()
        opcion = int(input("Seleccione una opcion: "))

        if opcion < 1 or opcion > 3:
            print("Opcion incorrecta, ingrese una opcion nuevamente")
        elif opcion == 1:

            opcionCorrecta = False
            continuar = True
            while(continuar):
                while(not opcionCorrecta):

                    funciones.limpiarPantalla()
                    Clases.Menu.menuNuevoJuego()
                    opcion = int(input("Seleccione una opcion: "))
                    
                    if opcion < 1 or opcion > 3:
                        print("Opcion incorrecta, ingrese una opcion nuevamente")
                    elif opcion == 1:
                        

        elif opcion == 2:
            pass
        elif opcion == 3:
            print("Gracias por jugar!!")
            continuar = False
            break


        funciones.limpiarPantalla()