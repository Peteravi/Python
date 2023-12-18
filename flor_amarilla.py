import turtle
import math

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto Turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("green")
flower.speed(10)

# Función para dibujar un pétalo
def draw_petal():
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Dibuja el tallo de la flor
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.color("green")
flower.begin_fill()
flower.forward(100)
flower.left(90)
flower.forward(200)
flower.left(90)
flower.forward(100)
flower.left(90)
flower.forward(200)
flower.end_fill()

# Dibuja los pétalos de la flor
flower.penup()
flower.goto(0, 0)
flower.pendown()
flower.color("yellow")
flower.begin_fill()
for _ in range(6):
    draw_petal()
    flower.left(60)
flower.end_fill()

# Mostrar el mensaje "Te quiero mucho"
flower.penup()
flower.goto(0, -250)
flower.color("black")
flower.write("Te quiero mucho", align="center", font=("Arial", 20, "normal"))

# Cierra la ventana al hacer clic
screen.exitonclick()