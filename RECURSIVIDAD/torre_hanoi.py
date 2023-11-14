contador = 0
def moverTorre(altura, origen, destino, intermedio):
    global contador 

    if altura >= 1:
        moverTorre(altura - 1, origen, intermedio, destino)
        moverDisco(origen, destino)
        moverTorre(altura - 1, intermedio, destino, origen)
        contador += 1

def moverDisco(desde, hacia):
    print('mover disco de {} a {}'.format(desde, hacia))

moverTorre(3, "O", 'D', 'I')

print('El numero de llamados recursivos fue de:',contador)