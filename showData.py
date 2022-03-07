#Se busca entre la lista de pisos para devoler una lista de patrones
from piso_Lista import piso_Lista as pisoLista
class showData:
    def __init__(self, pisoList):
        self.pisoList= pisoList

    def selectFloor(self):
        self.pisoList.showMenu()
        option = int(input("\nSeleccione una opción\n"))
        if option==0:
            print("\nHas regresado al menú")
        else:
            piso = self.pisoList.newList(option)
            try:
                return piso
            except:
                print("No se pudo cargar el piso seleccionado")
                self.selectFloor()