import turtle as t
from digital_tube import digital_tube
from datetime import datetime
import time

DELAY_TIME = 0.8

TUBES_POS = [
    (-500, -100),
    (-350, -100),
    (-125, -100),
    (25, -100),
    (250, -100),
    (400, -100),
]
COL_POS = [(-180, -100), (192, -100)]


def re_draw(char: str, pen: t.Turtle):
    pen.clear()
    digital_tube(char, font=(200, "normal"), pen=pen)
    time.sleep(0.05)


t.Screen().tracer(0)
t.Screen().delay(0)
t.Screen().bgcolor(0.8, 0.82, 0.85)
t.speed(0)
t.pensize(1)
t.hideturtle()
t.color(0.2, 0.22, 0.25)
t.penup()

for pos in COL_POS:
    t.goto(pos)
    t.clone().write(":", align="center", font=("Yahei", 200, "normal"))

tubes = [t.clone() for _ in range(6)]
for i, pos in enumerate(TUBES_POS):
    tubes[i].goto(pos)
    bg = tubes[i].clone()
    bg.color(0.75, 0.77, 0.8)
    digital_tube("8", font=(200, "normal"), pen=bg)
past_time = "xxxxxx"
try:
    while True:
        now_time = datetime.now().strftime("%H%M%S")
        for i in range(6):
            if now_time[i] != past_time[i]:
                re_draw(now_time[i], tubes[i])
                changed = True
        past_time = now_time
        t.update()
        if changed:
            time.sleep(DELAY_TIME)
        changed = False
except t.Terminator:
    print("Already terminated.")
