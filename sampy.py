import turtle
import random
turtle.speed(0)
turtle.colormode(255)
f = 45
turtle.tracer(0)
l = 0
turtle.right(90)
turtle.forward(50)
while l < 30:
	turtle.update()
	for i in range(1,12):
		R=random.randrange(1,255,1)
		s=random.randrange(1,8,1)
		G=random.randrange(1,255,1)
		B=random.randrange(1,255,1)
		
		turtle.begin_fill()
		turtle.fillcolor(R,G,B)
		turtle.screensize(canvwidth=2160, canvheight=1440, bg=None)
		turtle.left(180)
		turtle.forward(f)
		turtle.right(60)
		turtle.forward(f)
		turtle.right(60)
		turtle.forward(f)
		turtle.right(90)
		turtle.forward(2*f)
		turtle.end_fill()
	turtle.forward(90)
	l = l + 1

turtle.getscreen().getcanvas().postscript(file="finnesse.eps")
	


