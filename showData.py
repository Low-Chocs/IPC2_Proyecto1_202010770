class showData:

    def show(this, pisoList):
        pisoList.show()
        this.menu(pisoList)

    def menu(pisoList):
        option=0
        #while option !=int(pisoList.len()):
        for i in range(pisoList.len()):
            print("\n"+str(i)+". Lista:"+str(i))