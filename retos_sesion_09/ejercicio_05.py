"""
Sesión 09
Ejercicio 05

Tienes una tienda de abarrotes y tienes dos listas una con los productos que tienes 
y otra con los precios 

¿Cuántos productos tienes en total? 
¿Cuanto cuesta el total de los productos? 
Ordena los productos alfabéticamente y precios si es posible 
Eliminar todos los productos de las listas
"""

# Declarar la lista de productos
lista_productos = ["Pan", "Huevo", "Arroz", "Leche", "Jamón"]

# Declarar la lista de precios
lista_precios = [3, 4.5, 5, 3.14, 4.20]

# Total de productos
print(len(lista_productos))

# Precio total de productos
print(sum(lista_precios))

# Ordenar los productos alfabéticamente
lista_productos.sort()
print(lista_productos)

# Ordenar los precios de menor a mayor
lista_precios.sort()
print(lista_precios)

# Eliminar todos los productos de la lista
lista_productos.clear()
print(lista_productos)
