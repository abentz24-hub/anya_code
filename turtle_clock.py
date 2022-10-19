#turtle_clock.py

import turtle
#configure turtle objects
wn = turtle.Screen()
wn.bgcolor("light green")

lance = turtle.Turtle()
lance.color("blue")
lance.shape("turtle")

#drawing a clock
for i in range(12):
    lance.penup()
    lance.forward(100)
    lance.pendown()
    lance.forward(10)
    lance.penup()
    lance.forward(20)
    lance.stamp()
    lance.backward(130)
    lance.right(360 / 12)




wn.exitonclick()