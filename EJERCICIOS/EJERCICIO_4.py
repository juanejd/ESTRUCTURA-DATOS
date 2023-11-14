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
    
    # Metodos relacionales ==, >, >=, <, <= y !=
    
    # ==
    def __eq__(self, f2):
       return self.numerador == f2.numerador and self.denominador == f2.denominador
    
    # >
    def __gt__(self, f2):

       num_1 = self.numerador * f2.denominador
       num_2 = f2.numerador * self.denominador

       return num_1 > num_2
    
    # >=
    def __ge__(self, f2):

       num_1 = self.numerador * f2.denominador
       num_2 = f2.numerador * self.denominador
       
       if num_1 >= num_2:
          return True
       else:
          return False
    
    # <
    def __lt__(self, f2):
       num_1 = self.numerador * f2.denominador
       num_2 = f2.numerador * self.denominador

       return num_1 < num_2
    
    # <=
    def __le__(self, f2):

       num_1 = self.numerador * f2.denominador
       num_2 = f2.numerador * self.denominador
       
       if num_1 <= num_2:
          return True
       else:
          return False
       
    # !=
    def __ne__(self, f2):
        return self.numerador != f2.numerador or self.denominador != f2.denominador
       
#Objetos creados a partir de la clase Fraccion
f1 = Fraccion(4, 16)
f2 = Fraccion(1, 3)

#Sobrecarga de metodos para las operaciones basicas e igualdad
miFraccion = f1 + f2
miFraccion2 = f1 - f2
miFraccion3 = f1 * f2
miFraccion4 = f1 / f2

miFraccion5 = f1 == f2
miFraccion6 = f1 > f2
miFraccion7 = f1 >= f2
miFraccion8 = f1 < f2
miFraccion9 = f1 <= f2
miFraccion10 = f1 != f2


# Imprimir resultados
print(f1.__str__() + ' + ' + f2.__str__())
print(miFraccion, '\n')

print(f1.__str__() + ' - ' + f2.__str__())
print(miFraccion2, '\n')

print(f1.__str__() +' * '+ f2.__str__())
print(miFraccion3, '\n')

print(f1.__str__() +' / '+ f2.__str__())
print(miFraccion4, '\n')


print(f1.__str__() ,'==', f2.__str__())
if miFraccion5:
   print('Son iguales\n')
else:
   print('No son iguales\n')

print(f1.__str__() ,'>', f2.__str__())
if miFraccion6:
   print('Verdadero, la fraccion {} es mayor a {}\n'.format(f1.__str__(), f2.__str__()))
else:
   print('Falso, la fraccion {} es menor a {}\n'.format(f1.__str__(), f2.__str__()))

print(f1.__str__() ,'>=', f2.__str__())
if miFraccion7:
   print('Verdadero, la fraccion {} es mayor o igual a {}\n'.format(f1.__str__(), f2.__str__()))
else:
   print('Falso, la fraccion {} es menor a {}\n'.format(f1.__str__(), f2.__str__()))


print(f1.__str__() ,'<', f2.__str__())
if miFraccion8:
   print('Verdadero, la fraccion {} es menor a {}\n'.format(f1.__str__(), f2.__str__()))
else:
   print('Falso, la fraccion {} es mayor a {}\n'.format(f1.__str__(), f2.__str__()))

print(f1.__str__() ,'<=', f2.__str__())
if miFraccion9:
   print('Verdadero, la fraccion {} es menor o igual a {}\n'.format(f1.__str__(), f2.__str__()))
else:
   print('Falso, la fraccion {} es mayor a {}\n'.format(f1.__str__(), f2.__str__()))

print(f1.__str__() ,'!=', f2.__str__())
if miFraccion10:
   print('Verdadero, Son diferentes\n')
else:
   print('Falso, Son iguales\n')


numerador = f1.obtenerNum()
denominador = f1.obtenerDen()

print("el numerador de f1 es: {}".format(numerador))
print("el denominador de f1 es: {}".format(denominador))