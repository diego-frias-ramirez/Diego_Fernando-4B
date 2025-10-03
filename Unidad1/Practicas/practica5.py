# Practica 5. Patrones de diseño

class Logger:
    _instancia = None #Creamos un atributo de case donde se guarda la uncia intsancia 

    # __new__ es el metodo que controla la creacion del objeto antes de init. Sirve
    #  paa aseguranos de que  solo exista una instancia de la clase Looger
    
    def __new__(cls, *args, **kwargs):
        #args es un argumento posicional que permite recibir multiples parametros
        #kwargs permite cualquier cantidad de parametros con nombre
        # Validar si ya existe o no una instancia aun:
        if cls._instancia is None: #Si no existe una instancia
            cls._instancia = super().__new__(cls) #Creamos la instancia de logger
            # agregando un atributo "archivo" que apunte a un archivo fiscio
            # "a" signicifica append = Todo lo que se escriba se añade al final
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia #Devolvemos la misma instancia
    
    def log(self, mensaje):
        # simulando un logueo de logs
        self.archivo.write(mensaje + "\n")
        self.archivo.flush() #metodo para guardar en el disco

Logger1 = Logger() # Creamos la primera y uncia instancia
Logger2 = Logger() # Devolver la misma instancia sin crear una nueva 

Logger1.log("Inicio de secionen la aplicacion.")
Logger2.log("El usuario se autentico correctamente")


print(Logger1 is Logger2)  # True

# Actividad de la practica 

class Presidente:
    _instancia = None

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia

    def accion(self, accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)

# Instancias (todas apuntan a la misma por el Singleton)
p1 = Presidente("AMLO")
p1.accion("firmó decreto")

p2 = Presidente("Peña Nieto")
p2.accion("visitó España")

p3 = Presidente("Fox")
p3.accion("aprobó un presupuesto")

print("\n--- Historial de los presidentes: ---")
print(p1.historial)

## 1 . Que pasaria si eliminamos la verificacion if cls._instancia is None: en el metodo new?
"""
Si se elimina esa verificación, cada vez que se cree un nuevo objeto de la clase, 
se generará una nueva instancia. Eso rompe el propósito del patrón Singleton, que 
busca garantizar que solo haya una única instancia durante toda la ejecución del programa.
 Sin ese control, la clase se comportaría como cualquier otra clase normal.
"""
## 2. Que significa el "true" en p1 is p2 is p3 en el contexto del metodo sigleton?}
""" 
El "True" indica que todas las variables p1, p2 y p3 apuntan a la misma instancia de la clase Presidente.
"""
## 3. Es buena idea usar singleton para todo lo que sea global?
"""
No siempre. Aunque el Singleton puede ser útil para manejar recursos que deben compartirse 
(como logs, configuraciones o conexiones), abusar de este patrón puede traer problemas. 
Por ejemplo, dificulta las pruebas unitarias, puede generar acoplamiento fuerte entre clases, 
y no es adecuado cuando se necesitan instancias independientes. Es mejor usarlo solo cuando está 
justificado y se necesita explícitamente una única instancia.
"""