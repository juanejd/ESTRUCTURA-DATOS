def preorden(arbol):
    if arbol:
        print(arbol.obtenerValorRaiz())
        preorden(arbol.obtenerHijoIzquierdo())
        preorden(arbol.obtenerHijoDerecho())

def postorden(arbol):
    if arbol != None:
        postorden(arbol.obtenerHijoIzquierdo())
        postorden(arbol.obtenerHijoDerecho())
        print(arbol.obtenerValorRaiz())

def inorden(arbol):
    if arbol != None:
        inorden(arbol.obtenerHijoIzquierdo())
        print(arbol.obtenerValorRaiz())
        inorden(arbol.obtenerHijoDerecho())


