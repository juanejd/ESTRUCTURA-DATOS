import operator
def evaluar(arbolAnalisis):
    # Asociar simbolos una operacion en especifico
    operadores = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    hijoIzquierdo = arbolAnalisis.obtenerHijoIzquierdo()
    hijoDerecho = arbolAnalisis.obtenerHijoDerecho()

    if hijoIzquierdo and hijoDerecho:
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        
        return fn(evaluar(hijoIzquierdo), evaluar(hijoDerecho))
    
    else:
        return arbolAnalisis.obtenerValorRaiz()

    