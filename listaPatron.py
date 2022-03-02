from patron_Nodo import *

class listaPatron:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, name, cadena, row, column,flip,swap):

        nuevoPatron=patron_Nodo(name, cadena, row, column,flip,swap)
        self.size+=1

        if self.head is None:
            self.head =nuevoPatron
            self.bottom= nuevoPatron
        else:
            self.bottom.setNext(nuevoPatron)
            self.bottom= nuevoPatron

    def show(self):
        printer= self.head
        print("\nLista de patrones")
        for i in range(self.size):
            print("\nCódigo del patrón de piso: "+ printer.getCode()+"\nCoste de volteo: "+printer.getFlip()
            +" Coste de cambio: "+printer.getSwap() +"\nCon un patrón: "+ printer.getCadena())
            printer= printer.getNext()

    def showMenu(self):
        printer= self.head
        print("\nPresione 0 para regresar")
        for i in range(self.size):
            print("\nOpción: "+str(i+1)+"\nCódigo del patrón de piso: "+ printer.getCode()+"\nCoste de volteo: "+printer.getFlip()
            +" Coste de cambio: "+printer.getSwap() +"\nCon un patrón: "+ printer.getCadena())
            printer= printer.getNext()

    def showMatrix(self):
        print("Seleccione un patrón: ")
        printer= self.head
        for i in range(self.size):
            printer.getMatrix().show()
            printer= printer.getNext()

    def len(self):
        return self.size

    def newList(self, option):
        new = self.head
        for i in range(self.size):
            print(option)
            if i+1==option:
                return new.getMatrix()
            print(new.getNext().getMatrix().show())
            new=new.getNext()
        print("No se encontro la lista")
    
    

    
    def clean(self):
        self.head =None
        self.bottom= None 
        self.size=0