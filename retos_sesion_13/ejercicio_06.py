"""
Sesión 13
Ejercicio 06

Crea un ciclo infinito que reciba un número por teclado y 
verifique si es un número primo, termina la ejecución si se 
ingresa el número 0
"""

while True:
    # Pide un número al usuario
    numero = int(input("Ingrese un número (0 para salir): "))

    # Verificar si el número es 0
    if numero == 0:
        break

    # Verificar si el número es primo
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break

    # Imprimir resultado
    if es_primo:
        print(numero, "...es número primo.")
    else:
        print(numero, "...no es número primo.")
