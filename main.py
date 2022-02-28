from imp import load_source
from traceback import format_exception
from load import *
from piso_Lista import piso_Lista as pisoL
from showData import showData 


option = 0
option1 = False
text1= "Cargar XML"


# Temporal menu
while option != 3:
    print("\nPisos Artesanales S.A \n1. "+ text1 +" \n2. Seleccionar lista de pisos"
          + "\n3. Acciones con la lista de pisos")

    try:
        option = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Formato incorrecto\n")
        continue

    if option == 1:
        try:
            name = load.loadName()
            R = load.loadR()
            C = load.loadC()
            F = load.loadF()
            S = load.loadS()
            patron= load.loadPatron()
            patronName=load.loadPatronName()
            pisoLista = pisoL()
            for i in range(len(name)):
                pisoLista.insert(name[i].attrib['nombre'], R[i].text,C[i].text, F[i].text, S[i].text, patronName, patron)
            if pisoLista.len()>0:    
                option1 = True
                text1="Cargar nuevo XML"
            else:
                option1=False
                text1="Cargar XML"
        except:
            print("No se cargo el archivo")
            continue

    elif option == 2:
        if option1:
            show = showData(pisoLista)
            show.selectFloor()

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