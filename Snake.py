from turtle import Turtle
import time
#(-20, 0), (-40, 0
SNAKESTARTINGPOSITION = [(0, 0)]
MOVEDISTANCE = 20

class Snake:

    def __init__(self):
        self.snakeLength = []
        self.createSnake()
        self.lastPressedKey = 0
        self.position = 0



    def createSnake(self):

        for positions in SNAKESTARTINGPOSITION:
            Snakes = Turtle()
            Snakes.shape('circle')
            Snakes.color('green')
            Snakes.penup()
            Snakes.goto(positions)
            self.snakeLength.append(Snakes)


    def singleSnake(self):

        positions = self.snakeLength[-1].pos()
        Snakes = Turtle()
        Snakes.shape('circle')
        Snakes.color('red')
        Snakes.penup()
        Snakes.goto(positions)
        self.snakeLength.append(Snakes)



    def snakeMove(self):
            Snakehead = self.snakeLength[0]
            snakeBody = self.snakeLength[1:]
            self.position = Snakehead.pos()

            positionHolder = 0
            counter = 1
            for body in snakeBody:

                ## Get current Position
                currentPosition = body.pos()
                futurePosition = self.snakeLength[counter - 1].pos()

                if positionHolder == 0:
                    positionHolder = currentPosition
                    body.setpos(futurePosition)

                else:
                    body.setpos(positionHolder)
                    positionHolder = currentPosition
                counter += 1



            Snakehead.forward(MOVEDISTANCE)

    def Up(self):
        Snakehead = self.snakeLength[0]
        Snakehead.setheading(90)
        self.position = Snakehead.pos()

    def Down(self):
        Snakehead = self.snakeLength[0]
        Snakehead.setheading(270)
        self.position = Snakehead.pos()

    def Left(self):
        Snakehead = self.snakeLength[0]
        Snakehead.setheading(180)
        self.position = Snakehead.pos()

    def Right(self):
        Snakehead = self.snakeLength[0]
        Snakehead.setheading(0)
        self.position = Snakehead.pos()
