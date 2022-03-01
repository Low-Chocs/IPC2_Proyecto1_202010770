from listaMatriz import*
from patron_Nodo import*

for i in range(0):
    print("xd")
prueba= patron_Nodo("50","WBBBWBWWW",3,3)


prueba.loadMatrix("WBBBWBWWWWWB", 4,3)
prueba.getMatrix().show()
prueba.getMatrix().fillDown()
prueba.getMatrix().fillLeft()
prueba.getMatrix().fillUp()