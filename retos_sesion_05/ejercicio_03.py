"""
Sesión 05
Ejercicio 03

Convertir a cuantos días, horas, minutos y segundos corresponde la siguiente cantidad de segundos: 
288325
"""

# Segundos
segundos = 288325

# Convertir a días
formula_a_dias = 60 * 60 * 24
segundos_a_dias = segundos / formula_a_dias
print(segundos, "segundos equivale a", segundos_a_dias, "días")

# Convertir a horas
formula_a_horas = 60 * 60
segundos_a_horas = segundos / formula_a_horas
print(segundos, "segundos equivale a", segundos_a_horas, "horas")

# Convertir a minutos
formula_a_minutos = 60
segundos_a_minutos = segundos / formula_a_minutos
print(segundos, "segundos equivale a", segundos_a_minutos, "minutos")

# Convertir a segundos (???)
formula_a_segundos = 1
segundos_a_segundos = segundos / formula_a_segundos
print(segundos, "segundos equivale a", segundos_a_segundos, "segundos")