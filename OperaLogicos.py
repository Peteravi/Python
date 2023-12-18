# Operadores lógicos
# Encontramos 3 operadores especiales para realizar operaciones lógicas.
# Normalmente se utilizan para agrupar, excluir y negar expresiones.
# Puede ayudar echar un vistazo a esta explicación sobre las tablas de la verdad:

# Not
# And
# Or

# Not (Negación lógica)
# Niega un valor o expresión lógica:
print(True)
print(not True)
print(not False)
print(not True == False)

# And (Conjunción lógica)
# Devuelve verdadero sólo si se cumplen todas las condiciones:

True and True
True and False
False and True

c = "Hola Mundo"
print("Hola Mundo")
print(not len(c) >= 20 and c[0] == "H")


# Or(Disyunción lógica)
# Devuelve verdadero si se cumple como mínimo una condición:

True or True
True or False
False or True
False or False

print("OTRA COSA")
c = "OTRA COSA"
print(c == "EXIT" or c == "FIN" or c ==
      "SALIR" or c == "OTRA COSA" and c == "Hola")
