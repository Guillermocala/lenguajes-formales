class Padre:
    def __init__(self):
        self.lista = []

    def add_lista(self, item):
        self.lista.append(item)

    def set_lista(self, lista):
        self.lista = lista

    def union(self, lista1, lista2):
        lista_resultado = set(lista1) | set(lista2)
        return lista_resultado
    
    def diferencia(self, lista1, lista2):
        lista_resultado = []
        for item in lista1:
            if item not in lista2:
                lista_resultado.append(item)
        return lista_resultado
        
    def interseccion(self, lista1, lista2):
        lista_resultado = []
        for item in lista1:
            if item in lista2:
                lista_resultado.append(item)
        return lista_resultado


class Alfabetos(Padre):
    def cerradura(self, lista, cant_palabras):
        lista_resultado = []
        for i in range(cant_palabras):
            palabra = ""
            for i in range(random.randint(2, 5)):
                palabra += str(lista[random.randint(0, len(lista) - 1)])
            if palabra not in lista_resultado:
                lista_resultado.append(palabra)
        return lista_resultado