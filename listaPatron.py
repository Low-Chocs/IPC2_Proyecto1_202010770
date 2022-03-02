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
        for i in range(0,self.size):
            print("\nCódigo del patrón de piso: "+ printer.getCode()+"\nCoste de volteo: "+printer.getFlip()
            +" Coste de cambio: "+printer.getSwap() +"\nCon un patrón: "+ printer.getCadena())
            printer= printer.getNext()

    def showMatrix(self):
        printer= self.head
        for i in range(self.size):
            printer.getMatrix().show()
            printer= printer.getNext()
    def len(self):
        return self.size

    
    def clean(self):
        self.head =None
        self.bottom= None 
        self.size=0