"""
Sesión 06
Ejercicio 05

Comparar los números 123 y 890, comprobar si tienen la misma paridad (ambos pares o ambos impares)
"""

# Números
numero_a = 123
numero_b = 890

# Ver si ambos números son par o impar
comparacion_1 = numero_a % 2
comparacion_2 = numero_b % 2

# Comprobar si ambos números tiene la misma paridad
if comparacion_1 == comparacion_2:
    if comparacion_1 == 0:
        print("Ambos números son pares")
    else:
        print("Ambos números son impares")
else:
    print("Los números no tienen la misma paridad")
