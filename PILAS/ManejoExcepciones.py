import math

unNumero = int(input("Ingrese un numero: "))

try:
    print(math.sqrt(unNumero))
except:
    print("Valor incorrecto para calcular la raiz cuadrada, ya que es un numero negativo")
    print(f"Se ha usado en sustitucion, el valor absoluto de {unNumero}.")
    print(math.sqrt(abs(unNumero)))