from Estructura_datos_pilas import Pila

def evaluacionnotacionSufija(expresionSufija):
  pilaOperandos = Pila()
  listaSimbolos = expresionSufija.split()

  for simbolo in listaSimbolos:

    # en caso de que el simbolo sea un operando
    if simbolo in "0123456789":
      pilaOperandos.incluir(int(simbolo))

    # en caso de que el simbolo sea un operador
    else:
      operando2 = pilaOperandos.extraer()
      operando1 = pilaOperandos.extraer()

      resultado = hacerAritmetica(simbolo, operando1, operando2)
      pilaOperandos.incluir(resultado)

  return pilaOperandos.extraer()

def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):

  if operador == "*":
    return operandoIzquierda * operandoDerecha

  elif operador == "/":
    return operandoIzquierda / operandoDerecha

  elif operador == "+":
    return operandoIzquierda + operandoDerecha

  else:
    return operandoIzquierda - operandoDerecha
  

print(evaluacionnotacionSufija('7 8 + 3 12 + /'))