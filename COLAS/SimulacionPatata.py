from Estructura_datos_colas import Cola 

    # N = Número de rotaciones a ronda, en este caso es 7 
def papaCaliente(listaNombres, N):
    
    colaSimulacion = Cola()

    # Creacion de la cola a iterar
    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)      

    # Ciclo que acaba cuando en la cola solo queden 1 elemento y lo muestra en el return 
    while colaSimulacion.tamano() > 1:
        
        # Ciclo iterativo para agregar el elemento al frente de la cola al final de la misma
        # hasta N veces, eliminando el elemento que que esté al frente de la cola.
        for i in range(N):
            colaSimulacion.agregar(colaSimulacion.avanzar())
        
        print(colaSimulacion.avanzar())
    
    return colaSimulacion.avanzar()

jugadores = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']

print(papaCaliente(jugadores, 7))


"""
#Lista original
['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']

# Cola creada
['Brad', 'Kent', 'Jane', 'Susan', 'David', 'Bill']

# Ciclos
['Bill', 'Brad', 'Kent', 'Jane', 'Susan', 'David']

['David', 'Bill', 'Brad', 'Kent', 'Jane', 'Susan']

['Susan', 'David', 'Bill', 'Brad', 'Kent', 'Jane']

['Jane', 'Susan', 'David', 'Bill', 'Brad', 'Kent']

['Kent', 'Jane', 'Susan', 'David', 'Bill', 'Brad']

['Brad', 'Kent', 'Jane', 'Susan', 'David', 'Bill']

['Bill', 'Brad', 'Kent', 'Jane', 'Susan', 'David']

Retorna el nombre que esta al frente y queda eliminado

"""