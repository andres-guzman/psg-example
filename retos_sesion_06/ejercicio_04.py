"""
Sesión 06
Ejercicio 04

La suma de los números 7 y 3 es un número par?
"""

# Variables
numero_a = 7
numero_b = 3

# Calcular la sumaa
suma = numero_a + numero_b

# Revisa si el resultado de la suma es par o impar usando el operador módulo
if suma % 2 == 0:
    print("La suma de", numero_a, "y", numero_b, "es par")
else:
    print("La suma de", numero_a, "y", numero_b, "es impar")
