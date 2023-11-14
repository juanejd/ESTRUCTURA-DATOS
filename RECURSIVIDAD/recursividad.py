def sumarListaRecursiva(listaNumeros):
    if len(listaNumeros) == 1:
        return listaNumeros[0]
    else:
        return listaNumeros[0] + sumarListaRecursiva(listaNumeros[1:])
    
#listaNumeros = [1, 3, 5, 7, 9]

print("Resultado recursivo ", sumarListaRecursiva([1, 3, 5, 7, 9]))