#   WHY DRAW BY HAND  WHEN YOU CAN DEFINE AND DRAW IT #
"""
    
    Patterns Using Turtle in Python
            By Abhinab Khanal

    
"""



import turtle
import random
turtle.screensize(2160,1440)
turtle.colormode(255)
turtle.speed(10)
turtle.tracer(0,0)
random.seed(0)
k = 1
tp = turtle.pos()
print(tp)
for i in range(10):
    turtle.setpos(tp)
    for i in range (k):
        turtle.update()
        k = k + 1
        for i in range(k):
            R=random.randint(1,120)
            g=random.randint(1,120)
            b=random.randint(1,120)
            turtle.update()
            for i in range(k):
                turtle.update()
                turtle.pencolor(R,g,b)
                turtle.forward(50)
                turtle.left(45)
                turtle.right(20)
                turtle.forward(20)
                turtle.update()
            turtle.left(160)
            turtle.update()
            turtle.forward(30)
        
