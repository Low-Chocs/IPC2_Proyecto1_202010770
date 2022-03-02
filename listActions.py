class listActions:
    def __init__(self, patternsList):
        self.patternsList=patternsList
        self.option=0
        self.option2=0

    def menu(self):
        while self.option!=3:
            self.option=int(input("\nSeleccione una acción: \n1.Grafica de Pisos \n2.Cambiar a un nuevo patrón \n3.Regresar\n"))
            if self.option==1:
                matrix=self.showGrhapiz()
                
            elif self.option==2:
                self.newPattern()
            elif self.option<1:
                print("Elije un número mayor a 1")
            elif self.option>3:
                print("Elije un valor menor a 3")

    def showGrhapiz(self):
        try:
            self.patternsList.showMenu()
            self.option2=int(input("Seleccione una opción:\n"))
            matriz=self.patternsList.newList(self.option2)
            matriz.show()
            return matriz
        except:
            print("No se logro cargar la lista")
            self.showGrhapiz()
    def newPattern(self):
        print("Aquí se haran los movimientos")