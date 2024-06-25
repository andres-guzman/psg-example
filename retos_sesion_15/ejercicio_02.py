"""
Sesión 15
Ejercicio 02

Crear un programa para crear una canasta de frutas, solicitar 
frutas por teclado y almacenar en una lista, si se ingresa "salir" 
termina la ejecución. Solo se permiten las siguientes frutas caso 
contrario lanzar una excepción personalizada

🍅🍇🍈🍉🍊🍌🍍🍑
"""

# Creamos la función
def crear_canasta():
    """Crea una canasta de futas y permite a los usuarios añadir frutas."""
    canasta_de_frutas = []

    while True:
        fruta = input("Ingrese una fruta ('salir' para terminar): ")

        if fruta == "salir":
            break

        frutas_permitidas = ""  # Frutas permitidas

        for emoji in frutas_validas:
            frutas_permitidas += f"{emoji} "

        if fruta not in frutas_permitidas:
            print(f"Fruta inválida: {fruta}. Frutas válidas: {frutas_permitidas}")
            continue  # Salta a la siguiente fruta si se ingresa algo inválido

        canasta_de_frutas.append(fruta)

    print("Cesta de frutas final:")
    for fruta in canasta_de_frutas:
        print(fruta)

frutas_validas = "🍅🍇🍈🍉🍊🍌🍍🍑"  # Emojis de furtas válidas

# Llamamos a la función
crear_canasta()
