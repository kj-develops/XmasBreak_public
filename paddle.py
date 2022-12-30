import pygame
from pygame import Vector2

class Paddle:
    #initializes the object and makes the attributes of the class available
    #when the class is called
    def __init__(self, screenIn):
        #defines mainScreen in this class
        self.screen = screenIn
        #Adds the paddle image from png file and makes shure that "empty" pixels aren't drawn
        self.paddleImg = pygame.image.load("paddle.png")#pygame.image.load returnerer en surface
        self.paddleImg = self.paddleImg.convert_alpha()
        #positions the paddle in the window
        self.pos = self.reset()
        #sets the initial speed of the paddle
        self.speed = Vector2 (15, 15)
        self.width = self.paddleImg.get_width()
        self.height = self.paddleImg.get_height()

    #method to draw the padlle
    def draw (self):
        self.screen.blit(self.paddleImg, (self.pos.x, 680))

    #method to move the paddle
    def move (self):
        """x, y = pygame.mouse.get_pos()
        paddle_position = Vector2 (x,680)"""
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.pos.x = self.pos.x - self.speed.x
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.pos.x = self.pos.x + self.speed.x
        if self.pos.x <= 0: #stops the paddle from exciting to the left
            self.pos.x = 0
        if self.pos.x + self.width >= self.screen.get_width() : #stops the paddle from exciting to the right
            self.pos.x = (self.screen.get_width()) - self.width

    def reset(self):
        #positions the paddle in the window
        self.pos = Vector2 (188,680)
       