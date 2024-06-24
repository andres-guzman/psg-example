"""
Sesión 08
Ejercicio 06

De las tuplas de coordenadas:

$(x1,y1) = (40, 80) $ y $ (x2,y2) = (50, 50)$

Encuentra las coordenadas del punto medio, almacena en una tupla e imprime el resultado

$(x,y)$
"""

# Definir las coordenadas
x1 = 40
y1 = 80
x2 = 50
y2 = 50

# Encontrar el punto medio
punto_medio_x = (x1 + x2) / 2
punto_medio_y = (y1 + y2) / 2

# Almacenar las coordenadas del punto medio en una tupla
tupla_punto_medio = (punto_medio_x, punto_medio_y)

# Print the punto_medio tuple
print("Coordenadas del punto medio:", tupla_punto_medio)
