from Estructura_datos_pilas import Pila

p = Pila()
print(p.estaVacia())

print("")

p.incluir(4)
p.incluir('perro')
print(p.inspeccionar())

print("")

p.incluir(True)
print(p.tamano())
print(p.estaVacia())

print("")

p.incluir(8.4)
print(p.extraer())
print(p.extraer())
print(p.tamano())