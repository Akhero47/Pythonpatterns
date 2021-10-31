import turtle
import random
turtle.screensize(2160,1440)
turtle.colormode(255)
turtle.speed(1)
turtle.tracer(0,0)
for i in range (17):
    for i in range(10):
        R=random.randint(1,120)
        g=random.randint(1,120)
        b=random.randint(1,120)
        turtle.update()
        for i in range(75):
            turtle.pencolor(R,g,b)
            turtle.forward(50)
            turtle.left(45)
            turtle.right(20)
            turtle.forward(20)
            turtle.update()
        turtle.left(160)
        turtle.update()
        turtle.forward(30)    
