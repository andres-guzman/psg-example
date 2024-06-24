"""
Sesión 12
Ejercicio 04

Una tienda ofrece descuentos a sus clientes, si el cliente es 
mayor de edad y tiene una compra mayor a 1000, se le aplica un 
descuento del 10%, si es menor de edad y tiene una compra mayor 
a 500 se le aplica un descuento del 5%, si no cumple ninguna 
condición se le aplica un descuento del 2%
"""

# Pedimos al usuario que ingrese su edad y el monto de su compra
# (También podríamos almacenar ambos valores en variables)
edad_cliente = int(input("Ingrese su edad: "))
monto_compra = float(input("Ingrese el monto de su compra: $"))

# Calcular el descuento
if edad_cliente >= 18 and monto_compra > 1000:
    descuento = 0.1  # 10% de descuento
elif edad_cliente < 18 and monto_compra > 500:
    descuento = 0.05  # 5% de descuento
else:
    descuento = 0.02  # 2% de descuento

# Calcular el monto final
monto_final = monto_compra - (monto_compra * descuento)

# Mostrar el resultado
print("Su descuento es del", descuento * 1000)
print("El monto final a pagar es de: $", monto_final)
