import turtle
colores=[ 'deep pink','springGreen2','mediumblue','green2','orange red','gold']

t=turtle.Pen()
turtle.bgcolor('black')
for i in range (200):
    t.pencolor(colores[i%6])
    t.width(i/80+1)
    t.forward(i)
    t.left(59)
turtle.mainloop()
