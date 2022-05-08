## 2021041035 조민규
import turtle
import random

def screenRightClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    angle = random.randrange(0, 360)
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    turtle.color(r, g, b)
    turtle.left(angle)
    turtle.stamp()

pSize = 10

turtle.title('거북이 도장 찍기')
turtle.shape('turtle')
turtle.pensize(10)

turtle.onscreenclick(screenRightClick, 3)

turtle.done()
