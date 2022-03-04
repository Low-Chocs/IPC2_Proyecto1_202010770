from textList import *
import graphviz
class listActions:

    def __init__(self, patternsList):
        self.patternsList=patternsList
        self.option=0
        self.option2=0
        self.textLowerPrice=textList()
        self.textLowerPrice2= textList()
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

        if self.differences(array,array2):
            self.economicList3(array,array2)
            array=self.patternsList.newList(1)
            array2=self.patternsList.newList(self.option2)
            self.economicList4(array,array2)
        else:
            print("Elije un patrón diferente")
            self.newPattern
            



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
        +" De color: "+aux+" se volteo y tiene el color de: "+array.find(i, j).getColor())
        return int(self.patternsList.getFlip())

    def swapX(self,array,i,j):
        aux=array.find(i, j).getColor()
        array.find(i, j).setColor(array.find(i, j+1).getColor())
        array.find(i, j+1).setColor(aux)
        self.textLowerPrice.insert("Posición en x: "+ str(i) +" Posición en y: "+ str(j)
        +" De color: "+aux+" se intercambio y tiene el color de: "+array.find(i, j).getColor())
        return int(self.patternsList.getSwap())

    def swapY(self,array,i,j):
        aux=array.find(i, j).getColor()
        array.find(i, j).setColor(array.find(i+1, j).getColor())
        array.find(i+1, j).setColor(aux)
        self.textLowerPrice.insert("Posición en x: "+ str(i) +" Posición en y: "+ str(j)
        +" De color: "+aux+" se intercambio y tiene el color de: "+array.find(i, j).getColor())
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
    
    def economicList3(self, array, array2):
        total=0

        for p in range(int(array.lenX())):
            for l in range(int(array.lenY())):
                if array.find(p, l).getColor()!=array2.find(p,l).getColor():
                    if 2 *int(self.patternsList.getFlip())>=int(self.patternsList.getSwap()):
                        if array.find(p, l+1) is not None and array.find(p, l).getColor()!=array2.find(p,l).getColor()  and array.find(p, l).getColor()== array2.find(p, l+1).getColor():
                            if array.find(p, l+1).getColor()== array2.find(p, l).getColor():
                                total+=self.swapX(array, p, l)
                        if array.find(p+1, l) is not None:
                            if array.find(p+1, l).getColor()==array2.find(p, l).getColor() and array.find(p, l).getColor()== array2.find(p+1, l).getColor():
                                total+=self.swapY(array, p, l)

        for i in range(int(array.lenX())):
            for j in range(int(array.lenY())):
                if array.find(i, j).getColor()!=array2.find(i,j).getColor():
                    if 2 *int(self.patternsList.getFlip())>=int(self.patternsList.getSwap()):
                        if array.find(i, j+1) is not None:
                            if array.find(i, j+1).getColor()== array2.find(i, j).getColor():
                                total+=self.swapX(array, i, j)
                        if array.find(i+1, j) is not None and array.find(i, j).getColor()!=array2.find(i,j).getColor():
                            if array.find(i+1, j).getColor()==array2.find(i, j).getColor():
                                total+=self.swapY(array, i, j)

        for k in range(int(array.lenX())):
            for h in range(int(array.lenY())):
                if array.find(k, h).getColor()!=array2.find(k,h).getColor():
                    total+=self.flip(array,array2,k,h)
        self.textLowerPrice.show()
        print("El total es de: "+ str(total))
    
    def economicList4(self, array, array2):
        total=0

        for i in range(int(array.lenX())):
            for j in range(int(array.lenY())):
                if array.find(i, j).getColor()!=array2.find(i,j).getColor():
                    if 2 *int(self.patternsList.getFlip())>=int(self.patternsList.getSwap()):
                        if array.find(i+1, j) is not None:
                            if array.find(i+1, j).getColor()==array2.find(i, j).getColor() and array.find(i, j).getColor()== array2.find(i+1, j).getColor():
                                total+=self.swapY(array, i, j)
                        if array.find(i, j+1) is not None and array.find(i, j).getColor()!=array2.find(i,j).getColor()  and array.find(i, j).getColor()== array2.find(i, j+1).getColor():
                            if array.find(i, j+1).getColor()== array2.find(i, j).getColor():
                                total+=self.swapX(array, i, j)


        for l in range(int(array.lenX())):
            for p in range(int(array.lenY())):
                if array.find(l, p).getColor()!=array2.find(l,j).getColor():
                    if 2 *int(self.patternsList.getFlip())>=int(self.patternsList.getSwap()):
                        if array.find(l+1, p) is not None:
                            if array.find(l+1, p).getColor()==array2.find(l, p).getColor():
                                total+=self.swapY(array, l, p)
                        if array.find(l, p+1) is not None and array.find(l, p).getColor()!=array2.find(l,p).getColor():
                            if array.find(l, p+1).getColor()== array2.find(l, p).getColor():
                                total+=self.swapX(array, l, p)
            
        for k in range(int(array.lenX())):
            for h in range(int(array.lenY())):
                if array.find(k, h).getColor()!=array2.find(k,h).getColor():
                    total+=self.flip(array,array2,k,h)
        self.textLowerPrice.show()
        print("El total es de: "+ str(total))

    
        

