class Vertice:
    def __init__(self, clave):
        # los vertices tienen 2 atributos
        self.id = clave # Nombre del vertice 
        self.conectadoA = {} # Diccionario que conecta los vertices con la ponderacion

    # Agregar aristas de vertices con otros vertices
    def agregarVecino(self, vecino, ponderacion = 0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA ' + str([x.id for x in self.conectadoA])
    
    # Nos retorna los vertices
    def obtenerConexiones(self):
        return self.conectadoA.keys()
    
    # Retorna el nombre del vertice
    def obtenerId(self):
        return self.id
    
    # Retorna la ponderacion de un vertice en concreto
    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]