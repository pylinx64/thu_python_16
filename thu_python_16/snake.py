# библиотеки
import turtle
import time
from random import randint

#--------------------------экран---------------------------------
screen = turtle.Screen()
# меняем цвет экрана
screen.bgcolor('#06FFD1')
# размер экрана
screen.setup(650, 650)
# название игры 
screen.title('Змейка в соусе версия 123')
#--------------------------экран---------------------------------

#--------------------------змейка--------------------------------
snake = []
snake_segment = turtle.Turtle()
# меняет форму 
snake_segment.shape('square')
snake_segment.penup()
snake.append(snake_segment)
#--------------------------змейка--------------------------------

#--------------------------еда-----------------------------------
food = turtle.Turtle()
food.shape('turtle')
food.penup()
# цвет еды
food.color('#000000')
food.goto(randint(-300, 300), randint(-300, 300))
#--------------------------еда-----------------------------------

#--------------------------управление----------------------------
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.listen()
#--------------------------управление----------------------------

#--------------------------игра----------------------------------
while True:
    # скорость гловы змейки
    snake[0].forward(1)
    
    # обновляет экран
    screen.update()
    
    # упраляет FPS
    time.sleep(0)
