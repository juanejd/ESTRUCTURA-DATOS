class Pila:
    def __init__(self):
        self.items = [] #Lista que será nuestra pila

    # Metodo que nos validará si nuestra pila está vacia
    def estaVacia(self): 
        return self.items == []
    
    # Metodo para agregar un item a la pila en el tope
    def incluir(self, item):
        self.items.append(item)
    
    # Metodo que elimina el item que está al tope y nos lo muestra en pantalla 
    def extraer(self):
        return self.items.pop()
    
    # Metodo que nos muestra el item que está al tope y nos lo muestra en pantalla
    def inspeccionar(self):
        return self.items[len(self.items)-1] 
                        # pila = [1,hola,True] con "-1" nos retorna el item que esta al extremo derecho de la lista
    
    # Metodo que nos muestra la cantidad de items dentro de la pila
    def tamano(self):
        return len(self.items)

