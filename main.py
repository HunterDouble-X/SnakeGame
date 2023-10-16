# This is a sample Python script.
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Screen
from Snake import Snake
import time
from Game import gameEngine

### Screen Setup ###
Screen = Screen()
Screen.title("Snake")
Screen.setup(width=600, height=600)
Screen.bgcolor('black')
Screen.tracer(0)


Snake = Snake()
Screen.listen()

Screen.onkey(Snake.Up, "Up")
Screen.onkey(Snake.Down, "Down")
Screen.onkey(Snake.Left, "Left")
Screen.onkey(Snake.Right, "Right")

game_is_on = True



foodisVisible = False

#food = gameEngine()
#food.createFood(food.randomPosition())
#food.hideFood()
#foodPosition = food.foodPosition()

while game_is_on:
    Screen.update()
    time.sleep(1)





    if foodisVisible == False:
        food = gameEngine()
        food.createFood(food.randomPosition())
        food.showFood()
        foodisVisible = True

    #elif 300 or -300 in Snake.snakeHead:
    #    print("Out of Bounds!")
    #    break

    elif str(Snake.snakeHead) == str(food.foodPosition()):
        print("Scored a Point!")
        print("The Snake Head is at: %s " % (str(Snake.snakeHead)))
        print("The Food is at: %s" % (str(food.foodPosition())))
        time.sleep(3)
        Snake.singleSnake()
        food.hideFood()
        foodisVisible = False

    else:
        counter = 1
        for segment in Snake.snakeLength[1:]:
            #print(segment.pos())
            if str(Snake.snakeHead) == str(segment.pos()):
                print("The Snake Head Collided with Segement: %i" % (counter))
                print("DED")
                time.sleep(3)
                sys.exit()
            counter +=1




    print(Snake.snakeHead.__abs__())
    print("Food is at: %s" % (str(food.foodPosition())))
    Snake.snakeMove()









Screen.exitonclick()
