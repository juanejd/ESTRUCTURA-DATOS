def aCadena (n, base):
    cadenaConversion = "0123456789ABCDEF"

    if n < base: #Caso base que permite salir de la recursion
        return cadenaConversion[n]
    
    else: # Recursividad y concatenacion de residuos (caracteres)
        return aCadena(n//base, base) + cadenaConversion[n%base]
    

print(aCadena(769, 16))
print(aCadena(769, 2))