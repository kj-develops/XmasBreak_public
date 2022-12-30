import pygame


pygame.display.set_caption("XmasBreak")
#Size of window
screenWidth = 500
screenHeight = 700
#Gets image file from computer
BGFileName = "xmastree.jpg"
#Initilizes PyGame. Makes all Pygame modules available.
pygame.init() 
#Calls pygames display function to set the surface
mainScreen = pygame.display.set_mode((screenWidth, screenHeight))

#Sets the backgroud image and scales it to the size of the window
backGround = pygame.transform.scale(pygame.image.load(BGFileName), (screenWidth, screenHeight))

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
        pygame.display.update()