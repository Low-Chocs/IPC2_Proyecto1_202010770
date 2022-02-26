from imp import load_source
from traceback import format_exception
from load import *
from piso_Lista import piso_Lista as pisoL
from showData import showData


option = 0
option1 = False


# Temporal menu
while option != 3:

    print("\nPisos Artesanales S.A \n1. Cargar XML \n2. Seleccionar lista y pisos"
          + "\n3. Acciones con los datos cargados")

    try:
        option = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Formato incorrecto\n")
        continue

    if option == 1:
        name = load.loadName()
        R = load.loadR()
        C = load.loadC()
        F = load.loadF()
        S = load.loadS()
        pisoLista = pisoL()
        for i in range(len(name)):
            pisoLista.insert(name[i].attrib['nombre'], R[i].text,C[i].text, F[i].text, S[i].text, "xd")
        option1 = True

    elif option == 2:
        if option1:
            showData.menu(pisoLista)

        else:
            print("No se ha cargado información")
    elif option == 3:
        print("Opción 3")
    elif option < 1:
        print("Ingrese un dato mayor o igual a 1")
    elif option > 3:
        print("Ingrese un dato menor o igual a 3")
        option = 0

print("Has salido, feliz día")
