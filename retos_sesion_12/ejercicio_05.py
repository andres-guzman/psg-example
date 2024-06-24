"""
Sesión 12
Ejercicio 05

Un usuario ingresa su nombre y gustos musicales por teclado separados 
por coma, verifica si el usuario ingresó un nombre válido usando truthiness, 
convertir los gustos musicales en una lista y verifica si tiene el gusto rock 
en su lista de gustos musicales

Nombre: John Doe
Gustos musicales: rock, pop, jazz
"""

# Solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Verificar si el nombre es válido (no vacío)
if nombre:
    print("Hola", nombre, "!")

    # Solicitar los gustos musicales al usuario
    gustos_musicales = input("Ingrese sus tres gustos musicales separados por comas: ")

    # Convertir los gustos musicales a una lista
    lista_gustos_musicales = gustos_musicales.split(",")

    # Verificar si "rock" está en la lista de gustos musicales
    if "rock" in lista_gustos_musicales:
        print(nombre, "Te gusta el rock :)")
    else:
        print(nombre, "No te gusta el rock :(")

else:
    print("El nombre ingresado no es válido. No puede estar vacío.")
