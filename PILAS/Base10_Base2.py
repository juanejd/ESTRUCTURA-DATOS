from Estructura_datos_pilas import Pila

def dividirPor2(numeroDecimal):
    pilaResiduo = Pila()

    # Mientras el numero ingresado sea mayor a 0, seguiremos dividiendo entre 2
    while numeroDecimal > 0:

        # Sacamos el residuo del numero ingresado y lo agregamos a la pila
        residuo = numeroDecimal % 2
        pilaResiduo.incluir(residuo)

        # Ahora el numero ingresado lo dividimos entre 2 y volvemos al ciclo con el nuevo numero. 
        # EJ: 233 // 2 = 116
        # Luego 116 % 2 y agregamos el residuo a la pila y asi sucesivamente
        numeroDecimal = numeroDecimal // 2
        print(residuo)

    # Mientras la pila no esté vacia, vamos a concatenar los valores del tope de la pila
    # Lo convertimos en str para concatenar los valores
    cadenaBinaria = ''
    while not pilaResiduo.estaVacia():
        cadenaBinaria += str(pilaResiduo.extraer())

    return cadenaBinaria