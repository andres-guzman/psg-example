"""
Sesión 14
Ejercicio 06

Crear una función que reciba una lista de números y devuelva solo los números pares
"""

# Creamos la función
def filtrar_pares(lista_numeros):
    pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


# Lista de números
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filtrar_pares(lista_original)

# Imprime la lista origina y la lista con números pares
print("Lista original:", lista_original)
print("Lista de números pares:", lista_pares)
