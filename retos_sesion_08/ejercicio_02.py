"""
Sesión 08
Ejercicio 02

Crea una tupla con los siguientes elementos 1,2,3,4,5,6,7,8,9,10 y realiza:

Imprime el primer elemento
Imprime el último elemento
Imprime un slice del 4 al 7
Imprime un slice del 2 al 9 con pasos de 3
Imprime un slice del 10 al 1 con saltos de -2
"""

# Creamos la tupla
mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Imprimimos los elementos deseados
print(mi_tupla[0])
print(mi_tupla[-1])
print(mi_tupla[3:7])
print(mi_tupla[3:10:3])
print(mi_tupla[-1:-10:-2])
