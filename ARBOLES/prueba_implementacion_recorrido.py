from implementacion_nodos_referencias import ArbolBinario
from implementacion_recorridos_arboles import *

# Nodo raiz
libro = ArbolBinario('Libro')

# Nodo izquierdo del subarbol
libro.insertarIzquierdo('Seccion 1.1')
# Subarbol izquierdo y raiz
libro.insertarIzquierdo('Capitulo 1')

#Nodo derecho subarbol derecho
libro.insertarDerecho('Seccion 2.2.2')
libro.insertarDerecho('Seccion 2.2')
#Subarbol derecho y raiz
libro.insertarDerecho('Capitulo 2')

# Posicionar las secciones
libro.obtenerHijoIzquierdo().insertarDerecho('Seccion 1.2.2')
libro.obtenerHijoIzquierdo().insertarDerecho('Seccion 1.2')
libro.obtenerHijoIzquierdo().obtenerHijoDerecho().insertarIzquierdo('Seccion 1.2.1')

libro.obtenerHijoDerecho().insertarIzquierdo('Seccion 2.1')
libro.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierdo('Seccion 2.2.1')

print('Recorrido en preorden: ')
preorden(libro)

print('\nRecorrido en inorden: ')
inorden(libro)

print('\nRecorrido en postorden: ')
postorden(libro)