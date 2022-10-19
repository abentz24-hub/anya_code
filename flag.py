#flag.py
# -----------------------------------------+
  # Anya Bentz                               |  
  # Computer Science, Project 4              |
  # Last Updated: 10/19/22                   |  
  # -----------------------------------------|
  #                                          |
  #                                          | 
  # -----------------------------------------+

import turtle
window = turtle.Screen()
flag = turtle.Turtle()
flag.hideturtle()
flag.speed(0)

# Your functions go here 
def draw_rectangle(turtle, color, length, width, x, y):
  turtle.color(color)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
  turtle.end_fill()


def draw_star(turtle,color, length, x,y):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.color("White")
  turtle.begin_fill()
  for i in range(5):
    turtle.forward(length)
    turtle.right(144)
  turtle.end_fill()


# initially, make the background of the entire flag black
# the dimensions of the flag are 450 by 330
# the upper left corner of the flag is at (-225, 165)
draw_rectangle(flag, "black", 450, 330, -225, 165)

# draw the yellow and red stripes
y = 110
for i in range(2):
    draw_rectangle(flag, "yellow", 450, 55, -225, y)
    draw_rectangle(flag, "red", 450, 55, -225, y - 55)
    y = y - 165

# draw the black square in the center
draw_rectangle(flag, "green", 180, 180, -90, 90)

# draw the 13 white stars
flag.penup()
flag.goto(-70, 10)
for i in range(13):
    # each of the 5 lines of the star is 20 pixels
    # the left side of the horizontal line is at (flag.xcor(), flag.ycor())
    draw_star(flag, "white", 20, flag.xcor(), flag.ycor())
    flag.penup()
    flag.forward(140)
    flag.right(180 - 180/13)

window.exitonclick()