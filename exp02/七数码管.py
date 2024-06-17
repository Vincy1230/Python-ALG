import turtle as t
from digital_tube import digital_tube

# 浙 B94250
t.delay(0)
t.speed(0)
t.bgcolor(0, 0.05, 0.025)
t.hideturtle()
t.penup()
t.goto(-300, -100)
t.pencolor(0.5, 0.15, 0.1)
t.fillcolor(1.0, 0.2, 0.1)
digital_tube("b94250", font=(200, "normal"), frame=True)
t.goto(-580, -135)
t.color(1.0, 0.2, 0.1)
t.write("浙", font=("Arial", 175, "bold"))
t.done()
