from tkinter import W
from nodoMatriz import *
import os 
import webbrowser 
import graphviz


class listaMatriz:
    def __init__(self, row, column):
        self.head = None
        self.bottom = None
        self.size = 0
        self.row = row
        self.column = column

    def insert(self, color, posX, posY):

        newNode = nodoMatriz(color, posX, posY)
        self.size += 1

        if self.head is None:
            self.head = newNode
            self.bottom = newNode
        else:
            self.bottom.setRight(newNode)
            self.bottom = newNode
    #Para mostrar los datos de manera matricial
    def show(self):
        printer = self.head
        for i in range(self.size):
            print("\nMatriz de colores\nColor del piso: " + printer.getColor()
                  + "\nPosición en x: " +
                  str(printer.getPosX())+"\nPosición en y: "
                  + str(printer.getPosY()))
            printer = printer.getRight()
    #Para mostrar los patrones de manera sencilla
    def show2(self):
        printer = self.head
        chain=""
        for i in range(self.size):
            chain+=printer.getColor()
            printer = printer.getRight()
        return chain
    #La función para encontrar el color en una posición exacta
    def find(self, x, y):
        printer = self.head
        if printer!=None and printer.getRight()!=None:
            for i in range(self.size):
                if printer.getPosX() == x:
                    if printer.getPosY() == y:
                        #print("Se ha encontrado el color: "+printer.getColor() + " en la pos en x: "+str(printer.getPosX())
                             # + " y en la pos en y: " + str(printer.getPosY()))
                        return printer
                printer = printer.getRight()
        else:
            return None
    #Para llenar abajo
    def fillDown(self):
        printer = self.head
        for i in range(int(self.row)):
            for j in range(int(self.column)):
                if self.find(i+1,j)!=  None:
                    printer.setDown(self.find(i+1, j))
                    #print("Nodo principal es: "+printer.getColor()+" "+str(i)+" "+str(j) +
                    #" Apunta hacia:" + printer.getDown().getColor()+" "+str(printer.getDown().getPosX())
                    #+" "+str(printer.getDown().getPosY()))
                printer = printer.getRight()
    #Llenar el anterior
    def fillLeft(self):
        printer = self.head
        for i in range(int(self.row)):
            for j in range(int(self.column)):
                if self.find(i,j-1)!=None:
                    printer.setLeft(self.find(i,j-1))
                    #print("Nodo principal es: "+printer.getColor()+" "+str(i)+" "+str(j) +
                   # " Apunta hacia la izquierda:" + printer.getLeft().getColor()+" "+str(printer.getLeft().getPosX())
                    #+" "+str(printer.getLeft().getPosY()))
                printer = printer.getRight()
    #Llenar arriba
    def fillUp(self):
        printer = self.head
        for i in range(int(self.row)):
            for j in range(int(self.column)):
                a=self.find(i-1,j)
                if self.find(i-1,j)!=None:
                    printer.setUp(a)
                    #print("Nodo principal es: "+printer.getColor()+" "+str(i)+" "+str(j) +
                    #" Apunta hacia la arriba:" + printer.getUp().getColor()+" "+str(printer.getUp().getPosX())
                    #+" "+str(printer.getUp().getPosY()))
                printer = printer.getRight()
    #Para obtener la cantidad de filas 
    def lenX(self):
        return self.row
    #Para obtener una cantidad de  columnas
    def lenY(self):
        return self.column