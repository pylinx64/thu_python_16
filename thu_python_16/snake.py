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
# убирает задержки
screen.tracer(0)
#--------------------------экран---------------------------------

#--------------------------змейка--------------------------------
snake = []
# голова
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
    # проверка сьела ли змея еду
    if snake[0].distance(food) < 20:
        food.goto(randint(-300, 300), randint(-300, 300))
        # добавлем тело если змейка сьела еду
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('#78004D')
        snake_segment.penup()
        snake.append(snake_segment)
        
    # команды для перемещения тела
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()   # достает координату х прошлого туловища
        y = snake[i-1].ycor()
        snake[i].goto(x, y)
        
    # скорость гловы змейки
    snake[0].forward(15)
    
    # обновляет экран
    screen.update()
    
    # упраляет FPS
    time.sleep(0.05)
