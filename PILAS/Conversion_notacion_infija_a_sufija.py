from Estructura_datos_pilas import Pila
import string

def infija_a_sufija(expresionInfija):

    # Jerarquia de los operadores guardadas dentro de un diccionario
    precedencia = {}
    precedencia['*'] = 3
    precedencia['/'] = 3
    precedencia['+'] = 2
    # precedencia['-'] = 2
    precedencia['('] = 1

    pilaOPeradores = Pila() # Paso 0
    listaSufija = [] # Lista de salida
    listaSimbolos = expresionInfija.split()

    for simbolo in listaSimbolos:

        if simbolo in string.ascii_uppercase:
            listaSufija.append(simbolo)
        
        elif simbolo == '(':
            pilaOPeradores.incluir(simbolo)
        
        elif simbolo == ')':
            simboloTope = pilaOPeradores.extraer()
            
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope = pilaOPeradores.extraer()
        
        else:
            while (not pilaOPeradores.estaVacia()) and (precedencia[pilaOPeradores.inspeccionar()] >= precedencia[simbolo]):
                listaSufija.append(pilaOPeradores.extraer())
            pilaOPeradores.incluir(simbolo)
    
    while not pilaOPeradores.estaVacia():
        listaSufija.append(pilaOPeradores.extraer())
    
    return " ".join(listaSufija)
