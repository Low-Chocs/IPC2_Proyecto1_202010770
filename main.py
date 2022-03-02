from imp import load_source
from traceback import format_exception
from load import *
from piso_Lista import piso_Lista as pisoL
from showData import showData
from listaPatron import *
from listActions import *


option = 0
option1 = False
option2 = False
text1 = "Cargar XML"
patron = listaPatron()
palabra = ""


# Temporal menu
while option != 4:
    print("\nPisos Artesanales S.A \n1. " + text1 + " \n2. Seleccionar lista de pisos"
          + "\n3. Acciones con la lista de pisos"+"\n4. Salir")

    try:
        option = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Formato incorrecto\n")
        continue

    if option == 1:
        pisoLista = pisoL()
        #try:
        name = load.loadName()
        R = load.loadR()
        C = load.loadC()
        F = load.loadF()
        S = load.loadS()
        patronName = load.loadPatronName()

        for i in range(len(name)):
            patron = listaPatron()
            patron2 = load.loadPatron(name[i].attrib['nombre'])

            for j in range(len(patron2)):
                for k in range(len(patron2[j].text)):
                    if patron2[j].text[k] != " " and patron2[j].text[k] != "\n":
                            palabra += patron2[j].text[k]
                            
                if palabra != "" and palabra != " ":
                        patron.insert(patronName[j].attrib['codigo'], palabra, R[i].text, C[i].text, F[i].text, S[i].text)
                palabra = ""
            pisoLista.insert(name[i].attrib['nombre'], R[i].text, C[i].text, F[i].text, S[i].text, patron)

        if pisoLista.len() > 0:
            option1 = True
            print("Se ha cargado exitosamente el XML")
            text1 = "Cargar nuevo XML"
        else:
            option1 = False
            text1 = "Cargar XML"
        """except:
            print("No se cargo el archivo")
            continue"""

    elif option == 2:
        if option1:
            show = showData(pisoLista)
            piso = show.selectFloor()

            if piso.len() > 0:
                print("\nUsted ha seleccionado: \n")
                piso.show()
                option2 = True

        else:
            print("No se ha cargado información")
    elif option == 3:
        if option1 and option2:
            option3 = listActions(piso)
            option3.menu()
        else:
            print("No se ha seleccionado una lista")

    elif option < 1:
        print("Ingrese un dato mayor o igual a 1")
    elif option > 4:
        print("Ingrese un dato menor o igual a 4")
        option = 0

print("Has salido, feliz día")
