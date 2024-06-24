"""
Sesión 08
Ejercicio 03

Ingresa una cadena por teclado y almacena el valor en una tupla

Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
Imprime el resultado concatenado
Repite la tupla final 3 veces e imprime el nuevo resultado
"""

# Ingresar un texto
texto_del_usuario = input("Ingrese un texto: ")
# Almacenar el texto en un a tupla
texto_a_tupla = (texto_del_usuario,)

# Concatenar ¡ y ! al texto ingresado
texto_concatenado = ('¡',) + texto_a_tupla + ('¡',)
# Imprimir el texto concatenado
print(texto_concatenado)

# Repetir la tupla concatenada 3 veces e imprimir resultado
print(texto_concatenado * 3)
