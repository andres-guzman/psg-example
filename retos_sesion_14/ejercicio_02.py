"""
Sesión 14
Ejercicio 02

Calculadora_flexible flexible: Crea una calculadora_flexible que acepte diferentes 
operaciones matemáticas como argumentos de palabras clave y realice 
los cálculos correspondientes, las operaciones son suma, resta, 
multiplicación y división
"""

# Creamos la función
def calculadora_flexible(numero1, numero2, operacion):
    # Operaciones
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2
    else:
        print("Operación no válida.")
    return resultado


# Realizar una operación y mostrar el resultado
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

# Guarda el resultado de la funcion en la variable "resultado"
resultado = calculadora_flexible(numero1, numero2, operacion)

# Imprime el resultado de la operación
print(numero1, operacion, numero2, "=", resultado)
