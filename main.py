# This is a sample Python script.

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

food = gameEngine()
food.createFood(food.randomPosition())
food.hideFood()
foodPosition = food.foodPosition()

while game_is_on:
    Screen.update()
    time.sleep(0.8)
    print("Food is at: %s" % (str(food.foodLocation)))



    if foodisVisible == False:
        food.showFood()
        foodisVisible = True

    elif (Snake.snakeLength[0].pos().__abs__() == (300,300)) or (Snake.snakeLength[0].pos() == (-300,-300)):
        print("Out of Bounds!")
        break


    #elif str(Snake.snakeLength[0].pos()) == str(foodPosition):
    #    print("Scored a Point!")
    ##    Snake.singleSnake()
     #   food.hideFood()
     #   foodisVisible = False


    print("Moving!")
    print(Snake.snakeLength[0].pos())
    Snake.snakeMove()









Screen.exitonclick()
