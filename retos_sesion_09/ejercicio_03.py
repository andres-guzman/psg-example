"""
Sesión 09
Ejercicio 03

Crear una lista de personas con 10 nombres de personas
Obtener una sub lista de 2 a 7
Buscar si existe el nombre "Jhon" en la lista original
Ordenar la sub lista alfabéticamente
Ordenar la lista original alfabéticamente de forma descendente
"""

# Lista de personas
personas = ["Andres", "Juan", "Luis", "Pepa", "Sonia", "Pedro", "Roberto", "Tania", "Jose", "Jukka"]

# Sublista del 2 al 7
sublista = personas[1:7]
print("Sublista de 2 a 7:", sublista)

# Buscar el nombre "Jhon"
if "Jhon" in personas:
    print('"Jhon" se encuentra en la lista')
else:
    print('"Jhon" no se encuentra en la lista')
# Otra forma
print("Jhon" in personas)

# Ordenar la lista alfabéticamente
personas.sort()
print("Ordenado alfabéticamente", personas)

# Lista ordenada alfabéticamente de forma descendente
personas.sort(reverse=True)
print("De forma descendente", personas)
