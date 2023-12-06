from Implementacion_Grafo import Grafo

g = Grafo()

for i in range(6):
    g.agregarVertice(i)

print(g.obtenerVertices())

g.agregarArista("V0", "V1", 5)
g.agregarArista("V0", "V5", 2)
g.agregarArista("V1", "V2", 4)
g.agregarArista("V2", "V3", 9)
g.agregarArista("V3", "V4", 7)
g.agregarArista("V3", "V5", 3)
g.agregarArista("V4", "V0", 1)
g.agregarArista("V5", "V4", 8)
g.agregarArista("V5", "V2", 1)

for v in g:
    for w in v.obtenerConexiones():
        print("( %s , %s, %s)" % (v.obtenerId(), w.obtenerId(), v.obtenerPonderacion(w)))