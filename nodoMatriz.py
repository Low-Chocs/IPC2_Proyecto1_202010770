class nodoMatriz:
    def __init__(self, color, posX,posY):
        self.up=None
        self.down=None
        self.right=None
        self.down=None
        self.posX=posX
        self.posY=posY
        self.color=color

    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY

    def getColor(self):
        return self.color
    
    def setX(self,posX):
        self.posX=posX
        return self.x
    
    def setY(self,posY):
        self.posY=posY
        return self.posY

    def setColor(self, color):
        self.color=color
        return self.color

    def getUp(self):
        return self.up
    
    def getDown(self):
        return self.down

    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def setUp(self,up):
        self.up=up
        return self.up
    
    def setDown(self, down):
        self.down=down
        return self.down

    def setRight(self, right):
        self.right=right
        return self.right
    
    def setLeft(self, left):
        self.left=left
        return self.left

    

