from turtle import Turtle
import time

SNAKESTARTINGPOSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20

class Snake:

    def __init__(self):
        self.snakeLength = []
        self.createSnake()



    def createSnake(self):

        for positions in SNAKESTARTINGPOSITION:
            Snakes = Turtle()
            Snakes.shape('square')
            Snakes.color('white')
            Snakes.penup()
            Snakes.goto(positions)
            self.snakeLength.append(Snakes)


    def snakeMove(self):
            Snakehead = self.snakeLength[0]
            for Snake in self.snakeLength[1:]:
                Snake.setx(Snakehead.xcor())
                Snake.sety(Snakehead.ycor())
                Snakehead.forward(MOVEDISTANCE)

    def Up(self):
        Snakehead = self.snakeLength[0]
        for Snake in self.snakeLength[1:]:
            Snake.setx(Snakehead.xcor())
            Snake.sety(Snakehead.ycor())
            Snake.setheading(90)

    def Down(self):
        Snakehead = self.snakeLength[0]
        for Snake in self.snakeLength[1:]:
            Snake.setx(Snakehead.xcor())
            Snake.sety(Snakehead.ycor())
            Snake.setheading(270)

    def Left(self):
        Snakehead = self.snakeLength[0]
        for Snake in self.snakeLength[1:]:
            Snake.setx(Snakehead.xcor())
            Snake.sety(Snakehead.ycor())
            Snake.setheading(0)

    def Right(self):
        Snakehead = self.snakeLength[0]
        for Snake in self.snakeLength[1:]:
            Snake.setx(Snakehead.xcor())
            Snake.sety(Snakehead.ycor())
            Snake.setheading(180)
