import turtle
import math
import random
turtle.colormode(255)
turtle.speed(10000)
turtle.tracer(0,0)
turtle.pensize(1)
i=0
c=1
while True:
	turtle.update()
	for i in range(30,60,1):
		R=random.randrange(1,255,1)
		G=random.randrange(1,255,1)
		B=random.randrange(1,255,1)
		turtle.pencolor(R,G,B)
		turtle.forward(10+i)
		turtle.right(360-i)
		
