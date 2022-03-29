#base algorítmica para el proyecto
import os
def ingresar_lista(cantidad):
    lista_resultante = []
    for item in range(cantidad):
        cadena = input("{}- Ingrese los elementos separados por comas: ".format(item + 1))
        lista_aux = cadena.split(',')
        lista_resultante.append(lista_aux)
    return lista_resultante

alfabetos = []
lenguajes = []

while True:
    os.system("cls")
    print("""
        1-ingresa alfabeto
        2-ingresa lenguaje
        3-mostrar
        0-salir
    """)
    opcion = int(input("Ingrese la opcion: "))
    match opcion:
        case 1:
            cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            alfabetos = ingresar_lista(cant_alfabetos)
        case 2:
            cant_lenguajes = int(input("Ingrese la cantidad de lenguajes a ingresar: "))
            lenguajes = ingresar_lista(cant_lenguajes)
        case 3:
            print("alfabetos...", alfabetos)
            print("lenguajes...", lenguajes)
            input("presione para continuar")
        case 0:
            break
        case _:
            print("opcion invalida!")
            input("presione para continuar")

