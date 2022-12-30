import pygame
from pygame import Vector2


class Ball():
    #initializes the object and makes the attributes of the class available
    #when the class is called
    def __init__(self, screen, speedF):
        #defines mainScreen in this class
        self.screen = screen
        #Adds the ball image from png file and makes sure that "empty" pixels aren't drawn
        self.ballImg = pygame.image.load("ball.png")
        self.ballImg = self.ballImg.convert_alpha()
        #positions the ball in the window at reset postition (see method "reset" below)
        self.pos = self.reset()
        #sets the initial speed of the ball
        self.speed = Vector2 (0,-1) * speedF
        self.width = self.ballImg.get_width()
        self.height = self.ballImg.get_height()
        self.radius = self.ballImg.get_width()/2
                                                                                            
    #method to draw the ball
    def draw (self):
        self.screen.blit(self.ballImg, (self.pos))
    #method to move the ball
    def move (self):
        if self.pos.x < 0+5: #stops the ball from exciting to the left, 5 for good measure
            self.speed.x = abs(self.speed.x)
        if self.pos.y < 0+5: #stops the ball from exciting at the top, 5 for good measure
            self.speed.y = abs(self.speed.y)
        if self.pos.x > self.screen.get_width()-self.ballImg.get_width():
                                 #stops the ball from exciting to the right 
                                #of the screen, and keeps the
                                #entire ball inside the window
            self.speed.x = -abs(self.speed.x) 
        if self.pos.y > self.screen.get_height() + self.ballImg.get_width(): 
            return False
        
        self.pos += self.speed

    def reset (self):
        #positions the ball in the window
        self.pos = Vector2 (237, 650)

    