"""
Sesión 13
Ejercicio 04

Crea un ciclo infinito que reciba una palabra por teclado y verifique
si es palíndrome, termina la ejecución si se ingresa la palabra "salir"
"""

# Creamos el bucle infinito
while True:
    # El usuario ingresa la palabra
    palabra = input("Ingrese una palabra ('salir' para terminar): ")

    # Verifica si la palabra es "salir"
    if palabra == "salir":
        break  # Termina el bucle infinito

    # Invierte la palabra
    palabra_invertida = palabra[::-1]

    # Compara la palabra original con la invertida
    if palabra == palabra_invertida:
        print(palabra, "...es palíndromo.")
    else:
        print(palabra, "...no es un palíndromo.")
