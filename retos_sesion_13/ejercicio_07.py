"""
Sesión 13
Ejercicio 07

Crear una serie de números del 1 al 100, si el número es divisible por 3 
imprimir Fizz, si el número es divisible por 5 imprimir Buzz, si el 
número es divisible por 3 y 5 imprimir FizzBuzz
"""

# Bucle con rango de enteros del 1 al 100
for numero in range(1, 101):
    # Verificar si es divisible entre 3 y 5
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    # Verificar si es divisible entre 3
    elif numero % 3 == 0:
        print("Fizz")
    # Verificar si es divisible entre 5
    elif numero % 5 == 0:
        print("Buzz")
    # Si no es divisible por 3 ni 5, imprimir el número
    else:
        print(numero)
