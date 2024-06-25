"""
Sesión Bonus
Ejercicio 02

Tienes un juego de adivinanzas en el que el jugador tiene que
adivinar un número entre 1 y 100. El juego tiene bugs, arréglalos!
"""

# def obtener_aleatorio():
#     numeros = list(range(1, 101))
#     secreto = numeros.pop()
#     return secreto


# def adivina(secreto):
#     intentos = 0
#     print("Que número estoy pensando? (1-100)")
#     while True:
#         try:
#             intento = int(input(f"Intento N°: {intentos+1}: "))
#             if intento == secreto:
#                 print("Felicidades! Has adivinado el número!")
#                 break
#             elif intento < secreto:
#                 print("El número es mayor.")
#             else:
#                 print("El número es menor.")
#         except ValueError:
#             print("Por favor, ingresa un número válido.")
#         finally:
#             intentos += 1
#     print(f"Has adivinado el número en {intentos*10} intentos.\n")


# nombre_jugador = "Guest"


# def jugar():
#     while True:
#         print("Bienvenido al juego de adivinanzas! del Python Study Group 2024")
#         print("="*63)
#         nombre_jugador = input("¿Cuál es tu nombre?: ")
#         print(f"Bienvenido, {nombre_jugador}!")
#         print("="*63)
#         print()
#         opcion = input("Quieres jugar? (s/n): ")
#         if opcion.lower() != 'S':
#             break
#         secreto = obtener_aleatorio()
#         adivina(secreto)
#     print("Gracias por participar!")
#     print(f"🐍 Gracias {nombre_jugador.upper()
#                        } por ser parte del Python Study Group 2024! 🐍")


# jugar()

# ---------------------------------
# Código corregido
# ---------------------------------

# Importamos la librería "random"
import random

def obtener_aleatorio():
    """
    Esta función genera un número aleatorio entre 1 y 100 (inclusive) y lo devuelve.
    """
    numeros = list(range(101))  # Genera una lista de números del 0 al 100
    secreto = random.choice(numeros)  # Selecciona un número aleatorio de la lista
    return secreto


def adivina(secreto):
    """
    Esta función permite al usuario adivinar un número secreto entre 1 y 100.
    """
    intentos = 0
    print("¡Adivina el número que estoy pensando entre 1 y 100!")

    while True:
        try:
            intento = int(input(f"Intento N° {intentos + 1}: "))
            if intento == secreto:
                print("¡Felicidades! Has adivinado el número.")
                break
            elif intento < secreto:
                print("El número que estás pensando es mayor.")
            else:
                print("El número que estás pensando es menor.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        finally:
            intentos += 1

    print(f"¡Lo lograste en {intentos * 10} intentos!\n")


nombre_jugador = "Invitado"  # Se ha cambiado el nombre predeterminado a "Invitado"


def jugar():
    """
    Esta función controla el flujo principal del juego de adivinanzas.
    """
    while True:
        print("¡Bienvenido al Juego de Adivinanzas del Python Study Group 2024!")
        print("=" * 63)
        nombre_jugador = input("¿Cuál es tu nombre?: ")
        print(f"¡Bienvenido, {nombre_jugador}!")
        print("=" * 63)
        print()
        opcion = input("¿Quieres jugar? (s/n): ")
        if opcion.lower() != "s":
            break

        secreto = obtener_aleatorio()
        adivina(secreto)

    print("¡Gracias por participar!")
    print(f" ¡Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2024! ")


jugar()  # Se llama a la función jugar para iniciar el juego
