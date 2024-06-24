"""
Sesión 11
Ejercicio 05

Eres NOE y tienes que guardar dos animales de cada especie en un arca, 
crea un diccionario con las especies

arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}

Añade al arca 2 especies más usando update()
Toma lista de los animales en el arca iterando el diccionario
Existe en el arca la especie 'dragon'?
Elimina la especie 'unicornio' del arca
Modifica el valor de la especie 'jirafa' por 2
Vacía el arca después del diluvio
"""

# Diccionario
arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}

# Añadir 2 especies
arca.update({"lobo": 2, "loro": 2})

# Toma lista de los animales
iterador = iter(arca.items())
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

# Existe en el diccioinario "dragon"?
resultado = "dragon" in arca
print(resultado)

# Eliminar "unicornio" del diccionario
del arca["unicornio"]
print(arca)

# Modifica el valor de "girafa" a 2
arca["jirafa"] = 2
print(arca)

# Vaciar todo el contenido del diccionario
arca.clear()
print(arca)
