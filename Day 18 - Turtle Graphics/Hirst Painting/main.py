# import colorgram
import random
import turtle
from turtle import Turtle, Screen

# colors = colorgram.extract("image.jpg", 42)

# for i in range(len(colors)):
# color_list.append(colors[i].rgb[0::])
#
# print(color_list)


color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83),
              (245, 205, 7), (35, 88, 88), (103, 24, 56)]

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.hideturtle()


def start_point(x, y):
    """Move the turtle to a desired coordinate on the screen and start drawing from there.
        x and y are 2D coordinates"""
    # timmy.hideturtle()
    timmy.penup()
    timmy.goto(x, y)
    # timmy.showturtle()



def move_forward(diameter, paces):
    """Move turtle forward with desired pace and with dots of desired diameter"""
    for d in range(10):
        random_color = random.choice(color_list)
        # timmy.pencolor(random_color)
        timmy.dot(diameter, random_color)
        timmy.penup()
        timmy.forward(paces)




def next_row(x, y):
    """Move turtle to the next row from its starting point. Inputs are coordinates for
        turtle's start point."""
    # timmy.hideturtle()
    timmy.goto(x, y)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.right(90)
    # timmy.showturtle()


start_point(-200, -200)
y_ext = -200
for i in range(10):
    move_forward(20, 50)
    next_row(-200, y_ext)
    y_ext += 50  # Increase the y-coordinate by 50 each time to not be stuck looping to the same coordinate











Screen().exitonclick()
print(timmy)
