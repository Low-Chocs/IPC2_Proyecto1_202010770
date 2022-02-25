from nodo_Piso import nodo_Piso as floor

class piso_Lista:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, floorName, row, column, flip, swap, patron_List):

        newFloor=floor(floorName, row, column, flip, swap, patron_List)
        print(newFloor)
        self.size+=1

        if self.head is None:
            self.head =newFloor
            self.bottom= newFloor
        else:
            self.bottom.setNext(newFloor)
            self.bottom= newFloor
    
    def show(self):
        printer= self.head
        for i in range(self.size):
            print("Lista de pisos\nNombre del piso: "+ printer.getFloorName()
            +"\nCon un numero de filas de: "+ printer.getRow()+"\nCon un numero de columnas de: "
            +printer.getColumn()+"\nCon un coste de volteo de: "+printer.getFlip()+"\nCon un coste de"
            +" intercambio de: "+printer.getSwap())
            printer= printer.getNext()

    #To do list
    def sort(self):
        sorter=self.head
        nextNode = None
        aux= None
        if self.size== 1:
            print("Solo tienes un elemento en la lista")
    
        for i in range(self.size):
            print("Holaaa")
            if sorter.getNext != None:
                for j in range(self.size-2):
                    print("No entre")
                    if sorter.getFloorName()>nextNode.getFloorName():
                        sorter = aux
                        nextNode= sorter
                        sorter = aux
                    nextNode= sorter.getNext()
                sorter = sorter.getNext()
                    


