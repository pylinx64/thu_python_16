import turtle

t=turtle.Pen()
#--------------------
t.shape('turtle')


colors = ['black', 'yellow', 'lime', 'blue', 'magenta']

t.speed('fastest')

for x in range(1000):
	t.pencolor(colors[x%5])
	t.left(68)
	t.forward(x)

#--------------------
turtle.done()
