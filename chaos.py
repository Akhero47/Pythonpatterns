import turtle
import math
import random
turtle.tracer(0,0)
turtle.screensize(canvwidth=2160, canvheight=1440, bg=None)
turtle.colormode(255)
turtle.speed()
i = 1
j=0
while True:
	turtle.update()
	j=(((i*2)+2)/2)
	turtle.forward(j)
	turtle.left(j+i)
	i = j
	
