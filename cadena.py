print("Una cadena")
print('otra cadena')
print('otra cadena más')

# Acepta caracteres especiales como las tabulaciones \t o los saltos de línea \n:
print("Un texto\tuna tabulación")
print("Un texto\nuna nueva línea")


# Para evitar los caracteres especiales, debemos indicar que una cadena es cruda (raw):
print("C:\nombre\directorio")
print(r"C:\nombre\directorio")  # r(cadena) => raw (cruda)

# Operaciones
# Una de las operaciones de las cadenas es la concatenación(o suma de cadenas):
c = "Esto es una cadena\ncon dos líneas"
c + c
print(c+c)

# Una cadena compuesta de dos cadenas
c1 = "Una cadena"
c2 = "otra cadena"
print("Una cadena " + c2)

# Índices en las cadenas
# Los índices nos permiten posicionarnos en un carácter específico de una cadena.
# Representan un número [índice], que empezando por el 0 indica el carácter
# de la primera posición, y así sucesivamente:

palabra = "Python"
print(palabra[2])  # carácter en la posición 0

# print(palabra[3])

# El índice negativo -1, hace referencia al carácter de la última posición,
#  el -2 al penúltimo y así sucesivamente:
print("El índice negativo -1")
print(palabra[-1])

# Slicing en las cadenas
# El slicing es una capacidad de las cadenas que devuelve un subconjunto 
# o subcadena utilizando dos índices[inicio:fin]:

# El primer índice indica donde empieza la subcadena(se incluye el carácter).
# El segundo índice indica donde acaba la subcadena(se excluye el carácter).

palabra = "Python"
print("Slicing en las cadenas Python [0:4]")
print(palabra[0:4])

# Inmutabilidad
# Una propiedad de las cadenas es que no se puede modificar
# su contenido. Si intentamos reasignar un carácter,
# no nos dejará:

palabra[0] = "N"
print(palabra[0])
