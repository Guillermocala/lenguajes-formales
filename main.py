import random
def union_listas(lista1, lista2):
    lista_resultado = set(lista1) | set(lista2)
    return lista_resultado

def diferencia_listas(lista1, lista2):
    lista_resultado = []
    for item in lista1:
        if item not in lista2:
            lista_resultado.append(item)
    return lista_resultado

def interseccion_listas(lista1, lista2):
    lista_resultado = []
    for item in lista1:
        if item in lista2:
            lista_resultado.append(item)
    return lista_resultado

def cerradura_alfabeto(lista, cant_palabras):
    lista_resultado = []
    for i in range(cant_palabras):
        palabra = ""
        for i in range(random.randint(2, 5)):
            palabra += str(lista[random.randint(0, len(lista) - 1)])
        if palabra not in lista_resultado:
            lista_resultado.append(palabra)
    return lista_resultado


lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "e", "i", "o", "u", 1, 2, 3]
print("lista1: ", lista1)
print("lista2: ", lista2)
print("Union: ", union_listas(lista1, lista2))
print("Diferencia(1-2): ", diferencia_listas(lista1, lista2))
print("Diferencia(2-1): ", diferencia_listas(lista2, lista1))
print("Interseccion: ", interseccion_listas(lista1, lista2))
cant_palabras = int(input("Ingrese la cantidad de palabras para la cerradura: "))
print("Cerradura: ", cerradura_alfabeto(lista1, cant_palabras))