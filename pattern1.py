import turtle
import math
import random
turtle.colormode(255)
turtle.speed(100)
turtle.pensize(1)
i=0
c=1
while True:
	for i in range(1,30):
		R=random.randrange(1,255,1)
		G=random.randrange(1,255,1)
		B=random.randrange(1,255,1)
		turtle.pencolor(R,G,B)
		turtle.forward(5+i)
		turtle.right(360-i)