# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Screen, Turtle
import time

### Screen Setup ###
Screen = Screen()
Screen.title("Snake")
Screen.setup(width=600, height=600)
Screen.bgcolor('black')
Screen.tracer(0)

SnakeStartingPosition = [(0,0),(-20,0),(-40,0)]
SnakeLength = []



for positions in SnakeStartingPosition:
    Snakes = Turtle()
    Snakes.shape('square')
    Snakes.color('white')
    Snakes.penup()
    Snakes.goto(positions)
    SnakeLength.append(Snakes)



game_is_on = True

while game_is_on:
    Screen.update()
    time.sleep(0.8)
    Snakehead = SnakeLength[0]
    for Snake in SnakeLength[1:]:
        Snake.setx(Snakehead.xcor())
        Snake.sety(Snakehead.ycor())
        Snakehead.forward(30)
        Snakehead.left(90)









Screen.exitonclick()
