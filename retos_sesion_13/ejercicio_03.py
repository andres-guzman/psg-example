"""
Sesión 13
Ejercicio 03

Dar las felicitaciones a los estudiantes que aprobaron el curso de la siguiente tupla de estudiantes:

estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]
"""

# Tupla de estudiantes
estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]

# Bucle for que imprime las felicitaciones
for nombre, nota in estudiantes:
    if nota > 50:
        print("Felicitaciones", nombre, "Aprobaste el curso!")
