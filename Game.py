
from turtle import Turtle
import random






###### Create Game Class
class gameEngine:

    def __init__(self):
        self.food = []
        self.random = random
        self.foodPosition = ()

#### Foood

    def createFood(self):
        ### Variables
        randomX = random.randrange(-280, 280, 20)
        randomY = random.randrange(-280, 280, 20)
        foodPosition = (randomX, randomY)
        self.foodPosition = foodPosition
        food = Turtle()
        food.shape('circle')
        food.color('blue')
        food.penup()
        food.goto(foodPosition)






## Interaction Logic


gameBoundry = 600





### Add Loop Background Music ###