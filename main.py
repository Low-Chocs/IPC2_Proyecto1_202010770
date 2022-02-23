from traceback import format_exception


option=0

#Este menú es temporal
while option!=4:
    print("El gran menú \n1. Cargar información \n 2. Mostrar patrón"
    +"\n 3. Cambiar patrón \n 4. Salir")

    try:
        option = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Formato incorrecto\n")
        continue

    if option == 1:
        print("Opción 1")
    elif option==2:
        print("Opción 2")
    elif option==3:
        print("Opción 3")
    elif option<1:
        print("Ingrese un dato mayor o igual a 1")
    elif option>4:
        print("Ingrese un dato menor o igual a 4")

print("Has salido, feliz día")