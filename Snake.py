from turtle import Turtle
import time
#(-20, 0), (-40, 0
SNAKESTARTINGPOSITION = [(0, 0),(-20,0),(-40,0)]
MOVEDISTANCE = 20

class Snake:

    def __init__(self):
        self.snakeLength = []
        self.createSnake()
        self.lastPressedKey = 0
        self.position = 0
        self.snakeHead = 0



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

        snakeBody = self.snakeLength
        counter = 0
        currentPosition = 0
        futurePosition = 0

        for bodyPart in snakeBody:
            if counter == 0:
                print("I am the head")
                print("I am at: %s" % (str(bodyPart.pos())))
                futurePosition = bodyPart.pos()
                print("The next piece should be moving towards: %s " % (str(futurePosition)))
                bodyPart.forward(MOVEDISTANCE)
                self.snakeHead = bodyPart.pos()
                print("I am moving towards: %s" % (str(self.snakeHead)))
            else:
                print("I am Piece: %i" % (counter))
                currentPosition = bodyPart.pos()
                print("My Current Position is: %s" % str((currentPosition)))
                bodyPart.goto(futurePosition)
                print("Moving Towards: %s" % str((futurePosition)))
                futurePosition = currentPosition
                print("The next piece should be moving towards: %s" % (str(futurePosition)))


            counter += 1


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
