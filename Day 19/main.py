from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(20)


def move_back():
    timmy.back(20)


def turn_right():
    timmy.right(10)


def turn_left():
    timmy.left(10)


def clearScreen():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clearScreen)
screen.exitonclick()



