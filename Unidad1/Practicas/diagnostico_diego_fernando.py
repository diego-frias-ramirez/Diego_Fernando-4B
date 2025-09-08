import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
limpiar_pantalla()

# Diagnostico_nombre.py
# Simulador de pedidos
# Conceptos básicos: variables, inputs, condicionales, funciones y bucles

# Elegir una temática de tienda y escribir 3 productos
productos = ["Latte", "Capuchino", "Americano"]
precios = [50, 70, 40]

# Función para calcular el total
def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Menú para usuario (Outputs)
print("Menú de cafetería - ¡Bienvenido!")
nombre = input("Ingresa tu nombre: ")

cantidades = []

for i in range(len(productos)):
    print(f"{i + 1}. {productos[i]} - $ {precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} desea?: "))
    cantidades.append(cantidad)

total = calcular_total(cantidades, precios)

print(f"\nGracias por tu compra, {nombre}. El total a pagar es: ${total}")
