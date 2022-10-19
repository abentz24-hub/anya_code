#function_intro.py

import turtle as t
wn=t.Screen()
wn.bgcolor("lightgreen")

bob=t.Turtle()
bob.color("hotpink")
bob.pensize(5)



def draw_square(turtle,length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

#drwaing picture

# for i in range(5):
#     draw_square(bob,20)
#     bob.penup()
#     bob.forward(20)
#     bob.pendown()

length = 20
x= -10
y= -10
for i in range(5):
    draw_square(bob,length)
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    lenght = length + 20
    x=x-10
    y=y-10

# for i in range (1,6):
#     draw_square(bob, i*20)
#     bob.penup()
#     bob.goto( i * -10, i * -10)
#     bob.pendown()




wn.exitonclick()