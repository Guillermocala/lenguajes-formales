import random
class Padre:
    def __init__(self):
        self.lista = []

    def add_item(self, item):
        self.lista.append(item)

    def get_item(self, indice):
            return self.lista[indice]

    def set_lista(self, lista):
        self.lista = lista
    
    def get_lista(self):
        return self.lista

    def union(self, indice1, indice2):
        lista_resultado = set(self.lista[indice1]) | set(self.lista[indice2])
        return list(lista_resultado)
    
    def diferencia(self, indice1, indice2):
        lista_resultado = []
        for item in self.lista[indice1]:
            if item not in self.lista[indice2]:
                lista_resultado.append(item)
        return lista_resultado
        
    def interseccion(self, indice1, indice2):
        lista_resultado = []
        for item in self.lista[indice1]:
            if item in self.lista[indice2]:
                lista_resultado.append(item)
        return lista_resultado


class Alfabetos(Padre):
    def cerradura(self, indice, cant_palabras):
        lista_resultado = []
        lista_objetivo = self.lista[indice]
        for i in range(cant_palabras):
            palabra = ""
            for i in range(random.randint(2, 5)):
                palabra += str(random.choice(lista_objetivo))
            if palabra not in lista_resultado:
                lista_resultado.append(palabra)
        return lista_resultado


class Lenguajes(Padre):
    def generar(self, lista, cant_palabras):
        lista_resultado = []
        for i in range(cant_palabras):
            palabra = ""
            for i in range(random.randint(2, 5)):
                palabra += str(lista[random.randint(0, len(lista) - 1)])
            if palabra not in lista_resultado:
                lista_resultado.append(palabra)
        self.lista.append(lista_resultado)
    
    def concatenacion(self, indice1, indice2):
        lista_resultado = []
        for item in self.lista[indice1]:
            lista_resultado.extend([(str(item) + str(x)) for x in self.lista[indice2]])
        return lista_resultado
    
    def cerradura_estrella(self, indice, exponente):
        lista_resultado.append([str(x) for x in self.lista[indice]])
        lista_base = lista_resultado[0]
        for item in range(1, exponente - 1):
            lista_temp = []
            for temp in lista_base:
                lista_potencia = [(str(temp) + str(x)) for x in lista_resultado[item]]
                lista_temp.extend(lista_potencia)
            lista_resultado.append(lista_temp)
        return lista_resultado[len(lista_resultado) - 1]
    
    def inversa(self, indice):
        lista_resultado = []
        lista_objetivo = self.lista[indice]
        for i in range(len(lista_objetivo)):
            palabra = str(lista_objetivo[i])
            lista_resultado.append(palabra[::-1])
        return lista_resultado
    
    def cardinalidad(self, indice):
        return len(self.lista[indice])

