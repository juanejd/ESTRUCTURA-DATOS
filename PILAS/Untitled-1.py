class Cliente:
  def __init__(self,info_cuenta,nombre,apellido,edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    # Llamar a la clase interna, añadiendole los argumentos que necesita dicha clase
    self.info_cuenta = self.CuentaBancaria(info_cuenta[0],info_cuenta[1])
  
  def obtener_nombre_completo(self):
    return "\nNombre cliente: {} {}.".format(self.nombre, self.apellido)
  
  def obtener_edad(self):
    return "\nEdad: {}.".format(self.edad)
  
  class CuentaBancaria:
  # Constructor
    def __init__(self,numero_cuenta,saldo):
      self.__numero_cuenta = numero_cuenta
      self.__saldo = saldo

    def informacion(self):
      return "Numero de cuenta {} \nSaldo: {} ".format(self.__numero_cuenta, self.__saldo)
  
    # METODO DEPOSITAR
    def depositar(self):
      depo = int(input('\nCuanto desea depositar: '))
      self.__saldo += depo
      return "Su saldo es de: {}".format(self.__saldo)

    # METODO RETIRAR
    def retirar(self):
      # Ciclo se que se repite si el monto a retirar es mayor al saldo disponible
      while True:
        try:
          retirar = int(input('\nCuanto desea retirar: '))
          if retirar <= self.__saldo:
            self.__saldo -= retirar
            return "Su saldo es de: {}".format(self.__saldo)
          else:
            print("El monto a retirar es mayor que el saldo disponible, Intente nuevamente")
        except:
          print("Entrada inválida. Por favor, ingrese un número entero válido.")
      
    def getcuenta(self):
      return self.__numero_cuenta
    
    def getSaldo(self):
      return self.__saldo

class ClienteVIP(Cliente):
  def __init__(self,info_cuenta,nombre,apellido,edad,compra):
      super().__init__(info_cuenta,nombre,apellido,edad)
      self.compra = compra
  
  # Descuento del 15%
  def obtener_descuento(self):
    self.descuento = 15
    return self.descuento
  
  def aplicar_descuento(self):
    saldo = self.info_cuenta.getSaldo()
    
    # Variable donde guardaremos el valor de la compra original y luego se le restara a este valor el descuento del 15%
    compra_descuento = compra

    if saldo <= 0:
      print('Saldo insuficiente.')
    else:
      descuento = self.compra * (self.obtener_descuento()/100) 
      compra_descuento -= descuento #Compra ingresada por el usuario - descuento del 15%
      saldo -= compra_descuento

      return "\nSe aplicó un descuento del {}% a la compra de {}, el total es {}\nSu saldo actual es de: {}".format(self.obtener_descuento(),self.compra,int(compra_descuento),int(saldo))


cuenta = int(input('Ingrese su numero de cuenta: '))
saldo_actual = 50000
cliente = Cliente([cuenta,saldo_actual],'Juan','Jimenez',24)

#Llamar metodos para mostrar informacion en pantalla
print(cliente.obtener_nombre_completo(),cliente.obtener_edad())
print(cliente.info_cuenta.informacion())
print(cliente.info_cuenta.depositar())
print(cliente.info_cuenta.retirar())


compra = int(input('\nValor de la compra: '))

# Llamamos el saldo restante, despues de depositar y retirar del saldo original
saldo2 = cliente.info_cuenta.getSaldo()

descuento = ClienteVIP([cuenta,saldo2],'Juan','Jimenez',24,compra)

print(descuento.aplicar_descuento())
