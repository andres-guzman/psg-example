"""
Sesión 11
Ejercicio 04

Gestión de hábitats en peligro: Crea un diccionario que asocie 
especies animales en peligro de extinción con información sobre sus
hábitats amenazados, lo que permite priorizar la protección de 
áreas críticas para la supervivencia de estas especies

habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, 
            "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}

Añade al diccionario de habitats 2 habitats más usando update()
Existe en el diccionario de habitats el habitat 'amazonas'?
Añade al diccionario de amazonas la especie 'anaconda'
"""

# Habitats
habitats = {
    "polo norte":
        {"especies": {"oso polar", "morsa", "ballena"}
         },
    "amazonas":
        {"especies": {"tigre", "mono", "guacamayo"}}
}

# Añadir 2 habitats
habitats.update({
    "polo sur":
        {"especies": {"pingüino", "foca", "lobo marino"}
         },
    "africa":
        {"especies": {"girafa", "hipopótamo", "hyena"}}
})

# Verificar si existe "amazonas" en el diccionario
resultado = "amazonas" in habitats
# Imprimir el resultado
print(resultado)

# Añadir a la clave "amazonas" la especie "anaconda"
habitats["amazonas"]["especies"].add("anaconda")
# Imprimir el diccionario actualizado
print(habitats)
