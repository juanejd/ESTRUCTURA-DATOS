import random

from Estructura_datos_colas import Cola
from Clase_Impresora import Impresora
from Clase_Tarea import Tarea

def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
    tiempoEspera = []
    tareas = 0
    tamanoCola = []

    # Segundero
    for segundoActual in range(numeroSegundos):
        
        # Aca se crea la nueva tarea, de acuerdo si recibe True o False --> nuevaTareaImpresion y la agrega al final de la cola
        if nuevaTareaImpresion():
            tamanoCola.append(colaImpresion.tamano()) #Graficar valores en matplotlib

            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)
            tareas += 1

        # Si la impresora no esta ocupada y la cola no está ocupada
        if (not impresoraLaboratorio.ocupada()) and (not colaImpresion.estaVacia()):

            # Avanza en la siguiente tarea, y luego calculamos cuanto tiempo estuvo la tarea en la cola antes de ser atentida
            tareaSiguiente = colaImpresion.avanzar()
            tiempoEspera.append(tareaSiguiente.tiempoEspera(segundoActual))

            # Calcula cuanto tiempo estará ocupada la impresora
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()
    
    esperaPromedio = sum(tiempoEspera) / float(len(tiempoEspera))
    # % ---> convertidor: 6 cifras enteras y 2 decimales
    print('Tiempo de espera promedio %6.2f segundos %3d tareas restantes. %3d tareas en total'%(esperaPromedio, colaImpresion.tamano(), tareas))
    

# Distribucion uniforme
def nuevaTareaImpresion():
    numero = random.randrange(1, 181)

    # Si el numero es 180, retorna True para poder crear una tarea
    if numero == 180:
        return True
    else:
        return False

#Simulacion de impresora durante 1 hora (3600 segundos) e imprime 5 paginas por minuto
for i in range(10):
    simulacion(3600, 10)
