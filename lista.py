# Listas
# Las listas se tratan de un tipo compuesto de dato que puede
# almacenar distintos valores (llamados ítems o elementos)
# ordenados entre [ ] y separados con comas:

numeros = [1, 2, 3, 4]

# print(numeros)

# Índices y slicing
# Funcionan de una forma muy similar a las cadenas de caracteres:

datos = [4, "Una cadena", -15, 3.14, "Otra cadena"]
# print(datos)

# print(datos[0])
# print(datos[-1])
# print(datos[2:])
# print(datos[:2])


# Suma de listas
# Da como resultado una nueva lista que incluye todos los ítems:
#print(numeros + [5, 6, 7, 8])

# Mutabilidad
# A diferencia de las cadenas, en las listas sí podemos modificar
# sus ítems utilizando índices:
pares = [0, 2, 4, 5, 8, 10]
# print(pares)
pares[3] = 6
# print(pares)

# Integran funcionalidades internas como el método .append()
# para añadir un ítem al final de la lista:

pares.append(12)
# print(pares)
pares.append(7)
# print(pares)
pares.append(7*2)
# print(pares)

# Y una peculiaridad es que también aceptan asignación
# con slicing para modificar varios ítems en conjunto:

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3]
# print(letras)
letras[:3] = ['A', 'B', 'C']
letras
# print(letras)

# Asignar una lista vacía equivale a borrar los ítems de la lista
# o sublista:

letras[:3] = []
letras
#print("lista vacía")
letras = []
# print(letras)

# La función len() funciona con las listas del mismo modo
# que en las cadenas:

# print(len(letras))
# print(len(pares))

# Listas anidadas
# Podemos manipular fácilmente este tipo de estructuras utilizando
# múltiples índices, como si nos refieréramos a las filas y columnas
#  de una tabla:

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
r = [a, b, c]

print(r)

print(r[0])       # Primera sublista
# print(r[-1])      # Última sublista
print(r[0][0])
print(r[0][1])
print(r[0][2])
# print(r[0][0])    # Primera sublista, y de ella, primer ítem
# print(r[1][1])    # Segunda sublista, y de ella, segundo ítem
# print(r[2][2])    # Tercera sublista, y de ella, tercer ítem
# print(r[-1][-1])  # Última sublista, y de ella, último ítem
