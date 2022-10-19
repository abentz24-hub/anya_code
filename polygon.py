#polygon.py
import turtle
#get user input
sides = int(input("please input the number of sides:"))
length = int (input("please input the length of sides:"))
color = (input("enter the color of the pen:"))
fill = (input("enter the fill color:"))

#define variables

wn = turtle.Screen() #creates a screen window
lance = turtle.Turtle() #creates a turtle
lance.pencolor(color) #sets pencolor and fill color
lance.fillcolor(fill)

lance.begin_fill()



for i in range(sides):
    lance.forward(length)
    lance.left(360/ sides)

lance.end_fill()

wn.exitonclick()

