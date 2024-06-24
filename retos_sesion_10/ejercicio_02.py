"""
Sesión 10
Ejercicio 02

El dueño de un restaurante de comida Mexicana ha decidido comprar un 
restaurante de comida Italiana y abrir un nuevo restaurante de comida fusion. 
La apertura esta a la vuelta de la esquina y aun no hay podido actualizar el Menu, 
Ayuda a actualizar su menu de platos disponibles

menu_mexicano: "Tacos", "Enchiladas", "Guacamole", "Tamales"
menu_italiano: "Pizza", "Pasta", "Lasagna", "Tiramisú"
"""

# Menús de comida actuales
menu_mexico = {"Tacos", "Enchiladas", "Guacamole", "Tamales"}
menu_italia = {"Pizza", "Pasta", "Lasagna", "Tiramisú"}

# Menú fusión
menu_fusion = set() # Crea un set vacío para ser llenado luego
menu_fusion.update(menu_mexico) # Actualiza en set vacio con el menú de Mexico
menu_fusion.update(menu_italia) # Actualiza el set con el menú de Italia

# Imprime el nuevo menú
print(menu_fusion)
