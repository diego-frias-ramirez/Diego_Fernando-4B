# Práctica 4. Herencia
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")
    
# Clase Ticket
class Ticket:
    def __init__(self, id, tipo, prioridad, estado = "pendiente"):  # Constructor con estado por defecto
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "pendiente"

    def __str__(self):
        return f"{self.id:<15}{self.tipo:<10}{self.prioridad:<10}{self.estado:<10}"
    
# Clase padre Empleado
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

# Clase Desarrollador que hereda de Empleado
class Desarrollador(Empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo.lower() == "software":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print(f"{self.nombre} no puede resolver tickets de tipo '{ticket.tipo}'")

# Clase Tester que hereda de Empleado
class Tester(Empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo.lower() == "prueba":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print(f"{self.nombre} no puede resolver tickets de tipo '{ticket.tipo}'")

# Clase Project Manager que asigna tickets
class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_ticket(ticket)

"""
# Crear instancias de Ticket
ticket1 = Ticket(1, "software", "alta")
ticket2 = Ticket(2, "prueba", "media")

# Crear instancias de empleados
developer1 = Desarrollador("Gustavo")
tester1 = Tester("Pablo")
pm = ProjectManager("Susana")

# Asignar tickets a empleados
pm.asignar_ticket(ticket1, developer1)  # Ticket tipo software, lo resuelve el desarrollador
pm.asignar_ticket(ticket2, tester1)     # Ticket tipo prueba, lo resuelve el tester
pm.asignar_ticket(ticket1, tester1)     # Ticket tipo software, el tester no lo puede resolver


"""
# Lista de tickets
tickets = []

# Función para crear un nuevo ticket
def crearTicket():
    print("\n\t\t.::Agregar ticket::.\n\t")
    id = input("\nIngresa el id: ").upper().strip()
    tipo = input("\nIngresa el tipo: ").upper().strip()
    prioridad = input("\nIngresa la prioridad: ").upper().strip()
    estado = input("\nIngresa el estado: ").upper().strip()
    new_ticket = Ticket(id, tipo, prioridad, estado)
    tickets.append(new_ticket)
    print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!\n\t")

# Función para ver los tickets
def verTicket():
    print("Mostrar Ticket")
    if len(tickets) > 0:
        print(f"{'id':<15}{'tipo':<10}{'prioridad':<10}{'estado':<10}")
        print("-" * 50)
        for ticket in tickets:
            print(ticket)  # Usamos el __str__() de la clase Ticket
        print("-" * 50)
    else:
        print("No hay Tickets en el sistema")

# Crear instancias de empleados
developer1 = Desarrollador("Gustavo")
tester1 = Tester("Pablo")
pm = ProjectManager("Susana")

# Función para asignar un ticket a un empleado
def asignar_ticket(ticket_id, empleado_nombre):
    # Buscar el ticket por ID
    ticket = next((t for t in tickets if t.id == ticket_id), None)
    
    if ticket:
        # Verificar qué tipo de empleado y asignar
        if empleado_nombre == developer1.nombre:
            pm.asignar_ticket(ticket, developer1)
        elif empleado_nombre == tester1.nombre:
            pm.asignar_ticket(ticket, tester1)
        else:
            print("Empleado no encontrado.")
    else:
        print("Ticket no encontrado.")

# Interfaz de usuario
opcion = True
while opcion:
    borrarPantalla()
    print("\n\t\t\t..::: Tickets :::... \n\t\t..::: Sistema de Gestión de Tickets :::...\n\t\t 1.- Crear ticket  \n\t\t 2.- Ver tickets \n\t\t 3.- Asignar tickets \n\t\t 4.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            crearTicket()
            esperarTecla()
            borrarPantalla()
        case "2":
            verTicket()
            esperarTecla()
            borrarPantalla()
        case "3":
            ticket_id = input("\nIngresa el ID del ticket a asignar: ").strip().upper()
            empleado_nombre = input("Ingresa el nombre del empleado: ").strip().capitalize()
            asignar_ticket(ticket_id, empleado_nombre)  
            esperarTecla()
            borrarPantalla()
        case "4":
            opcion = False    
            print("\n\t\t Terminaste la ejecución del sistema.")
        case _:
            print("Opción inválida, vuelve a intentarlo... Presiona Enter.")
            input()
