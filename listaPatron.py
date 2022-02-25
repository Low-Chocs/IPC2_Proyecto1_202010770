from patron_Nodo import patron_Nodo as patron

class listaPatron:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, name, matriz):

        nuevoPatron=patron(name, matriz)
        self.size+=1

        if self.head is None:
            self.head =nuevoPatron
            self.bottom= nuevoPatron
        else:
            self.bottom.setNext(nuevoPatron)
            self.bottom= nuevoPatron