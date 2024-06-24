"""
Sesión 12
Ejercicio 01

Crear un script que pida un número entero y verifique si es par o impar usando operador ternario
"""

# Pide al usuario que ingrese un número
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es par o impar
resultado = "Par" if numero % 2 == 0 else "Impar"

# Imprime resultado
print("El número", numero, "es", resultado)
