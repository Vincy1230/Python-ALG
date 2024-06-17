import turtle as t
import random as rd

t.delay(0)
t.speed(0)
t.bgcolor(0.53, 0.8, 0.98)


def snowflake(size, n):

    def _koch(size, n):
        if n == 0:
            t.fd(size)
        else:
            for angle in [0, 60, -120, 60]:
                t.left(angle)
                _koch(size / 3, n - 1)

    for _ in range(3):
        _koch(size, n)
        t.right(120)


screensize = t.screensize()
snow_amount = int((screensize[0] + screensize[1]) // 50 * (rd.random() + 0.5))
for _ in range(snow_amount):
    t.penup()
    t.goto(
        rd.randint(-screensize[0] // 2, screensize[0] // 2),
        rd.randint(-screensize[1] // 2, screensize[1] // 2),
    )
    t.pendown()
    t.pencolor(*(rd.random() / 10 + 0.9,) * 3)
    snowflake(rd.randint(min(screensize), max(screensize)) / 30, rd.randint(1, 3))

t.done()
