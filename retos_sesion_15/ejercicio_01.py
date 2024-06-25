"""
Sesión 15
Ejercicio 01

Crear una calculadora que solicite dos números y realice las operaciones 
básicas de suma, resta, multiplicación y división con manejo de excepciones, 
para salir del programa se debe ingresar "salir"
"""

# Creamos la función
def calculadora():
    """
    Función que simula una calculadora básica con operaciones aritméticas.
    Permite salir del programa con la palabra "salir".
    """
    while True:
        try:
            # Solicitar el primer número
            numero1 = float(input("Ingrese el primer número: "))

            # Solicitar la operación
            operacion = input("Ingrese la operación (+, -, *, /): ")

            # Validar la operación
            # if operacion not in "+-*/":
            #     raise ValueError("Operación inválida. Use +, -, * o /.")

            # Solicitar el segundo número
            numero2 = float(input("Ingrese el segundo número: "))

            # Realizar la operación
            if operacion == "+":
                resultado = numero1 + numero2
            elif operacion == "-":
                resultado = numero1 - numero2
            elif operacion == "*":
                resultado = numero1 * numero2
            else:
                resultado = numero1 / numero2

            # Mostrar el resultado
            print(numero1, operacion, numero2, "=", resultado)

        except ValueError as error:
            print("Error:", error)

        # Verificar la condición para salir del programa
        if input("Escriba 'salir' para terminar el programa: ") == "salir":
            break

# Llamamos la función
calculadora()
