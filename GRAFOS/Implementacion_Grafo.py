from Implementacion_Vertice import Vertice

class Grafo:
    def __init__(self):
        self.listaVertices = {} # Lista adyacencia
        self.numVertices = 0 # Numero de vertices
    
    def agregarVertice(self, clave):
        self.numVertices += 1 # Agregarle 1 a 1 los vertices
        nuevoVertice = Vertice(clave) # Crear un objeto de la clase Vertice
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice
    
    # Consultar en el diccionario los vertices, en caso de que si exista lo retorna, de lo contrario no devuelve nada
    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
        
    # vertice in grafo 
    # n = claves ; self.listaVertices = diccionario
    def __contains__(self, n):
        return n in self.listaVertices
    
    # de = Origen ; a = Destino ; costo = Ponderacion
    def agregarArista(self, de, a, costo = 0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)

        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
    
    # Mostrar todos los vertices
    def obtenerVertices(self):
        return self.listaVertices.keys()
    
    # Iterar las ponderaciones
    def __iter__(self):
        return iter(self.listaVertices.values())