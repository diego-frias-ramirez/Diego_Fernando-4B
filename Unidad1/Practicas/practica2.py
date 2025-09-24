# Practica 2 Atributos publicos y privados 

class Persona:
    def __init__(self, nombre, edad):  # Constructor de una c
        self.nombre = nombre
        self.edad = edad
        self.__cuenta = None #Atributo privado

    def Presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"Esta persona cumplió {self.edad} años")

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria")

    def consulatar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es ${self.__cuenta.mostrar_saldo()}")
        else:
            print(f"{self.nombre} aun no teine una cuenta bancaria ")

class cuenta_bancaria:
    
    def __init__(self, num_cuenta, saldo): 
        self.num_cuenta = num_cuenta
        self.__saldo = saldo # Atributo privado

    def mostrar_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se deposito la cantidad de ${cantidad} a la cuenta, nuevo saldo es ${self.__saldo}")
        else:
            print("Ingresa una cantidad valida")

    def retirar(self, cantidad):
        print(f"El saldo de la cuenta es ${self.__saldo}")
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se retiró ${cantidad} de la cuenta, nuevo saldo es ${self.__saldo}")
        else:
            print("Cantidad inválida o fondos insuficientes")


#crear un objeto o instancia de la clase
perosna1 = Persona("Miguel", 20)
cuenta1 = cuenta_bancaria("001", 500)

perosna1.asignar_cuenta(cuenta1)
perosna1.consulatar_saldo()

cuenta1.depositar(200)
cuenta1.retirar(100)

#Acceder a los valores de los atributos publicos 
#print(perosna1.nombre)
#print(perosna1.edad)
