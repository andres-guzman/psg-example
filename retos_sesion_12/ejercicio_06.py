"""
Sesión 12
Ejercicio 06

Crea una calculadora por consola que realice las operaciones de 
suma, resta, multiplicación y división, ingresa dos números y 
la operación a realizar, verifica si la operación es válida y 
muestra el resultado

Número 1: 10
Número 2: 5
Operación: +
-------------
Resultado: 15

"""

# Pedir los números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Pedir la operación al usuario
operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

# Realizar la operación y mostrar el resultado
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 == 0:
        resultado = "Error: No se puede dividir por cero."
    else:
        resultado = numero1 / numero2
else:
    resultado = "Operación no válida."

# Imprimir el resultado
if isinstance(resultado, float):
    print("Número 1:", numero1)
    print("Número 2:", numero2)
    print("Operación:", operacion)
    print("-------------")
    print(f"Resultado: {resultado}")
else:
    print(resultado)
