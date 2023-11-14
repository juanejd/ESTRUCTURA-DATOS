def maximo(a,b):
  if b == 0: 
    return a # cuando el segundo numero es 0, nos retorna el primer numero.
  else:
    return maximo(b,a%b)

class Fraccion:
    def __init__(self,numerador, denominador):

        self.numerador = numerador
        self.denominador = denominador

        mcd = maximo(self.numerador, self.denominador)
        self.numerador = numerador // mcd
        self.denominador = denominador // mcd

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)
    
    def __add__(self, f2):
        nuevo_numerador = (self.numerador * f2.denominador + self.denominador * f2.numerador)
        nuevo_denominador = self.denominador * f2.denominador

        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def obtenerNum(self):
       return self.numerador
    
    def obtenerDen(self):
       return self.denominador
    
    def __sub__(self, f2):
        nuevo_numerador = (self.numerador * f2.denominador - self.denominador * f2.numerador)
        nuevo_denominador = self.denominador * f2.denominador

        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, f2):
        nuevo_numerador = (self.numerador * f2.numerador)
        nuevo_denominador = (self.denominador * f2.denominador)

        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __truediv__(self, f2):
        nuevo_numerador = (self.numerador * f2.denominador)
        nuevo_denominador = (self.denominador * f2.numerador)     
       
        return Fraccion(nuevo_numerador, nuevo_denominador)

#Objetos creados a partir de la clase Fraccion
f1 = Fraccion(6, 4)
f2 = Fraccion(16, 8)

#Sobrecarga de metodos para las operaciones basicas e igualdad
miFraccion = f1 + f2
miFraccion2 = f1 - f2
miFraccion3 = f1 * f2
miFraccion4 = f1 / f2

# Imprimir resultados
print(f1.__str__() + ' + ' + f2.__str__())
print(miFraccion, '\n')

print(f1.__str__() + ' - ' + f2.__str__())
print(miFraccion2, '\n')

print(f1.__str__() +' * '+ f2.__str__())
print(miFraccion3, '\n')

print(f1.__str__() +' / '+ f2.__str__())
print(miFraccion4, '\n')


numerador = f1.obtenerNum()
denominador = f1.obtenerDen()

print("el numerador de f1 es: {}".format(numerador))
print("el denominador de f1 es: {}".format(denominador))