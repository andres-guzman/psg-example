# Conjuntos

print("Conjunto de enteros")
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
print(type(conjunto))

print("Conjunto de cadenas")
conjunto = {'🍕', '🍔', '🍟', '🌭'}
print(conjunto)
print(type(conjunto))

print("Conjunto mixto")
conjunto = {1, True, 3.14, '☕'}
print(conjunto)
print(type(conjunto))

print("Conjunto vacío")
conjunto = set()
print(conjunto)
print(type(conjunto))

print("Conjunto a partir de la cadena")
cadena = 'Hola Mundo'
conjunto = set(cadena)
print(conjunto)
print(type(conjunto))

print("Conjunto a partir de una tupla")
tupla = (1, 2, 3, 4, 5, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

print("Conjunto a partir de una lista")
lista = [True, False, 0, 1]
conjunto = set(lista)
print(conjunto)
print(type(conjunto))

print("Conjunto por comprensión")
conjunto = {x for x in '🍕🍔🍟🍕🍔🍟🍔🍟'}
print(conjunto)
print(type(conjunto))

# conjunto = {1, 2, 3, 4, 5}
# print(conjunto[0]) # TypeError: 'set' object is not subscriptable

# conjunto = {1, 2, 3, 4, 5}
# print(conjunto[0:3]) # TypeError: 'set' object is not subscriptable

# conjunto1 = {1, 2, 3}
# conjunto2 = {4, 5, 6}
# print(conjunto1 + conjunto2)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

# conjunto = {1, 2, 3}
# print(conjunto * 3)
# TypeError: unsupported operand type(s) for *: 'set' and 'int'

print("Método add()")
conjunto = {'🍕', '🍔', '🍟', '🌭'}
print(conjunto)
conjunto.add('🥗')
print(conjunto)

print("Método update()")
conjunto = {'🍕', '🍔', '🍟', '🌭'}
print(conjunto)
conjunto.update(['🥤', '🍦'])
print(conjunto)
conjunto.update('🍩🍪')
print(conjunto)
conjunto.update(('🍫', '🍬'))
print(conjunto)
conjunto.update({'🍭', '🍮'})
print(conjunto)

print("Método remove()")
conjunto = {'🍕', '🍔', '🍟', '🌭'}
print(conjunto)
conjunto.remove('🍔')
print(conjunto)
# conjunto.remove('🍔')
# print(conjunto)
# Key Error: '🍔'

print("Método discard()")
conjunto = {'🍕', '🍔', '🍟', '🌭'}
print(conjunto)
conjunto.discard('🍔')
print(conjunto)
conjunto.discard('🍔')
print(conjunto)

print("Método pop()")
conjunto = {'🍕', '🍔', '🍟', '🌭', '🥤', '🍦'}
print(conjunto)
print(conjunto.pop())
print(conjunto)
print(conjunto.pop())
print(conjunto)

print("Método clear()")
conjunto = {'🍕', '🍔', '🍟', '🌭'}
print(conjunto)
conjunto.clear()
print(conjunto)

print("Método union()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print(conjunto1, conjunto2)
union = conjunto1.union(conjunto2)
print(union)

print("Método intersection()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print(conjunto1, conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

print("Método difference()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print("1:", conjunto1, "2:", conjunto2)
diferencia = conjunto1.difference(conjunto2)
print("1 y 2:", diferencia)
diferencia = conjunto2.difference(conjunto1)
print("2 y 1:", diferencia)

print("Método symmetric_difference()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print(conjunto1, conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)

print("Método intersection_update()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print(conjunto1, conjunto2)
conjunto1.intersection_update(conjunto2)
print(conjunto1)

print("Método difference_update()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print("1:", conjunto1, "2:", conjunto2)
conjunto1.difference_update(conjunto2)
print("1:", conjunto1, "2:", conjunto2)

print("Método symmetric_difference_update()")
conjunto1 = {'🍔', '🍟', '🥤'}
conjunto2 = {'🍕', '🍨', '🥤'}
print(conjunto1, conjunto2)
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)
