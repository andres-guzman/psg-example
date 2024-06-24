"""
Sesión 11
Ejercicio 02

Crea un diccionario para almacenar información de comidas de animales por ejemplo

comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}

Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)
Existe en el diccionario de comidas la comida 'carne'?
Elimina la comida 'frutas' del diccionario de comidas
"""

# Diccionario con comidas para ciertos animales
comidas = {
    "frutas": {
        "animales": ["párajo", "tortuga"],
    },
    "carnes": {
        "animales": ["gato", "perro", "zorro"]
    },
    "verduras": {
        "animales": ["cebra", "caballo", "panda"]
    }
}

# Añadir al diccionario de comidas cuatro alimentos nuevos
comidas.update({"arroz": {"animales": ["pavo", "ganzo"]},
                "lacteos": {"animales": ["lince", "tigre"]},
                "yogurt": {"animales": ["zorro", "gallo"]},
                "queso": {"animales": ["loro", "pez"]}})

# Revisar si la clave "carnes" existe en el diccionario comidas
resultado = "carnes" in comidas # Devuelve un booleano

# Imprime el resultado dependiendo si la
# clave "carnes" existe en "comidas"
if resultado:
    print("Si existe")
else:
    print("No existe")

# Eliminar del diccionario la clave "frutas"
del comidas["frutas"]

# Imprimir el diccionario sin la comida "frutas"
print(comidas)
