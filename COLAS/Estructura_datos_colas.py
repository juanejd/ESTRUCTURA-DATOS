# Asumimos que el 'frente' está al final de la lista
class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []
    
    def agregar(self, item):
        self.items.insert(0, item) # Agregar items al final de la cola

    def avanzar(self):
        return self.items.pop() # Eliminar el item que esta al frente de la cola

    def tamano(self):
        return len(self.items)