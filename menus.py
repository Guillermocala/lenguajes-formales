def menu_principal():
    while True:
        print("""       Menu proncipal
            1-Alfabetos
            2-Lenguajes
            0-salir
        """)
        opcion = input("Ingrese la opcion: ")
        while not opcion.isdigit():
            print("Ingrese un numero!")
            opcion = input("Ingrese la opcion: ")

        match int(opcion):
            case 1:     "alfabetos"
                cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            case 2:     "lenguajes"
                cant_lenguajes = int(input("Ingrese la cantidad de lenguajes a ingresar: "))
            case 0:
                break
            case _:
                print("opcion invalida!")
                input("presione para continuar")


def menu_alfabetos():
    while True:
        print("""       Menu alfabetos
            1-Ingresar alfabeto
            2-Union alfabetos
            3-Diferencia alfabetos
            4-Interseccion alfabetos
            5-Cerradura estrella alfabeto
            6-Mostrar alfabetos
            0-salir
        """)
        opcion = input("Ingrese la opcion: ")
        while not opcion.isdigit():
            print("Ingrese un numero!")
            opcion = input("Ingrese la opcion: ")

        match int(opcion):
            case 1:     "ingresa"
                cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            case 2:     "union"
                cant_lenguajes = int(input("Ingrese la cantidad de lenguajes a ingresar: "))
            case 3:     "diferencia"
                pass
            case 4:     "interseccion"
                pass
            case 5:     "cerradura"
                pass
            case 6:     "mostrar"
                pass
            case 0:
                break
            case _:
                print("opcion invalida!")
                input("presione para continuar")

def menu_lenguajes():
    while True:
        print("""       Menu lenguajes
            1-Generar lenguaje
            2-Union lenguajes
            3-Diferencia lenguajes
            4-Interseccion lenguajes
            5-Concatenacion lenguajes
            6-Cerradura estrella lenguajes
            7-Inversa lenguaje
            8-Cardinalidad lenguaje
            6-Mostrar lenguajes
            0-salir
        """)
        opcion = input("Ingrese la opcion: ")
        while not opcion.isdigit():
            print("Ingrese un numero!")
            opcion = input("Ingrese la opcion: ")

        match int(opcion):
            case 1:     "generar"
                cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            case 2:     "union"
                cant_lenguajes = int(input("Ingrese la cantidad de lenguajes a ingresar: "))
            case 3:     "diferencia"
                pass
            case 4:     "interseccion"
                pass
            case 5:     "concatenacion"
                pass
            case 6:     "cerradura"
                pass
            case 7:     "inversa"
                pass
            case 8:     "cardinalidad"
                pass
            case 0:
                break
            case _:
                print("opcion invalida!")
                input("presione para continuar")