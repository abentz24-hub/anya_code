#lesson 3-1.py

import turtle 

wn = turtle.Screen()  #creates a screen window
wn.bgcolor("purple")
bob = turtle.Turtle() #creates a turtle object
bob.color("teal")
bob.pensize(5)


# bob.forward(300)
# bob.right(90)
# bob.forward(100)
# bob.right(90)
# bob.forward(300)
# bob.right(90)
# bob.forward(100)
# bob.right(90)

# bob.left(60)
# bob.backward(100)

# bob.penup() #pick up the pen
# bob.goto(-100,100) #go to this x,y coordinate
# bob.pendown() #put pen down
# bob.hideturtle()
# bob.showturtle()
# bob.forward(100)

#draw an equilateral triangle
bob.begin_fill()
for i in range(3):
    bob.forward(200)
    bob.left(120)
bob.end_fill()






wn.exitonclick()
