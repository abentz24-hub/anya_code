#fancy_sqaure.py

import turtle
wn = turtle.Screen()
turtle= turtle.Turtle()
wn.bgcolor("LightPink")
turtle.speed(0)
turtle.pensize(5)
turtle.color("CadetBlue3")

def rectangle_area(length,width):
    area = length * width
    return area

def draw_sprite(turtle,legs,length):
    for i in range(legs):
        turtle.forward(length)
        turtle.backward(length)
        turtle.right(360/legs)

draw_sprite(turtle,8,100)

def fancy_square(turtle,length):
    for i in range(4):
        turtle.forward(length)
        draw_sprite(turtle,8,100)
        turtle.right(90)

fancy_square(turtle, 300)


wn.exitonclick()