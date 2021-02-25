import turtle
import time

t=turtle.Pen()
#-----------------------
turtle.bgcolor('black')

t.shape('triangle')
 
i = 256
while True:
	t.pencolor('red')
	t.forward(100)
	t.left(i)

#-----------------------
time.sleep(1000)
