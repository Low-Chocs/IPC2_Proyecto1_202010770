from load import * 

name = load.loadName()
R = load.loadR()
C = load.loadC()
F = load.loadF()
S = load.loadS()

for i in range(len(name)):
    print(name[i].attrib['nombre'])
    print(R[i].text)
    print(C[i].text)
    print(F[i].text)
    print(S[i].text)