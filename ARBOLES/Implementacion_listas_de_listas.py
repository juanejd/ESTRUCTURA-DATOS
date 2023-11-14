# Instancia de un arbol binario, representado con listas de 3 items
def ArbolBinario(r):
    return [r, [], []]

def insertarIzquierdo(raiz,nuevaRama):
    t = raiz.pop(1)

    if len(t) > 1:
        raiz.insert(1, [nuevaRama, t, []] )
    else:
        raiz.insert(1, [nuevaRama, [], []] )
    
    return raiz

def insertarDerecho(raiz,nuevaRama):
    t = raiz.pop(2)
    
    if len(t) > 1:
        raiz.insert(2, [nuevaRama, [], t] )
    else:
        raiz.insert(2, [nuevaRama, [], []] )

    return raiz

# Posicion 0 de la lista, que en este caso, la raiz es el primer item de la lista
def obtenerValorRaiz(raiz):
    return raiz[0]

# Modificar el valor almacenado en un nodo, en este caso, en la primera posicion
def asignarValorRaiz(raiz, nuevoValor):
    raiz[0] = nuevoValor

def obtenerHijoIzquierdo(raiz):
    return raiz[1]

def obtenerHijoDerecho(raiz):
    return raiz[2]


r = ArbolBinario(3)

insertarIzquierdo(r, 4)
insertarIzquierdo(r, 5)

insertarDerecho(r, 6)
insertarDerecho(r, 7)

l = obtenerHijoIzquierdo(r)
print(l)

asignarValorRaiz(l, 9)
print(r)

insertarIzquierdo(l, 11)
print(r)
print(obtenerHijoDerecho(obtenerHijoDerecho(r)))