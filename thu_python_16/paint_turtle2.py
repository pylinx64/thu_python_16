import turtle

t=turtle.Pen()
#-------------
t.shape('turtle')

t.color('#FFA100', '#FF0085')# цвет карандаша, цвет заливки
t.begin_fill()

t.pencolor('#00FFBE')
t.forward(100)
t.left(120)

t.pencolor('#FFD800')
t.forward(100)
t.left(120)

t.pencolor('#FFD800')
t.forward(100)
t.left(120)

t.end_fill()

t.penup()
t.left(65)
t.forward(200)
t.pendown()
t.circle(30)

t.write('Hello world', align='left', font=('Thintel', 40))

#------------
turtle.done()
