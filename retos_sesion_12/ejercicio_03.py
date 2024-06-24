"""
Sesión 12
Ejercicio 03

El usuario Jhon Doe esta en una red social sus amigos son:
{Alice, Bob, Charlie, David, Eve}
La usuaria Jess Doe tiene los siguientes amigos
{Alice, Bob,  Frank, Grace}
¿Tienen Jhon y Jess amigos en común?, ¿Cuáles son?
"""

# Amigos de John y Jess
john_doe = {"Alice", "Bob", "Charlie", "David", "Eve"}
jess_doe = {"Alice", "Bob",  "Frank", "Grace"}

# Encontrar elementos en común
amigos_en_comun = john_doe.intersection(jess_doe)

# Verificar si hay elementos en común
if amigos_en_comun:
    print("John y Jess si tienen amigos en común")  # Ambos tienen amigos en común
    print("Amigos en común:", amigos_en_comun)
else:
    print("False")  # Ambos no tienen amigos en común
