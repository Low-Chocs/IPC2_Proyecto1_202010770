#Lista para obtener y mostrar las instrucciones a seguir
from textNode import *

class textList:
    def __init__(self):
        self.head = None
        self.bottom = None
        self.size = 0

    def insert(self, text):

        newNode = textNode(text)
        self.size += 1

        if self.head is None:
            self.head = newNode
            self.bottom = newNode
        else:
            self.bottom.setNext(newNode)
            self.bottom = newNode

    def show(self):
        printer=self.head
        for i in range(self.size):
            print(printer.getText())
            printer=printer.getNext()

    def len(self):
        return self.size