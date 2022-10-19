#square_sprite.py
import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.color("LightPink2")
bob.speed(0)
#center square
bob.penup()
bob.goto(-100,100)
bob.pendown()
for i in range(4):
    bob.forward(200)
    #draw sprite
    for i in range(8):
        bob.forward(30)
        bob.back(30)
        bob.left(360/8)
    


    bob.right(90)

wn.exitonclick()
