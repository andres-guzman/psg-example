"""
Sesión 15
Ejercicio 03

Simular un cajero automático que solicite un monto a retirar, 
si el monto es mayor al saldo lanzar una excepción personalizada 
y si el monto es mayor a 1000 lanzar una excepción genérica
"""

# Funcion para retirar dinero
def reitar_dinero(saldo):
    """Simula la transacción de un cajero automático."""
    try:
        cantidad_a_retirar = float(input("Ingrese el monto que desea retirar: $"))

        if cantidad_a_retirar > saldo:
            raise Exception("Saldo insuficiente.")

        if cantidad_a_retirar > 1000:
            raise Exception("Limite excedido. Consulte a un representante.")

        print(f"Retirando ${cantidad_a_retirar:}...")
        saldo -= cantidad_a_retirar
        print(f"Su nuevo saldo es: ${saldo:}")

    except ValueError as error:
        print("Error:", error, "Ingrese un monto válido.")
    except Exception as error:
        print("Error:", error, "Consulte a un representante.")


saldo = 500  # Saldo inicial

# Llamamos a la función
reitar_dinero(saldo)
