import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.color("purple")
# timmy.pensize(5)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    selected_color = (r, g, b)
    return selected_color


def draw_spirograph(size_of_gap):

    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(4)











# This is a spirograph donut😁

# for i in range(200):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.tilt(7)
#     timmy.left(7)
#     timmy.forward(7)















Screen().exitonclick()
print(timmy)















# sides = 3
# while sides < 11:
#     timmy.penup()
#     timmy.goto(0, 300)
#     timmy.pendown()
#     math = 360 / sides
#     timmy.color(random.choice(color))
#     for i in range(sides):
#         timmy.forward(100)
#         timmy.right(math)
#         timmy.forward(100)
#
#       sides += 1
