class textNode:
    def __init__(self, text):
        self.text=text
        self.next=None

    def getText(self):
        return self.text

    def getNext(self):
        return self.next
    
    def setNext(self,next):
        self.next=next