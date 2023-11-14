# Una forma de realizarlo
listaCuadrados = []
listaCuadrados = [ x*x for x in range(1,11)]
print (listaCuadrados)

# Otra forma de realizaro
listaCuadrados2 = []
for i in range(1,11):
    listaCuadrados2.append(i*i)
print(listaCuadrados2)

#Criterios de seleccion mostrando solo los numeros impares
listaCuadrados3 = [ j*j for j in range(1,11) if j%2 != 0]
print(listaCuadrados3)

# Otro ejemplo de criterio de seleccion con caracteres, donde solo se agreguen ciertos elementos
letras = [caracter.upper for caracter in "comprensiones" if caracter not in 'aeiou']
print(letras)

