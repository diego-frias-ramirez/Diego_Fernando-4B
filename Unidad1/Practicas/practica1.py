# Practica 1 clases, objetos y atributos 

# Una clase es una plantilla o un molde 
# que define cómo será un objeto 

class Persona:
    def __init__(self, nombre, edad):  # Constructor 
        self.nombre = nombre
        self.edad = edad

    def Presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"Esta persona cumplió {self.edad} años")


# Un objeto es una instancia creada a partir
# de una clase
estudiante1 = Persona("Diego", 18)
estudiante2 = Persona("Pedro", 50)

# Asignar métodos a esos objetos (Acciones)
estudiante1.Presentarse()
estudiante1.cumplir_anios()


# Paso 1. Agrega un método cumplir_anios()
# que aumente en la edad

# INSTANCIA 
# Cada objeto creado de una clase es una instancia 
# Podemos tener varias instancias que coexistan con sus 
# propios datos 
# Objeto = instancia de la clase
# Cada vez que se crea un objeto con clase() se obtiene
# una instancia que tiene sus propios datos aunque vengan 
# de la misma clase.

# Abstracción
# Representar solo lo importante del mundo real,
# ocultando detalles innecesarios.

class Automovil:
    def __init__(self, marca):  # Constructor 
        self.marca = marca
      
    def arrancar(self):
        print(f"{self.marca} arrancó")


# Crear un objeto auto y asignar una marca
auto = Automovil("Nissan")
auto.arrancar()

# Abstracción: Nos centramos solo en lo que importa (acciones)
# que es arrancar el automóvil, ocultando detalles internos 
# como motor, transmisión, tipo_combustible. 
# Enfoque solo en la acción del objeto.
# Objetivo es hacer que el código sea más limpio y fácil de usar.

# Practica 1.2 
# 1. Crear una clase mascotas
# 2. Agregar mínimo 4 atributos 
# 3. Definir al menos 4 métodos diferentes
# 4. Crear 2 instancias de la clase 
# 5. Llamar los métodos y aplicar abstracción. (Agregar 
# un atributo innecesario)

class Mascota:
    def __init__(self, especie, raza, sexo, tamaño, sonido, color_ojos):  # Constructor 
        self.especie = especie
        self.raza = raza
        self.sexo = sexo
        self.tamaño = tamaño
        self.sonido = sonido
        self.color_ojos = color_ojos  # Atributo innecesario para mostrar abstracción

    def la_especie(self):
        print(f"La especie del animal es {self.especie} y su raza es {self.raza}")
    
    def el_tamaño(self):
        print(f"El tamaño del animal es {self.tamaño} cm.")

    def el_sexo(self):
        print(f"Su sexo es {self.sexo}")
    
    def su_sonido(self):
        print(f"El sonido del animal es {self.sonido}")

    def color_de_ojos(self):
        print(f"El color de ojos del animal es {self.color_ojos}")

# Un objeto es una instancia creada a partir
# de una clase
Mascota1 = Mascota("Perro", "French Poodle", "Hembra", 38, "Guau", "Café")
Mascota2 = Mascota("Gato", "Siames", "Macho", 20, "Miau", "Verde")
Mascota3 = Mascota("Vaca", "Holstein", "Hembra", 150, "Muuu", "Negro")
Mascota4 = Mascota("Oso", "Oso Pardo", "Macho", 300, "Gruñe", "Miel")

# Asignar métodos a esos objetos (Acciones)
Mascota1.la_especie()
Mascota1.el_tamaño()
Mascota1.el_sexo()
Mascota1.su_sonido()
Mascota1.color_de_ojos()

Mascota2.la_especie()
Mascota2.el_tamaño()
Mascota2.el_sexo()
Mascota2.su_sonido()
Mascota2.color_de_ojos()