"""
Sesión 10
Ejercicio 01

Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que salen van a 
comer a una plaza de comidas. Ambos quieren saber que tan compatibles son viendo 
cuantos platos de comida tienen en común. A continuación tienes los platos de
comida que ambos han ido pidiendo a los largo de sus citas:

Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa

Si la cantidad platos de comida que tienen en comunes mayor a 50% entonces ambos seguirán saliendo
"""

# Comidas favoritas
set_anita = {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
set_pepito = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}

# Interseción de platos en común
platos_en_comun = set_anita.intersection(set_pepito)
# Guarda la cantidad de platos en común
platos_en_comun_len = len(platos_en_comun)

# Imprimir platos en común
print("Anita y Pepito tiene estos platos en común:", platos_en_comun)

# Segirán saliendo?
set_anita_len = len(set_anita)
set_pepito_len = len(set_pepito)

# Suma la cantidad de todos los platos y divide entre 2 (50%)
suma_sets = (set_anita_len + set_pepito_len) / 2

# Si la cantidad de platos en común es mayor al 50%
# de la suma de todos los platos, seguirán saliendo
if platos_en_comun_len > suma_sets:
    print("Seguirán saliendo :)")
else:
    print("No seguirán saliendo :(")
