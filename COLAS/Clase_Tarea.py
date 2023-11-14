import random

class Tarea:
    def __init__(self,tiempo):
        self.marcaTiempo = tiempo
        self.paginas = random.randrange(1, 21)

    def obtenerMarca(self):
        return self.marcaTiempo
    
    def obtenerPaginas(self):
        return self.paginas
    
    def tiempoEspera(self, tiempoActual):
        return tiempoActual - self.marcaTiempo