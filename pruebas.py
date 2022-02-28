from load import *
from listaPatron import *
palabra=""
patroncito=listaPatron()
name = load.loadName()
R = load.loadR()
C = load.loadC()
F = load.loadF()
S = load.loadS()
patronName=load.loadPatronName()

for i in range(len(name)):
    patron2= load.loadPatron(name[i].attrib['nombre']) 

    for j in range(len(patron2)):
        for k in range(len(patron2[j].text)):
            if patron2[j].text[k]!= " ":
                palabra+=patron2[j].text[k]
        if palabra!="" or palabra!= " ":
            print("He pasado")
            patroncito.insert(patronName[j].attrib['codigo'],palabra,5,12)
        palabra=""
    patroncito.show()
    patroncito.clean()

    print("Sali")


    

