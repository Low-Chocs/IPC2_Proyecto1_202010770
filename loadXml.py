from tkinter import N, filedialog
from lxml import etree as xp
route=""
class loadXml:
    def __init__(self):
        pass
    def loadName():
        global route
        route = filedialog.askopenfilename(title="Select A file")
        tree=xp.parse(route)
        pisos=tree.xpath('//piso')
        return pisos

    def loadR():
        tree=xp.parse(route)
        R=tree.xpath('//piso//R')
        return R

    def loadC():
        tree=xp.parse(route)
        C=tree.xpath('//piso//C')
        return C
    
    def loadF():
        tree=xp.parse(route)
        F=tree.xpath('//piso//F')
        return F
    
    def loadS():
        tree=xp.parse(route)
        S=tree.xpath('//piso//S')
        return S

    def loadPatronName():
        tree=xp.parse(route)
        patronName=tree.xpath('//patron')
        return patronName

    def loadPatron(nombre):
        tree=xp.parse(route)
        patron=tree.xpath('//piso[@nombre="'+nombre+'"]//patrones//patron')
        return patron