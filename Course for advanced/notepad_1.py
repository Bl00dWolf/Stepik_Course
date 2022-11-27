import turtle


def rectangle(width, height):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)


def triangle(side):
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)


def square(side):
    rectangle(side, side)


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


def romb(side):
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)


for _ in range(12):
    turtle.forward(200)
    turtle.backward(200)
    turtle.left(25)

input()
