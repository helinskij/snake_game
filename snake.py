from turtle import Turtle
import random

SHAPES = ['circle', 'square', 'triangle']
COLORS = ['green', 'blue', 'red', 'yellow', 'purple']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(SHAPES))
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        self.shape(random.choice(SHAPES))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
