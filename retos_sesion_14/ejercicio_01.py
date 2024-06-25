"""
Sesión 14
Ejercicio 01

Un estudiante desea saber cuál es su promedio de calificaciones en 
la materia de matemáticas, cree una función que reciba las calificaciones
como lista y devuelva el promedio las calificaciones son 20,40,60,51,13
"""

# Creamos nuestra función
def promedio_matematicas(calificaciones):
    total_calificaciones = sum(calificaciones)
    numero_calificaciones = len(calificaciones)
    # Calculamos el promedio
    promedio = total_calificaciones / numero_calificaciones

    return promedio

# Calificaciones
calificaciones = [20, 40, 60, 51, 13]
promedio = promedio_matematicas(calificaciones)

# Imprimimos el promedio
print("Promedio de las calificaciones:", promedio)
