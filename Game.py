
from turtle import Turtle
import random






###### Create Game Class
class gameEngine:

    def __init__(self):
        self.random = 0
        self.foodLocation = 0
        self.food = Turtle()

#### Foood
    def randomPosition(self):
        randomX = random.randrange(-280, 280, 20)
        randomY = random.randrange(-280, 280, 20)
        randomPosition = (randomX, randomY)
        self.random = randomPosition
        return self.random
    def createFood(self,var):
        ### Variables
        self.food.shape('circle')
        self.food.color('blue')
        self.food.penup()
        self.food.goto(var)


    def showFood(self):
        self.food.st()

    def hideFood(self):
        self.food.ht()

    def foodPosition(self):
        Y = round(self.random[1],2)
        X = round(self.random[0],2)
        self.food.goto(X,Y)
        self.foodLocation = self.food.pos()
        return self.foodLocation





## Interaction Logic


gameBoundry = 600





### Add Loop Background Music ###