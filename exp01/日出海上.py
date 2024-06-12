SKY_COLOR_START = (0, 146, 246)
SKY_COLOR_END = (0, 146, 246)
SUN_COLOR = (161, 35, 24)
SEA_COLOR_LIGHT = (255, 255, 255)
SEA_COLOR_DARK = (13, 27, 161)

import turtle as t

t.speed(0)
t.hideturtle()
t.colormode(255)


def setcolor(start, end, step=0.5, qu=1, qucolor="black"):
    if (
        len(start) != 3
        or len(end) != 3
        or step < 0
        or step > 1
        or type(qu) != type(1)
        or qu < 1
    ):
        raise Exception("setcolor 函数传入值错误")
    for i in start:
        if i < 0 or i > 255 or type(i) != type(1):
            raise Exception("setcolor 函数传入值错误")
    newcolor = []
    for i in range(3):
        newcolor.append(int((1.0 - step) * start[i] + step * end[i]))
    newcolor = tuple(newcolor)
    if qu == 1:
        return newcolor
    op = []
    if qucolor == "black":
        qucolor = (0, 0, 0)
    elif qucolor == "white":
        qucolor = (255, 255, 255)
    else:
        raise Exception("qucolor 仅限传入 black 或 white")
    for i in range(qu, 0, -1):
        onecolor = []
        for j in range(3):
            onecolor.append(int(i / qu * newcolor[j] + (1.0 - i / qu) * qucolor[j]))
        op.append(tuple(onecolor))
    return op


def sky():
    t.up()
    t.seth(0)
    t.pensize(3)
    t.goto(-200, 149)
    c = setcolor(SKY_COLOR_START, SKY_COLOR_END, qu=100, qucolor="white")
    t.down()
    for i in range(100):
        t.pencolor(c[i])
        t.fd(400)
        t.up()
        t.goto(-200, 149 - 3 * i)
        t.down()


def sun(center=(0, 0), r=50):
    t.up()
    t.seth(0)
    t.goto(center[0], center[1] - r)
    t.pensize(1)
    t.pencolor(SUN_COLOR)
    t.fillcolor(SUN_COLOR)
    t.down()
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def sea(center, r, plies=9):
    psize = r / plies
    t.pensize(psize)
    r = psize / 2
    for i in range(plies):
        t.up()
        t.seth(90)
        t.goto(center[0] + r, center[1])
        if i % 2 == 0:
            t.pencolor(SEA_COLOR_DARK)
        else:
            t.pencolor(SEA_COLOR_LIGHT)
        t.down()
        t.circle(r, 180)
        r = r + psize


sky()
sun(center=(0, 0))
for y in range(-50, -151, -25):
    for x in range(-200, 201, 50):
        sea((x, y), 25)
    for x in range(-175, 176, 50):
        sea((x, y - 12.5), 25)
t.up()
t.goto(-250, 200)
t.pensize(100)
t.pencolor(255, 255, 255)
t.seth(0)
t.down()
for i in range(2):
    t.fd(500)
    t.right(90)
    t.fd(400)
    t.right(90)
t.done()
