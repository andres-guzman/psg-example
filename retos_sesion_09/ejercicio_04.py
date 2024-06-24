"""
Sesión 09
Ejercicio 04

Tienes una tienda de abarrotes y tienes dos listas una con los 
productos que tienes y otra con los precios

Agregar 5 productos nuevos al final de las listas
Eliminar el producto con el nombre "Leche" de las listas
¿Cuanto cuesta el producto "Pan" y "Huevo"?
¿Cual es el producto más caro y más barato?
"""

# Lista de productos
lista_productos = ["Pan", "Huevo"]
# Lista de precios
lista_precios = [3, 4.5]

# Agregar 5 productos
lista_productos.extend(["Leche", "Jamón", "Azúcar", "Te", "Café"])
print(lista_productos)

# Eliminar "Leche" de la lista
lista_productos.remove("Leche")
print(lista_productos)

# Precio del pan
print(lista_precios[0])

# Precio más caro
print(max(lista_precios))

# Precio más barato
print(min(lista_precios))
