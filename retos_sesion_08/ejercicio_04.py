"""
Sesión 08
Ejercicio 04

Las notas de un estudiante durante un semestre son:
34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15
Genera una tupla con los resultados y calcula el promedio para saber si 
aprobó o no el semestre utiliza la función sum() y len()
"""

# Tupla con las notas
notas = (34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15)

# Sumar las notas
notas_suma = sum(notas)
# Contar el número de notas
notas_total = len(notas)

# Sacar el promedio dividiendo la suma con el numero de notas
notas_promedio = notas_suma / notas_total

# Imprimir si el alumno aprobó el semestre
if notas_promedio > 50:
    print("El alumno aprobó el semestre. Su promedio es:", notas_promedio)
else:
    print("El alumno reprobó el semestre. Su promedio es:", notas_promedio)
