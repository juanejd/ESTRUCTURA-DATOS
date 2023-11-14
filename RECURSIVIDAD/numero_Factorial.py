def factIter(n):
    resultado = 1

    for i in range(2, n+1):
        resultado *= i
    return resultado

print(factIter(5))

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    
print(factorial(5))