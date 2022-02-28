from listaPatron import listaPatron as newPatron
class nodo_Piso:
    def __init__(self, floorName, row, column, flip, swap, listaPiso):
        self.floorName = floorName
        self.row = row
        self.column= column
        self.flip=flip
        self.swap=swap
        self.next= None
        self.listaPiso : newPatron= listaPiso
    
    def getList(self):
        return self.listaPiso

    def getNext(self):
        return self.next
    
    def getFloorName(self):
        return self.floorName

    def getRow(self):
        return str(self.row)
    
    def getColumn(self):
        return str(self.column)
    
    def getFlip(self):
        return str(self.flip)
    
    def getSwap(self):
        return str(self.swap)

    def setNext(self, next):
        self.next : nodo_Piso =next
        return self.next

    def setFloorName(self, floorName):
        self.floorName = floorName
        return self.floorName
    
    def setRow(self, row):
        self.row = row
        return self.row
    
    def setColumn(self, column):
        self.column = column
        return self.column

    def setFlip(self, flip):
        self.flip = flip
        return self.flip
    
    def setFlip(self, flip):
        self.flip = flip
        return self.flip
    
    def setSwap(self, swap):
        self.swap = swap
        return self.swap
    