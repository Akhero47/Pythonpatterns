import turtle
import math
import random
turtle.screensize(canvwidth=2160, canvheight=1440, bg=None)
turtle.colormode(255)
turtle.speed(300)
turtle.up()
turtle.goto(400,0)
turtle.down()
turtle.tracer(0,0)
for k in range(1,50):
	turtle.update()
	for j in range(1,20,5):
		turtle.forward(5)
		turtle.left(j*5)
		for i in range (1,20):
			R=random.randrange(1,255,1)
			G=random.randrange(1,255,1)
			B=random.randrange(1,255,1)
			turtle.fillcolor(B,G,R)
			turtle.pencolor(R,0,B)
			turtle.pensize(abs(5*math.sin(i)))
			turtle.forward(100)
			turtle.right(i*10)
turtle.update()
#turtle.getscreen().getcanvas().postscript(file="sp.eps")
turtle.done()
