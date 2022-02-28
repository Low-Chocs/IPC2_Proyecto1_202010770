from patron_Nodo import *

class listaPatron:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, name, cadena, row, column):

        nuevoPatron=patron_Nodo(name, cadena, row, column)
        self.size+=1

        if self.head is None:
            self.head =nuevoPatron
            self.bottom= nuevoPatron
        else:
            self.bottom.setNext(nuevoPatron)
            self.bottom= nuevoPatron

    def show(self):
        printer= self.head
        for i in range(self.size):
            print("\nLista de patrones\nCódigo del patrón de piso: "+ printer.getCode()
            +"\nCon un patrón: "+ printer.getCadena())
            printer= printer.getNext()
    
    def clean(self):
        self.head =None
        self.bottom= None 
        self.size=0