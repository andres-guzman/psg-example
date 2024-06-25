"""
Sesión 13
Ejercicio 01

Imprimir los 20 primeros números de la serie de Fibonacci
"""

# Creamos los dos primeros números
a = 1
b = 1

# Impresión de los 20 primeros números de la serie de Fibonacci
for i in range(1, 21):
    print(a)
    c = a + b
    a = b
    b = c
