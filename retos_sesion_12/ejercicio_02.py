"""
Sesión 12
Ejercicio 02

Tienes una página web y un usuario quiere acceder a ella, 
verifica si el usuario inició sesión para acceder a la página, 
caso contrario muestra un mensaje de error
"""

# Alamcenamos el email del usuario
email_almacenado = "usuario@email.com"

# Pedimos al usuario que ingrese su email
email_ingresado = input("Ingrese su correo electrónico: ")

# Si el email ingresado es igual al email almacenado
# imprimimos el mensaje de éxito
if email_ingresado == email_almacenado:
    print("Ya iniciaste sesión.")
    # Si el email ingresado está vacio:
elif email_ingresado == "":
    print("No ha ingresado ningún correo electrónico.")
    # Si el email ingresado no es igual al almacenado, error:
else:
    print("Error, el email no coincide.")
