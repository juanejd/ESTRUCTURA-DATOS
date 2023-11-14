def raizCuadrada(n):
    raiz = n/2 #La suposicion inicial sera de 1/2 de 'n'
    
    for i in range(5):
        raiz = (1/2) * (raiz + (n / raiz))
    return raiz

print(raizCuadrada(2))

# 1.4142135623730951