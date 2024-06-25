"""
Sesión 14
Ejercicio 03

Crear una función recursiva para obtener el N número de la serie de Fibonacci
"""

# Creamos la función
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Pedimos al usuario que ingrese el número N
n = int(input("Ingrese el número en la serie de Fibonacci: "))
resultado = fibonacci_recursivo(n)

# Imprimimos el resultado
print("La posicion del número es:", resultado)
