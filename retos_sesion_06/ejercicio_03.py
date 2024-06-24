"""
Sesión 06
Ejercicio 03

Imprime una tabla de verdad para la siguiente afirmación: "Una puerta tiene dos interruptores 
que controlan dos luces, la puerta sólo debe abrirse cuando las dos luces están apagadas o las 
dos están encendidas, caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?"
"""

# Table de verdad
print(False and False)  # La puerta se abre
print(True and False)  # La puerta se no se abre
print(False and True)  # La puerta se no se abre
print(True and True)  # La puerta se abre

# Ejemplo
luz_1 = False
luz_2 = False

puerta = luz_1 == luz_2  # Operación XNOR

if puerta: # Si la comparación de puerta es True, la puerta se abrirá
    print("La puerta se abrirá")
else:
    print("La puerta no se abirá")
