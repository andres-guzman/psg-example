"""
Sesión 11
Ejercicio 03

Crea un diccionario con las siguientes tuplas de animales

tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))

Del diccionario obtén y elimina el valor de la clave 'aves'
Modifica el valor de la clave 'gato' por ''
Cambia la clave perro por perros y su valor por ['🐶','🐕']
"""

# Crear una tupla
tupla_animales = (('perro', '🐶'), ('gato','🐱'), ('aves',['🐦','🦅']))

# Crear un diccionario apartir de la tupla "tupla_aniamles"
animales = dict(tupla_animales)

# Imprmimos el diccionario
print(animales)

# Modificar el valor de la clave "gato" por su nuevo emoji
animales.update({"gato": "🐈"})

# Imprimimos el diccionario actualizado
print(animales)

# Cambiar la clave perro por perros y su valor por los nuevos emojis
animales["perros"] = animales.pop("perro")  # Mueve el valor de "perro" a "perros"
animales["perros"] = ['🐶','🐕']  # Actualiza el valor de "perros"

# Imprime el diccionario actualizado
print(animales)
