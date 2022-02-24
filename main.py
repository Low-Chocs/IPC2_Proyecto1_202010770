from traceback import format_exception


option=0
option1=False
menuOutput=False

#Temporal menu
while option!=3 and option!=6:
    
    if not menuOutput:
        print("\nPisos Artesanales S.A \n1. Cargar información \n2. Seleccionar piso"
        +"\n3. Salir")

        try:
            option = int(input("Ingrese una opción\n"))
        except ValueError:
            print("Formato incorrecto\n")
            continue

        if option == 1:
            print("Opción 1")
            option1=True
        elif option==2:
            if option1:
                print("Opciones 2")
                menuOutput=True

            else:
                print("No se ha cargado información")
        elif option==3:
            print("Opción 3")
        elif option<1:
            print("Ingrese un dato mayor o igual a 1")
        elif option>3:
            print("Ingrese un dato menor o igual a 3")
            option =0

    else:
        while menuOutput and menuOutput!=6:
            print("\nPisos Artesanales S.A \n 1. Cargar nueva información \n 2. Seleccionar nuevos patrones"
            +"\n 3. Costo Mínimo \n 4. Mostrar las instrucciones a seguir" 
            +"\n 5. Mostrar el patrón resultante \n 6. Salir")

            try:
                option = int(input("Ingrese una opción\n"))
            except ValueError:
                print("Formato incorrecto\n")
                continue

            if option == 1:
                print("Opción 1")
                menuOutput=False
            elif option==2:
                print("Opciones 2")
            elif option==3:
                print("Opción 3")
            elif option==4:
                print("Opción 4")
            elif option==5:
                print("Opción 5")
            elif option==6:
                break
            elif option<1:
                print("Ingrese un dato mayor o igual a 1")
            elif option>6:
                print("Ingrese un dato menor o igual a 6") 
    if option!=6:            
        continue
print("Has salido, feliz día")

