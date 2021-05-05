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

#-------------------------рекорд----------------------------------
score = 0
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.goto(-300, 300)
#-------------------------рекорд----------------------------------

FLAG = False
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
        # обновляем рекорд если голова коснулась яблока
        score = score + 1
    
    score_pen.clear()
    score_pen.write(score,  align= 'center', font=('Arial', 15)) 
    
    # команды для перемещения тела
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()   # достает координату х прошлого туловища
        y = snake[i-1].ycor()
        snake[i].goto(x, y)
        
    # скорость гловы змейки
    snake[0].forward(15)
    
    # обновляет экран
    screen.update()
    
    # узнали координаты головы
    x_head = snake[0].xcor()
    y_head = snake[0].ycor()
    
    x_head = int(x_head)
    y_head = int(y_head)
    print(x_head, y_head)
    
    # проверка вышла ли голова за правый крайний угол
    if x_head > 300:
        # текст (текст, шрифт, размер)
        turtle.write('GAME OVER', font=('Arial', 20))
        break
    
    if x_head < -300:
        # команда которая меняет цвет фона
        turtle.write('GAME OVER', font=('Arial', 20))
        break
    
    if y_head > 300:
        turtle.write('GAME OVER', font=('Arial', 20))
        break 
    
    if y_head < -300:
        turtle.write('GAME OVER', font=('Arial', 20))
        break
        
    # мы будем программировать здесь=================================
    # проверка кушает ли себя змея
    # перебираем все туловища
    for i in snake[1:]:
        # достаем коорлинаты туловища
        coords = i.position()
        # если голова коснулась туловища
        if snake[0].distance(coords) < 10:
            FLAG = True
    
    # проверка флажка
    if FLAG == True:
        turtle.write('GAME OVER', font=('Arial', 20))
        break
    
    # упраляет FPS
    time.sleep(0.05)

time.sleep(3)
