import turtle

from itertools import cycle
colors = cycle(['Peach Puff','Misty Rose','Deep Pink','Lemon Chiffon','Aquamarine','Gold'])

def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+8,angle+2,shift+3)

turtle.bgcolor('Navy')
turtle.speed('fast')
turtle.pensize(80)
draw_circle(30,0,1)
