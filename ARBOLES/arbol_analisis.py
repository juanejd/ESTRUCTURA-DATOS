from Estructura_datos_pilas import Pila
from implementacion_nodos_referencias import ArbolBinario
from implementacion_recorridos_arboles import *
from evaluar_recursivamente import *

def construirArbolAnalisis(expresionAgrupada):
    listaSimbolos = expresionAgrupada.split()
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion #validar el nodo en el que nos encontramos

    for i in listaSimbolos:
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        
        elif i not in ['+', '-', '*', '/', ')']:
            arbolActual.asignarValorRaiz(int(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        
        elif i in ['+', '-', '*', '/']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        
        else:
            raise ValueError
        
    return arbolExpresion

miArbolAnalisis = construirArbolAnalisis("( ( 10 + 5 ) * 3 )")

preorden(miArbolAnalisis)
print()
print(evaluar(miArbolAnalisis)) # invocacion recursivamente