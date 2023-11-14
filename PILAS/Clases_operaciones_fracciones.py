def maximo(a,b):
  if b == 0: 
    return a # cuando el segundo numero es 0, nos retorna el primer numero.
  else:
    return maximo(b,a%b)

 # Otra funcion para hallar el maximo comun divisor de 2 numeros usando while 
def mcd(m, n):
   while m%n != 0:
      mViejo = m
      nViejo = n
      
      m = nViejo
      n = mViejo % nViejo
      return n

class Fraccion:
    def __init__(self,numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)
    
    def __add__(self, f2):
        nuevo_numerador = (self.numerador * f2.denominador + self.denominador * f2.numerador)
        nuevo_denominador = self.denominador * f2.denominador
        
        #Simplificar la fraccion
        mcd = maximo(nuevo_numerador, nuevo_denominador)
        nuevo_numerador = nuevo_numerador // mcd
        nuevo_denominador = nuevo_denominador // mcd

        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __sub__(self, f2):
        nuevo_numerador = (self.numerador * f2.denominador - self.denominador * f2.numerador)
        nuevo_denominador = self.denominador * f2.denominador
        
        #Simplificar la fraccion
        mcd = maximo(nuevo_numerador, nuevo_denominador)
        nuevo_numerador = nuevo_numerador // mcd
        nuevo_denominador = nuevo_denominador // mcd

        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, f2):
        nuevo_numerador = (self.numerador * f2.numerador)
        nuevo_denominador = (self.denominador * f2.denominador)
        
        #Simplificar la fraccion
        mcd = maximo(nuevo_numerador, nuevo_denominador)
        nuevo_numerador = nuevo_numerador // mcd
        nuevo_denominador = nuevo_denominador // mcd

        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __truediv__(self, f2):
        nuevo_numerador = (self.numerador * f2.denominador)
        nuevo_denominador = (self.denominador * f2.numerador)
        
        #Simplificar la fraccion
        mcd = maximo(nuevo_numerador, nuevo_denominador)
        nuevo_numerador = nuevo_numerador // mcd
        nuevo_denominador = nuevo_denominador // mcd
        
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __eq__(self, f2):
       return self.numerador == f2.numerador and self.denominador == f2.denominador

#Objetos creados a partir de la clase Fraccion
f1 = Fraccion(1, 4)
f2 = Fraccion(1, 2)

#Sobrecarga de metodos para las operaciones basicas e igualdad
miFraccion = f1 + f2
miFraccion2 = f1 - f2
miFraccion3 = f1 * f2
miFraccion4 = f1 / f2
miFraccion5 = f1 == f2

# Imprimir resultados
print(f1.__str__() + ' + ' + f2.__str__())
print(miFraccion, '\n')

print(f1.__str__() + ' - ' + f2.__str__())
print(miFraccion2, '\n')

print(f1.__str__() +'*'+ f2.__str__())
print(miFraccion3, '\n')

print(f1.__str__() +'/'+ f2.__str__())
print(miFraccion4, '\n')

print(f1.__str__() ,'==', f2.__str__())
if miFraccion5:
   print('Son iguales')
else:
   print('No son iguales')