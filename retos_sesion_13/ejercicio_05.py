"""
Sesión 13
Ejercicio 05

Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
"""

# Podemos definir el tamaño del tablero
tamano = 8

# Bucle para cada fila
for fila in range(tamano):
    # Cadena para almacenar la fila actual
    fila_caracter = ""

    # Bucle para cada columna
    for columna in range(tamano):
        # Determinar el caracter de la casilla
        if (fila + columna) % 2 == 0:
            caracter = "#"
        else:
            caracter = "*"

        # Agregar el caracter a la cadena de la fila
        fila_caracter += caracter

    # Imprimir la fila completa
    print(fila_caracter)
