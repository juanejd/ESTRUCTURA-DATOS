from Estructura_datos_pilas import Pila

def verificarSimbolos(cadenaSimbolos):
    p = Pila()
    balanceados = True
    indice = 0

    #cadenaSimbolos = { { ([] []) } () } len = 12

    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        print("p == ",simbolo)

        if simbolo in "([{":
            p.incluir(simbolo)
            print("pila == ",p.inspeccionar())
        else:
            if p.estaVacia():
                balanceados = False
            else:
                #print("\npila nueva",p.inspeccionar())
                tope = p.extraer()
                print("\n== tope ",tope)
                print("")
                print("== simbolo", simbolo)
                if not parejas(tope, simbolo):
                    balanceados = False  
        indice += 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False

def parejas(simboloApertura, simboloCierre):
    aperturas = "([{"
    cierres = ")]}"
    return aperturas.index(simboloApertura) == cierres.index(simboloCierre)


    
                
