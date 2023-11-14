from Estructura_datos_colas import Cola

c = Cola()

print(c.estaVacia())
c.agregar('perro')
c.agregar(4)
c = Cola()

print()
print(c.estaVacia())
c.agregar(4)
c.agregar('perro')
c.agregar(True)

print()
print(c.tamano())
c.agregar(8.4)

print()
print(c.avanzar())
print(c.avanzar())
print(c.tamano())