import pygame
from pygame import Vector2

class Brick:
    #initializes the object and makes the attributes of the class available
    #when the class is called
    def __init__(self, screen, x, y):
        #defines mainScreen in this class
        self.screen = screen
        #Adds the brick image from subclass png file and makes shure that "empty" pixels aren't drawn
        self.brickImg = pygame.image.load("brick.png").convert_alpha()
        self.pos = Vector2 (x, y)
        self.width = self.brickImg.get_width()
        self.height = self.brickImg.get_height()

    #method to draw the bricks
    def draw (self):
        self.screen.blit(self.brickImg, (self.pos.x,self.pos.y))
    
class Chocolate(Brick):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.brickImg = pygame.image.load("chocbrick.png").convert_alpha()
    
class Gingerbread(Brick):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.brickImg = pygame.image.load("gingerbrick.png").convert_alpha()

class Lollipop(Brick):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.brickImg = pygame.image.load("lollibrick.png").convert_alpha()