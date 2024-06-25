"""
Sesión 13
Ejercicio 02

Imprimir los 20 primeros números primos
"""

# Contador de números primos encontrados
contador_primos = 0
# Número a evaluar
numero = 2

# Bucle while para encontrar 20 números primos
while contador_primos < 20:
    es_primo = True

    # Bucle for
    divisor = 2
    while divisor <= numero ** 0.5 and es_primo:
        if numero % divisor == 0:  # Si el número es divisible por el divisor
            es_primo = False  # El número no es primo
            break  # Sale del bucle for si encuentra un divisor
        divisor += 1

    if es_primo:
        print(numero)  # Imprime el número primo encontrado
        contador_primos += 1  # Incrementa el contador de primos encontrados

    # Incrementa el número a evaluar como primo potencial
    numero += 1
