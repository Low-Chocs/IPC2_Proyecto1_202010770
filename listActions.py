from textList import *
class listActions:

    def __init__(self, patternsList):
        self.patternsList=patternsList
        self.option=0
        self.option2=0
        self.textFlip=textList()
        self.textLowerPrice= textList()
        self.Total=0

    def menu(self):
        while self.option!=3:
            self.option=int(input("\nSeleccione una acción: \n1.Grafica de Pisos \n2.Cambiar a un nuevo patrón \n3.Regresar\n"))
            
            if self.option==1:
                matrix=self.showGrhapiz()
                matrix.graphviz()
                
            elif self.option==2:

                self.newPattern()
            elif self.option<1:
                print("Elije un número mayor a 1")
            elif self.option>3:
                print("Elije un valor menor a 3")

    def showGrhapiz(self):
        try:
            self.patternsList.showMenu()
            self.option2=int(input("Seleccione una opción:\n"))
            matriz=self.patternsList.newList(self.option2)
            return matriz
        except:
            print("No se logro cargar la lista")
            self.showGrhapiz()
            
    def newPattern(self):
        array=self.patternsList.newList(1)
        self.patternsList.showMenu()
        self.option2=int(input("Seleccione una opción:\n"))
        array2=self.patternsList.newList(self.option2)
        array3=self.patternsList.newList(1)
        array4=self.patternsList.newList(self.option2)

        if self.differences(array,array2):
            self.economicList(array3,array4)
            array3.show()
            



    #Function to make all  flips possible
    def allFlips(self, array, array2):
        total=0
        for i in range(int(array.lenX())):
            for j in range(int(array.lenY())):
                if array.find(i, j).getColor()!=array2.find(i,j).getColor():
                    aux=array.find(i, j).getColor()
                    array.find(i, j).setColor(array2.find(i,j).getColor())
                    total+=int(self.patternsList.getFlip())
                    self.textFlip.insert("Posición en x: "+ str(i) +" Posición en y: "+ str(j)
                    +"De color: "+aux+" se volteo y tiene el color de: "+array.find(i, j).getColor()) 
        print("Total a pagar: "+str(total))       
        return total

    def flip(self,array,array2,i,j):
        aux=array.find(i, j).getColor()
        array.find(i, j).setColor(array2.find(i,j).getColor())
        self.textLowerPrice.insert("Posición en x: "+ str(i) +" Posición en y: "+ str(j)
        +"De color: "+aux+" se volteo y tiene el color de: "+array.find(i, j).getColor())
        return int(self.patternsList.getFlip())

    def swapX(self,array,i,j):
        aux=array.find(i, j).getColor()
        array.find(i, j).setColor(array.find(i, j+1).getColor())
        self.textLowerPrice.insert("Posición en x: "+ str(i) +" Posición en y: "+ str(j)
        +"De color: "+aux+" se intercambio y tiene el color de: "+array.find(i, j).getColor())
        return int(self.patternsList.getSwap())

    def swapY(self,array,i,j):
        aux=array.find(i, j).getColor()
        array.find(i, j).setColor(array.find(i+1, j).getColor())
        self.textLowerPrice.insert("Posición en x: "+ str(i) +" Posición en y: "+ str(j)
        +"De color: "+aux+" se intercambio y tiene el color de: "+array.find(i, j).getColor())
        return int(self.patternsList.getSwap())
        

    #Function that compares if the arrays are different
    def differences(self, array, array2):
        movements=0
        isDifferent =True
        for i in range(int(array.lenX())):
            for j in range(int(array.lenY())):
                if array.find(i, j).getColor()!=array2.find(i,j):
                    movements+=1
        if movements==0:
            isDifferent==False
        return isDifferent
    
    def economicList(self, array, array2):
        total=0
        for i in range(int(array.lenX())):
            for j in range(int(array.lenY())):
                if array.find(i, j).getColor()!=array2.find(i,j).getColor():
                    if 2 *int(self.patternsList.getFlip())>int(self.patternsList.getSwap()):
                        if array.find(i, j+1) is not None and array.find(i,j) is not None:
                            if array.find(i, j+1).getColor()== array2.find(i, j).getColor():
                                total+=self.swapX(array, i, j)
                        elif array.find(i+1, j) is not None and array.find(i,j) is not None:
                            if array.find(i+1, j).getColor()==array2.find(i, j).getColor():
                                total+=self.swapY(array, i, j)
                        else:
                            total+=self.flip(array,array2,i,j)
                    else:
                            total+=self.flip(array,array2,i,j)
        self.textLowerPrice.show()
        print("El total es de: "+ str(total))

    
        

