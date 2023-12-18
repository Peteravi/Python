# Condiciones
# Condicionar permite dividir el flujo de un programa en diferentes
# caminos.
# Sentencia if (si)
# El if se ejecuta siempre que la expresión que comprueba
# devuelva True:

# if True:  # equivale a if not False
#    print("Se cumple la condición")
#    print("También se muestre este print")

# Podemos encadenar diferentes If:
#a = 5
# if a == 2:
#    print("a vale 2")
# if a == 5:
#    print("a vale 5")


# O también anidar If dentro de If:
a = 5
b = 10
if a == 5:
    print("a vale", a)
    if b == 10:
        print("y b vale", b)


if a == 5:
    print("a vale", a)
if b == 10:
    print("y b vale", b)


# Como condición podemos evaluar múltiples expresiones,
# siempre que éstas devuelvan True o False:
if a == 5 and b == 10:
    print("a vale 5 y b vale 10")


# Sentencia else (sino)
# Se encadena a un If para comprobar el caso
# contrario(en el que no se cumple la condición):

n = 11
if n % 2 == 0:
    print(n, "es un número par")
else:
    print(n, "es un número impar")


# Sentencia elif (sino si)
# Se encadena a un if u otro elif para comprobar múltiples condiciones,
#  siempre que las anteriores no se ejecuten:

comando = "OTRA COSA"

if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que te lo estés pasando bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema...")
else:
    print("Este comando no se reconoce")

print("*******************")
# ingresar por teclado
nota = float(input("Introduce una nota: "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")


# Instrucción pass
# Sirve para como instrucción de paso para utilizar en un bloque
# de código vacío, no finaliza el código. No tiene ningún efecto
# pero sirve para crear estructuras pendientes
# de ser programadas:

if True:
    pass
