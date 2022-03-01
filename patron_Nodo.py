from listaMatriz import *

class patron_Nodo:
    def __init__(self, code, cadena, row, column):
        self.code = code
        self.cadena = cadena
        self.row = row
        print(row)
        self.column = column
        print(column)
        self.next = None
        self.matrix = listaMatriz(row,column)
        self.loadMatrix(cadena,row,column)
        self.matrix.show()


    def getNext(self):
        return self.next

    def getCode(self):
        return self.code

    def getMatriz(self):
        return self.matriz

    def getCadena(self):
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

    

    def loadMatrix(self, chain, x, y):
        print("CADENA"+chain)
        for i in range(int(x)):
            for j in range(int(y)):
                self.matrix.insert(chain[j], i, j)

        self.matrix.fillDown()
        self.matrix.fillLeft()
        self.matrix.fillUp()
