class patron_Nodo:
    def patron_Nodo(self, code, cadena, row, column):
        self.code= code
        self.cadena= cadena
        self.row= row 
        self.column=column
        self.matriz
        self.next= None


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
        self.next= next
        return self.next
    
    def setName(self, name):
        self.name= name
        return self.name
    
    def setMatriz(self, matriz):
        self.matriz= matriz
        return self.matriz
