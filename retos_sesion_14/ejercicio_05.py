"""
Sesión 14
Ejercicio 05

Crear una función que reciba una cadena y devuelva la cadena invertida
"""

# Creamos la función
def invertir_cadena(cadena):
    # Invertir la cadena usando un ciclo for
    cadena_invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida = cadena[::-1]

    return cadena_invertida


# Pedimos al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")
cadena_invertida = invertir_cadena(cadena)

# Imprimimos el resultado
print("La cadena invertida es:", cadena_invertida)