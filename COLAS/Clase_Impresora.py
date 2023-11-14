class Impresora:
    def __init__(self, paginas):
        self.tasaPaginas = paginas # Velocidad impresora
        self.tareaActual = None # La impresora inicializa sin tareas asignadas
        self.tiempoRestante = 0
    
    # Segundero cuando haya una tarea en curso (Simula cuanto tiempo estará ocupada la impresora,
    # de acuerdo a la tarea asignada, si la tarea dura 100 segundos, durante las siguientes 100 iteraciones
    # de 'segundoActual' no estará disponible la impresora)
    def tictac(self):
        if self.tareaActual != None:
            self.tiempoRestante -= 1

            if self.tiempoRestante == 0:
                self.tareaActual = None

    def ocupada(self):
        if self.tareaActual != None:
            return True
        else:
            return False

    def iniciarNueva(self, nuevaTarea):
        self.tareaActual = nuevaTarea
        self.tiempoRestante = nuevaTarea.obtenerPaginas() * (60 / self.tasaPaginas) 


