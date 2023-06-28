import turtle
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angle,shift,shape):
    turtle.bgcolor(next(colors))
    next_shape ==''
    if shape =='Circle':
        turtle.Circle(Size)
        next_shape = 'square'
    elif shape == 'square':
        for in range(4):
            turtle.forward(size + 2)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_Shape(size+5, angle+1, shift+1, next_shape)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_CIRCLE(30, 0, 1, 'Circle')
