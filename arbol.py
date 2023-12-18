import turtle
import random
import numpy as np

def dibujar_arbol(niveles, x, y):
    # Configurar la velocidad de la tortuga
    turtle.speed("fastest")

    # Posicionar el árbol
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Dibuja las ramas
    dibujar_rama(niveles, 100)

    # Dibuja el tronco
    turtle.color("saddlebrown")
    turtle.pensize(20)
    turtle.left(90)
    turtle.forward(100)

    # Dibuja el mensaje
    turtle.penup()
    turtle.goto(x, y - 220)  # Ajusta la posición vertical del mensaje
    turtle.color("darkred")
    turtle.write("¡Feliz Navidad y Próspero 2024!", align="center", font=("Arial", 18, "bold"))

    # Dibuja las decoraciones
    for i in range(1, niveles + 1):
        if random.random() < 0.5:
            dibujar_decoracion("estrella", (random.randint(x - 40, x + 40), y + i * 20))
        if random.random() < 0.3:
            dibujar_decoracion("bola", (random.randint(x - 40, x + 40), y + i * 20))

    # Añade animación de luces y copos de nieve
    for _ in range(10):
        luces(x, y + niveles * 20)
        copos_nieve(x, y + niveles * 20)

    turtle.done()

def dibujar_rama(nivel, longitud):
    if nivel == 0:
        return
    else:
        colores = ["#8B4513", "#228B22", "#228B22", "#228B22"]  # Colores para las ramas
        turtle.pensize(max(1, nivel // 2))
        turtle.color(random.choice(colores))
        turtle.forward(longitud)
        turtle.left(45)
        dibujar_rama(nivel - 1, longitud * 0.6)
        turtle.right(90)
        dibujar_rama(nivel - 1, longitud * 0.6)
        turtle.left(45)
        turtle.backward(longitud)

def dibujar_decoracion(tipo, posicion):
    if tipo == "estrella":
        turtle.penup()
        turtle.goto(posicion)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("yellow")
        for _ in range(5):
            turtle.forward(15)
            turtle.right(144)
        turtle.end_fill()
    elif tipo == "bola":
        turtle.penup()
        turtle.goto(posicion)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(random.choice(["red", "green", "blue", "yellow", "purple", "orange"]))
        turtle.circle(5)
        turtle.end_fill()

def luces(x, y):
    turtle.penup()
    turtle.goto(x + random.randint(-40, 40), y + random.randint(0, 30))
    turtle.pendown()
    turtle.dot(random.randint(5, 15), random.choice(["red", "green", "blue", "yellow"]))

def copos_nieve(x, y):
    turtle.penup()
    turtle.goto(x + random.randint(-200, 200), y + random.randint(-100, 100))
    turtle.pendown()
    turtle.color("white")
    turtle.dot(random.randint(2, 5))

if __name__ == "__main__":
    niveles = 5  # Puedes ajustar el número de niveles según tu preferencia
    dibujar_arbol(niveles, 0, 0)  # Puedes ajustar las coordenadas (x, y)