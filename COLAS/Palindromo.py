from Cola_doble import ColaDoble

def verificarPalindromo(cadena):
    colaDobleCaracteres = ColaDoble()
    cadena = cadena.lower()
    
    for caracter in cadena:
        
        # Omitir espacios en la cadena de caracteres
        if caracter != " ":
            colaDobleCaracteres.agregarFinal(caracter)
    
    # Variable bandera
    aunIguales = True

    # condicion mientras la cola doble no esté vacia y aunIguales sea True
    while colaDobleCaracteres.tamano() > 1 and aunIguales:

        # removemos y mostramos el caracter que está al final y al frente de la cola doble 
        primero = colaDobleCaracteres.removerFrente()
        ultimo = colaDobleCaracteres.removerFinal()

        # En caso de que alguno de los 2 caracteres del final y al frente sean diferentes, la cadena ya no es palindromo
        if primero != ultimo:
            aunIguales = False
        
    return aunIguales

print(verificarPalindromo("lsdkjfskf"))
print(verificarPalindromo("radar"))
print(verificarPalindromo("Anita lava la tina"))