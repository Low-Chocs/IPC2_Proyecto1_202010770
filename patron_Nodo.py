class patron_Nodo:
    def patron_Nodo(self, name, matriz):
        self.name= name
        self.matriz= matriz
        self.next= None

    def getNext(self):
        return self.next

    def getName(self):
        return self.name

    def getMatriz(self):
        return self.matriz

    def setNext(self, next):
        self.next= next
        return self.next
    
    def setName(self, name):
        self.name= name
        return self.name
    
    def setMatriz(self, matriz):
        self.matriz= matriz
        return self.matriz
