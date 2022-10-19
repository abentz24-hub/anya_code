#ppr1.py

#1
#solution
#user input
# radius = input("the radius of the cylinder")
# radius = float(radius)
# height = input("the height of the cylinder")
# height = float(height)
# #calculate
# area = 2 * 3.1415 * radius * radius + height *( 2 * 3.1415 * radius)
# #print statement
# print("the are of the cylinder is:", area )

#2
#solution
# import turtle
# wn = turtle.Screen()
# shape = turtle.Turtle()
# for i in range (4):
#     shape.forward(10)
#     shape.right(90)
#     shape.forward(10)
#     shape.left(90)
# wn.exitonclick()

#3
#solution
# import turtle
# wn = turtle.Screen()
# bob = turtle.Turtle()
# bob.color("red")
# bob.penup()
# bob.goto(0,0)
# bob.begin_fill()
# bob.pendown()
# bob.goto(80,0)
# bob.goto(0,60)
# bob.end_fill
#wn.exitonclick()

#4
#solution
#user input
from sre_constants import ANY_ALL


first_name=input("Please enter your first name")
last_name=input("Please enter your last name")
characters=len(first_name+last_name)
print("The number of chatacters in", first_name,last_name"is",characters)
