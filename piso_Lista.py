from nodo_Piso import nodo_Piso as floor

class piso_Lista:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, floorName, row, column, flip, swap, patron_List):

        newFloor=floor(floorName, row, column, flip, swap, patron_List)
        self.size+=1

        if self.head is None:
            self.head =newFloor
            self.bottom= newFloor
        else:
            self.bottom.setNext(newFloor)
            self.bottom= newFloor
    
    def showMenu(self):
        printer= self.head
        print("\nLista de pisos: \nOpción 0: Regresar al menú principal")
        for i in range(self.size):
            print("\nOpción: "+str(i+1)+"\nNombre del piso: "+ printer.getFloorName()
            +"\nCon un numero de filas de: "+ printer.getRow()+"\nCon un numero de columnas de: "
            +printer.getColumn()+"\nCon un coste de volteo de: "+printer.getFlip()+"\nCon un coste de"
            +" intercambio de: "+printer.getSwap())
            
            printer.getList().show()
            printer= printer.getNext()    

    def show(self):
        printer= self.head
        for i in range(self.size):
            print("\nLista de pisos\nNombre del piso: "+ printer.getFloorName()
            +"\nCon un numero de filas de: "+ printer.getRow()+"\nCon un numero de columnas de: "
            +printer.getColumn()+"\nCon un coste de volteo de: "+printer.getFlip()+"\nCon un coste de"
            +" intercambio de: "+printer.getSwap()+" Contiene el piso con código de: ")
            printer.getList().show()
            printer= printer.getNext()

    def len(self):
        return self.size

    def newList(self, option):
        new = self.head
        for i in range(self.size):
            if i+1==option:
                return new.getList()
            new= new.getNext()
        print("No se encontro la lista")

    def clean(self):
        self.head =None
        self.bottom= None   
        self.size=0 

    def showMatrix(self):
        printer= self.head
        for i in range(self.size):
            printer.getList().showMatrix()
            printer=printer.getNext()



    #To do list
    """""
    def sort(self):
        sorter=self.head
        nextNode = sorter.getNext()
        aux= None
        if self.size== 1:
            print("Solo tienes un elemento en la lista")
    
        for i in range(self.size):
            print("Holaaa")
            self.show()
            if sorter.getNext() != None:
                
                for j in range(i,self.size):
                    print("No entre")
                    if sorter.getFloorName()>nextNode.getFloorName():
                        aux= sorter
                        sorter.setFloorName(sorter.getNext().getFloorName())
                        sorter.setRow(sorter.getNext().getRow())
                        sorter.setColumn(sorter.getNext().getNext())
                        sorter.setFlip(sorter.getNext().getFlip())
                        sorter.setSwap(sorter.getNext().getSwap())
                        sorter.setList(sorter.getNext().getList())

                        sorter.getNext().setFloorName(aux.getFloorName())
                        sorter.getNext().setRow(aux.getRow())
                        sorter.getNext().setColumn(aux.getNext())
                        sorter.getNext().setFlip(aux.getFlip())
                        sorter.getNext().setSwap(aux.getSwap())
                        sorter.getNext().setList(aux.getList())
                        sorter= sorter.getNext()
                        self.show()
                sorter = sorter.getNext()"""

