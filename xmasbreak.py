import pygame
from pygame import Vector2
from ball import Ball
from paddle import Paddle
from brick import Chocolate, Gingerbread, Lollipop
from intersect import intersect_rectangle_circle
import time
speedFactor = 20
pygame.init()
winSound = pygame.mixer.Sound('jingle.wav')
looseSound = pygame.mixer.Sound('gasping.wav')

def startNewGame(ball, paddle, bricksList, mainScreen):
    ball.reset()
    paddle.reset()
    brickX = 0 #the position of the x of each brick
    brickY = 25 #the position of the y of each brick
    
    for i in range(4):
        for j in range(7):#making the list containing twentyone brick objects
            if j == 0:
                bricksList.append(Lollipop(mainScreen, brickX, brickY))
            if j == 1:
                bricksList.append(Chocolate(mainScreen, brickX, brickY))
            if j == 2:
                bricksList.append(Gingerbread(mainScreen, brickX, brickY))
            if j == 3:
                bricksList.append(Lollipop(mainScreen, brickX, brickY))
            if j == 4:
                bricksList.append(Chocolate(mainScreen, brickX, brickY))
            if j == 5:
                bricksList.append(Gingerbread(mainScreen, brickX, brickY))
            if j == 6:
                bricksList.append(Lollipop(mainScreen, brickX, brickY))
            brickX += 75 #print each brick on a row next to eachother from left to right
        brickY += 24#print each brick in a column under each other
        brickX = 0#start each row at the left side of the screen
   

def xmasBreak():
    print ("Lets play XmasBreak! Press SPACE to start the game.")
    pygame.display.set_caption("XmasBreak")
    #Size of window
    screenWidth = 525
    screenHeight = 700
    #Gets image file from computer
    BGFileName = "xmastree.png"
    #Initilizes PyGame. Makes all Pygame modules available.
    pygame.init() 
    #Calls pygames display function to set the surface
    mainScreen = pygame.display.set_mode((screenWidth, screenHeight))

    #Sets the backgroud image and scales it to the size of the window
    backGround = pygame.transform.scale(pygame.image.load(BGFileName), (screenWidth, screenHeight))

    #make ball object
    ball = Ball(mainScreen, speedFactor)#Creates a ball object
    paddle = Paddle(mainScreen)#Creates a paddle object
    bricksList = [] #initializing the list containing all the bricks

    startNewGame(ball, paddle, bricksList, mainScreen)

    ballInPlay = False#Sets a variable to control if the ball should move or not
    waitForRestart = False
   
    #loops in order to make the ball and paddle move
    while True:
        #pauses the program,in order to keep the window open
        pygame.time.delay(60)
        #Exits the game window and sends a message to the user when the game is quit
        #or the window is shut
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thank you for playing!")
                exit()
        #Draws the background I defined in backGround on top of the surface
        #on position x = 0 and y = 0
        mainScreen.blit(backGround, (0,0))
        #draw the ball
        #calls the "draw" procedure in the class Ball, Paddle and Bricks to draw them on the screen
        ball.draw()
        paddle.draw()
        
        #writing the list of bricks to the screen
        for brick in bricksList:
            impulse = intersect_rectangle_circle(brick.pos, brick.width, 
                                    brick.height, Vector2(ball.pos.x + ball.radius, ball.pos.y + ball.radius),
                                    ball.radius, ball.speed)
            if impulse:
                ball.speed = impulse * speedFactor
                bricksList.remove(brick)
            else:
                brick.draw()
        if pygame.key.get_pressed()[pygame.K_UP]:
            for brick in bricksList:
                bricksList.remove(brick)

        if (ballInPlay == True):
            if not bricksList:
                ballInPlay = False
                winSound.play()
                time.sleep(5)
                winSound.stop()
                print("YOU WIN!!/n Press ENTER to play again or close the window to quit.")
                waitForRestart = True
            if waitForRestart == True:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    waitForRestart = False
                    startNewGame(ball, paddle, bricksList, mainScreen)

        

        #moves the paddle
        paddle.move()
        
        
        
        #if the ball exits the bottom of the screen
        if (ballInPlay == True):
            if (ball.move() == False): 
                ballInPlay = False
                looseSound.play()
                time.sleep(2)
                looseSound.stop()
                print("You lose. Press ENTER to play again! ..or close the window to quit.")
                waitForRestart = True
        if waitForRestart == True:
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                waitForRestart = False
                startNewGame(ball, paddle, bricksList, mainScreen)

        #If space is pressed the ball starts to move
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            ballInPlay = True


        #check if the ball hits anything    
        impulse = intersect_rectangle_circle(paddle.pos, paddle.width, 
                                    paddle.height, Vector2(ball.pos.x + ball.radius, ball.pos.y + ball.radius),
                                    ball.radius, ball.speed)
        if impulse:
            if (ball.pos.x < (paddle.pos.x + paddle.width/2)- 25):
                diff = (ball.pos.x + ball.radius) - (paddle.pos.x + paddle.width/2)   
                impulse.x = diff/100
                impulse.normalize() * speedFactor
           
            if (ball.pos.x > (paddle.pos.x + paddle.width/2) +25):
                diff = (ball.pos.x + ball.radius) - (paddle.pos.x + paddle.width/2)   
                impulse.x = diff/100
                impulse.normalize() * speedFactor
               
            
            ball.speed = impulse * speedFactor
        #updates the display 
        pygame.display.update()


if __name__ == '__main__':
    xmasBreak()