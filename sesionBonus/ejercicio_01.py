"""
Sesión Bonus
Ejercicio 01

Tienes un programa que cuenta la cantidad de frutas que 
aparecen en una lista y las guarda en un diccionario. 
El programa no muestra correctamente la información. Corrigelo!
"""

frutas = ['🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍌', '🍊', '🍉', '🍈', '🍇', '🍅', '🍅', '🍇']

# Función para contar las frutas
# def contar_frutas(lista_frutas):
#     contador = {}
#     for fruta in lista_frutas:
#         if fruta in contador:
#             contador[fruta] += 1
#         else:
#             contador[fruta] = 0
#     return contador

# # Función para imprimir el conteo de frutas
# def imprimir_conteo(conteo):
#     for fruta, cantidad in conteo:
#         print(f"Hay {cantidad} {fruta}(s).")

# # Llamando a las funciones
# conteo_frutas = contar_frutas(frutas)
# imprimir_conteo(conteo_frutas)


# ---------------------------------
# Código corregido
# ---------------------------------

# Función para contar las frutas
def contar_frutas(lista_frutas):
    contador = {}
    for fruta in lista_frutas:
        # Se utiliza `get()` para evitar errores si la fruta no está en el diccionario
        contador[fruta] = contador.get(fruta, 0) + 1
    return contador

# Función para imprimir el conteo de frutas
def imprimir_conteo(conteo):
    for fruta, cantidad in conteo.items():
        print(f"Hay {cantidad} {fruta}(s).")


# Llamando a las funciones
conteo_frutas = contar_frutas(frutas)
imprimir_conteo(conteo_frutas)
