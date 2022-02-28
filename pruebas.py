from load import * 
palabra=""
name = load.loadName()
R = load.loadR()
C = load.loadC()
F = load.loadF()
S = load.loadS()
patron= load.loadPatron()
patronName=load.loadPatronName()


for i in range(len(patron)):
    for j in range(len(patron[i].text)):
        if patron[i].text[j]!= " ":
            palabra+=patron[i].text[j]
    print(palabra)
    palabra=""

for i in range(len(patron)):
    print(patronName[i].attrib['codigo'])
    

