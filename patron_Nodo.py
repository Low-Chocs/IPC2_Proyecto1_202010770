from listaMatriz import *

class patron_Nodo:
    def __init__(self, code, cadena, row, column,flip,swap):
        #print(self.cadena)
        self.code = code
        self.cadena = cadena
        print(self.cadena)
        self.row = row
        self.column = column
        self.next = None
        self.flip=flip
        self.swap=swap
        self.matrix = listaMatriz(row,column)
        self.loadMatrix(cadena,row,column)

    def getSwap(self):
        return self.swap
    
    def getFlip(self):
        return self.flip
    
    def setFlip(self, flip):
        self.flip=flip

    def setSwap(self, swap):
        self.swap=swap

    def getNext(self):
        return self.next

    def getCode(self):
        return self.code

    def getMatriz(self):
        return self.matriz

    def getCadena(self):
        print(self.cadena)
        return self.cadena

    def getColumn(self):
        return self.column

    def getRow(self):
        return self.row

    def setNext(self, next):
        self.next = next
        return self.next

    def setName(self, name):
        self.name = name
        return self.name

    def setMatrix(self, matrix):
        self.matrix = matrix
        return self.matrix

    def getMatrix(self):
        return self.matrix
    
    def printMatrix(self):
        self.matrix.show()

    

    def loadMatrix(self, chain, x, y):
        for i in range(int(x)):
            for j in range(int(y)):
                self.matrix.insert(chain[j], i, j)

        self.matrix.fillDown()
        self.matrix.fillLeft()
        self.matrix.fillUp()
