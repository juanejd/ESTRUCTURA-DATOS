from Estructura_datos_colas import Cola 
from random import randint

def papaCaliente(listaNombres):
    
    colaSimulacion = Cola()

    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)

    while colaSimulacion.tamano() > 1:
        
        for i in range(randint(1, 20)):
            colaSimulacion.agregar(colaSimulacion.avanzar())
        
        print(colaSimulacion.avanzar())
    
    return colaSimulacion.avanzar()

jugadores = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']

print(papaCaliente(jugadores))