# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Screen
from Snake import Snake
import time
import Game

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
gameEngine = Game.gameEngine()

gameEngine.createFood()

while game_is_on:
    Screen.update()
    time.sleep(0.8)


    if (Snake.position.__abs__() >= 300) or (Snake.position.__abs__() <= -300):
        print("Out of Bounds!")
        break


    if Snake.position == gameEngine.foodPosition:
        print("Scored a Point!")
        Snake.singleSnake()
        gameEngine.createFood()
    print("Moving!")
    print(Snake.position)
    Snake.snakeMove()









Screen.exitonclick()
