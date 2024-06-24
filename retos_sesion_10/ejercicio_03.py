"""
Sesión 10
Ejercicio 03

Dos mochileros se encuentran en el Salar de Uyuni y se ponen a 
comparar la cantidad de lugares que han visitado. Cada uno quiere 
saber en que parte del mundo ha estado el otro que el no haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivi
"""

# Mochileros a y b
mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina","Brasil","Panama","Bolivia"}

# Lugares en los que mochilero a no ha estado
mochilero_a_no_estuvo = mochilero_b.difference(mochilero_a)

# Lugares en los que mochilero b no ha estado
mochilero_b_no_estuvo = mochilero_a.difference(mochilero_b)

# Imprime los resultados de ambos mochileros
print("Mochilero A no conoce:", mochilero_a_no_estuvo)
print("Mochilero B no conoce:", mochilero_b_no_estuvo)

# ---------------------------------------------------------------
# Ahora quieren saber en que ciudades han estado ambos mochileros
# ---------------------------------------------------------------

# Intersección entre ambos sets de mochileros
lugares_en_comun = mochilero_a.intersection(mochilero_b)

# Imprime los resultados de la intersección
print("Lugares que ambos mochileros conocen:", lugares_en_comun)
