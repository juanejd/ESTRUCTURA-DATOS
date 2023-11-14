from Estructura_datos_pilas import Pila

def convertirBase(numeroDecimal, base):
    digitos = '0123456789ABCDEF'
    pilaResiduo = Pila()

    # Mientras el numero ingresado sea mayor a 0, seguiremos dividiendo entre la base ingresada
    while numeroDecimal > 0:

        # Sacamos el residuo del numero ingresado y lo agregamos a la pila
        residuo = numeroDecimal % base
        pilaResiduo.incluir(residuo)

        # Ahora el numero ingresado lo dividimos entre la base ingresada y volvemos al ciclo con el nuevo numero. 
        # EJ: 233 // {base} 
        # Luego {numeroDecimal} % {base} y agregamos el residuo a la pila y asi sucesivamente
        numeroDecimal = numeroDecimal // base
        
    nuevaCadena = ''
    while not pilaResiduo.estaVacia():
        nuevaCadena += digitos[pilaResiduo.extraer()]

    return nuevaCadena