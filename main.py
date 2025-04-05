# Spirograph
# draw circles
# tilt circles

from turtle import *
import random

t = Turtle()
screen = Screen()
# Set colormode to apply the RGB coloring system
screen.colormode(255)
screen.bgcolor("black")

t.pensize(1)
t.speed(0)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return_tuple = (r, g, b)
    return return_tuple


for i in range(200):
    t.circle(100)
    t.left(10)

    t.color(colors())


screen.exitonclick()
