from VerificarSimbolos import verificarSimbolos

verificacion = verificarSimbolos('{{([][])}()}')
if verificacion:
    print('Los símbolos están balanceados')
else:
    print('Los símbolos no estan balanceados')

