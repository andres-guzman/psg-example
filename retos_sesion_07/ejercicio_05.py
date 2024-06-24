"""
Sesión 07
Ejercicio 05

Escribe un programa que reciba una cadena y retorna verdadero o falso si es 
palindrome la frase o palabra ejemplo "Anita lava la Tina" es verdad
"""

# Recibir texto del usuario
texto_del_usuario = input("Ingrese una cadena de texto: ")

# Convierte la cadena en minúsculas y remueve espacios en blanco (para frases con espacios)
texto_mejorado = texto_del_usuario.lower().replace(' ', '')

# Asigna el valor del texto mejorado al texto invetido
texto_invertido = texto_mejorado[::-1]

# Imprimir el resultado
if texto_mejorado == texto_invertido: # Compara ambas cadenas
    print(f"La cadena '{texto_del_usuario}' es un palíndromo")
else:
    print(f"La cadena '{texto_del_usuario}' no es un palíndromo")
