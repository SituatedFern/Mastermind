# Mastermind
# Ashwin Gnanam
# June 21st, 2021
# This program creates a mastermind puzzle and menu system

"""
Important Things I added:
 * subprograms (to skip to different sections of code)
 * sounds & music
 * mouse input
 * lists (many of them)
 * adding images (and making them clickable)
 * timer
 * highscore
 * save files
 * cheats menu
 * global variables
 * choosing a selected number of objects in a large list (random.sample)
 * drawing triangles (using polygon function)
"""

"""
Sources:
 * menu system is from my pong assignment
 * difficulty settings are from my snake assignment
"""

# import the necessary modules
import pygame
import random
import time
import sys

from pygame import display

#initialize pygame
pygame.init()
 
# setting the size of the window
screenWidth = 800
screenHeight = 625
screen = pygame.display.set_mode((screenWidth,screenHeight),0)
pygame.display.set_caption("Mastermind") #setting the name of the pygame window

difficulty = "Hello!"

#setting the game clock with 75 frames per second
clock = pygame.time.Clock()
FPS = 75

#defining colours that will be used
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
MUD = (194,128,0)
BROWN = (95,71,24)
NEWBLUE = (0,255,247)
PURPLISH = (4,9,31)

soundtrack = pygame.mixer.Sound('Thinking Music.wav')
soundtrack.play()

def inst(): #instructions menu
    #creating font presets to use later
    smallfont = pygame.font.SysFont("arial",20)
    fontTitle = pygame.font.SysFont("arial",35)

    main = True
    while main == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                sys.exit()

        clock.tick(FPS) # constrain this loop to the specified FPS                      

        # render the text into an image of the text, colour is white
        Title1 = smallfont.render("Put the balls in the first row of slots in the correct sequence.", True, WHITE)
        # create a rect from the text
        Rect1 = Title1.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen

        Rect1.center = (screenWidth / 2), (screenHeight / 2)

        Rect1.x = 40
        Rect1.y = int(screenHeight//2)-200

        screen.fill(BLACK)
        screen.blit(Title1, Rect1)

        # render the text into an image of the text, colour is white
        Title2 = smallfont.render("Your previous guesses are stored below in the lower rows.", True, WHITE)
        # create a rect from the text
        Rect2 = Title2.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen

        Rect2.center = (screenWidth / 2), (screenHeight / 2)

        Rect2.x = 40
        Rect2.y = int(screenHeight//2)-100

        screen.blit(Title2, Rect2)

        # render the text into an image of the text, colour is white
        Title3 = smallfont.render("Press escape at anytime to return to the menu.", True, WHITE)
        # create a rect from the text
        Rect3 = Title3.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen

        Rect3.center = (screenWidth / 2), (screenHeight / 2)

        Rect3.x = 40
        Rect3.y = int(screenHeight//2)+15

        screen.blit(Title3, Rect3)

        # render the text into an image of the text, colour is red
        backTitle = fontTitle.render("Main Menu", True, YELLOW)
        # create a rect from the text
        backRect = backTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen

        backRect.center = (screenWidth / 2), (screenHeight / 2)

        backRect.x = 40
        backRect.y = int(screenHeight//2)+150

        screen.blit(backTitle, backRect)

        # render the text into an image of the text, colour is red
        qTitle = fontTitle.render("Quit", True, RED)
        # create a rect from the text
        qRect = qTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen

        qRect.center = (screenWidth / 2), (screenHeight / 2)

        qRect.x = 650
        qRect.y = int(screenHeight//2)+150

        screen.blit(qTitle, qRect)

        pygame.display.flip()

        if(backRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            menu()
        elif(qRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()

def cheatsmenu():
    global OSTon, TRon
    smallfont = pygame.font.SysFont("arial",35)

    main = True
    while main == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                sys.exit()

        clock.tick(FPS) # constrain this loop to the specified FPS

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        screen.fill(PURPLISH)
        cheatImage = pygame.image.load('cheatsimg.jpg') #this image was created using: https://web.over.app/
        screen.blit(cheatImage, (220, 10))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # render the text into an image of the text, colour is red
        trTitle = smallfont.render("Terminal Readout", True, WHITE)
        # create a rect from the text
        trRect = trTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        trRect.center = (screenWidth / 2), (screenHeight / 2)

        trRect.x = int(screenWidth//2)-350
        trRect.y = int(screenHeight//2)-65

        screen.blit(trTitle, trRect)

        TRonTitle = smallfont.render("ON", True, GREEN)
        # create a rect from the text
        TRonRect = TRonTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        TRonRect.center = (screenWidth / 2), (screenHeight / 2)

        TRonRect.x = int(screenWidth//2)+175
        TRonRect.y = int(screenHeight//2)-65

        screen.blit(TRonTitle, TRonRect)

        TRoffTitle = smallfont.render("OFF", True, RED)
        # create a rect from the text
        TRoffRect = TRoffTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        TRoffRect.center = (screenWidth / 2), (screenHeight / 2)

        TRoffRect.x = int(screenWidth//2)+275
        TRoffRect.y = int(screenHeight//2)-65

        screen.blit(TRoffTitle, TRoffRect)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # render the text into an image of the text, colour is red
        ostTitle = smallfont.render("On Screen Target", True, WHITE)
        # create a rect from the text
        ostRect = ostTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        ostRect.center = (screenWidth / 2), (screenHeight / 2)

        ostRect.x = int(screenWidth//2)-350
        ostRect.y = int(screenHeight//2)

        screen.blit(ostTitle, ostRect)

        OSTonTitle = smallfont.render("ON", True, GREEN)
        # create a rect from the text
        OSTonRect = OSTonTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        OSTonRect.center = (screenWidth / 2), (screenHeight / 2)

        OSTonRect.x = int(screenWidth//2)+175
        OSTonRect.y = int(screenHeight//2)

        screen.blit(OSTonTitle, OSTonRect)

        OSToffTitle = smallfont.render("OFF", True, RED)
        # create a rect from the text
        OSToffRect = OSToffTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        OSToffRect.center = (screenWidth / 2), (screenHeight / 2)

        OSToffRect.x = int(screenWidth//2)+275
        OSToffRect.y = int(screenHeight//2)

        screen.blit(OSToffTitle, OSToffRect)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #render the text into an image of the text, colour is red
        backTitle = smallfont.render("Main Menu", True, YELLOW)
        #create a rect from the text
        backRect = backTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        #place this rect at the centre of the screen

        backRect.center = (screenWidth / 2), (screenHeight / 2)

        backRect.x = 40
        backRect.y = screenHeight-100

        screen.blit(backTitle, backRect)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #render the text into an image of the text, colour is red
        qTitle = smallfont.render("Quit", True, RED)
        #create a rect from the text
        qRect = qTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        #place this rect at the centre of the screen

        qRect.center = (screenWidth / 2), (screenHeight / 2)

        qRect.x = screenWidth-115
        qRect.y = screenHeight-100

        screen.blit(qTitle, qRect)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #render the text into an image of the text, colour is red
        choffTitle = smallfont.render("Cheats Off", True, GREEN)
        #create a rect from the text
        choffRect = choffTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        #place this rect at the centre of the screen

        choffRect.center = (screenWidth / 2), (screenHeight / 2)

        choffRect.x = int(screenWidth//2)-80-95
        choffRect.y = screenHeight-180

        screen.blit(choffTitle, choffRect)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #render the text into an image of the text, colour is red
        pTitle = smallfont.render("Play", True, NEWBLUE)
        #create a rect from the text
        pRect = pTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        #place this rect at the centre of the screen

        pRect.center = (screenWidth / 2), (screenHeight / 2)

        pRect.x = int(screenWidth//2)+150-60
        pRect.y = screenHeight-180

        screen.blit(pTitle, pRect)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        pygame.display.flip()

        if(OSTonRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            OSTon = True

        elif(OSToffRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            OSTon = False

        elif(TRonRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            TRon = True

        elif(TRoffRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            TRon = False

        elif(choffRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            TRon = False
            OSTon = False
            mastermind()

        elif(pRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            mastermind()

        elif(backRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            menu()

        elif(qRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()

def diffselect():
    global difficulty, readout

    fontTitle = pygame.font.SysFont("arial",35)

    main = True
    while main == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                sys.exit()

        clock.tick(FPS) # constrain this loop to the specified FPS                      

        # render the text into an image of the text, colour is red
        diffTitle = fontTitle.render("Choose Difficulty:", True, WHITE)
        # create a rect from the text
        diffRect = diffTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        diffRect.center = (screenWidth / 2), (screenHeight / 2)

        diffRect.x = int(screenWidth//2)-140
        diffRect.y = int(screenHeight//2)-200

        screen.fill(BLACK)
        screen.blit(diffTitle, diffRect)

        # render the text into an image of the text, colour is red
        easyTitle = fontTitle.render("Easy", True, GREEN)
        # create a rect from the text
        easyRect = easyTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        easyRect.center = (screenWidth / 2), (screenHeight / 2)

        easyRect.x = int(screenWidth//2)-300
        easyRect.y = int(screenHeight//2)-100

        screen.blit(easyTitle, easyRect)

        # render the text into an image of the text, colour is red
        medTitle = fontTitle.render("Hard", True, YELLOW)
        # create a rect from the text
        medRect = medTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        medRect.center = (screenWidth / 2), (screenHeight / 2)

        medRect.x = int(screenWidth//2)-300
        medRect.y = int(screenHeight//2)+20

        screen.blit(medTitle, medRect)

        # render the text into an image of the text, colour is red
        hardTitle = fontTitle.render("Impossible", True, RED)
        # create a rect from the text
        hardRect = hardTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        hardRect.center = (screenWidth / 2), (screenHeight / 2)

        hardRect.x = int(screenWidth//2)-300
        hardRect.y = int(screenHeight//2)+150

        screen.blit(hardTitle, hardRect)

        pygame.display.flip()

        cheatseffect = pygame.mixer.Sound("Hackerman.wav")

        if(easyRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            difficulty = str("Easy")
            cheatseffect.play()
            cheatsmenu()
            
        elif(medRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            difficulty = str("Hard")
            cheatseffect.play()
            cheatsmenu()

        elif(hardRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            difficulty = str("Impossible")
            cheatseffect.play()
            cheatsmenu()

def run2():

    def numtrick(file):
        global nextpage
        with open(file) as f:
            nextpage = []
            for line in f:
                line = line.split() # to deal with blank
                if line:            # lines (ie skip them)
                    line = [int(i) for i in line]
                    nextpage.append(line)
        print(nextpage)

    def run():
        global prevguess, slotcolour5, slotcolour6, slotcolour7, slotcolour8, row2y, row3y, row4y, row5y, count, elapsed
        r = 20 #setting the radius for the balls

        row2y = 175
        row3y = 250
        row4y = 325
        row5y = 400

        # setting colours for the four main slots  
        slotcolour1 = BROWN
        slotcolour2 = BROWN
        slotcolour3 = BROWN
        slotcolour4 = BROWN
        slotcolour5 = BROWN
        slotcolour6 = BROWN
        slotcolour7 = BROWN
        slotcolour8 = BROWN
        slotcolour9 = BROWN
        slotcolour10 = BROWN
        slotcolour11 = BROWN
        slotcolour12 = BROWN
        slotcolour13 = BROWN
        slotcolour14 = BROWN
        slotcolour15 = BROWN
        slotcolour16 = BROWN
        slotcolour17 = BROWN
        slotcolour18 = BROWN
        slotcolour19 = BROWN
        slotcolour20 = BROWN

        numtrick('save_file.txt')

    #~~~~~~~~~~~~~ROW1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if nextpage[0][0] == 1:
            slotcolour19 = RED
        if nextpage[0][0] == 2:
            slotcolour19 = GREEN
        if nextpage[0][0] == 3:
            slotcolour19 = WHITE
        if nextpage[0][0] == 4:
            slotcolour19 = YELLOW
        if nextpage[0][0] == 5:
            slotcolour19 = BLUE

        if nextpage[0][1] == 1:
            slotcolour18 = RED
        if nextpage[0][1] == 2:
            slotcolour18 = GREEN
        if nextpage[0][1] == 3:
            slotcolour18 = WHITE
        if nextpage[0][1] == 4:
            slotcolour18 = YELLOW
        if nextpage[0][1] == 5:
            slotcolour18 = BLUE

        if nextpage[0][2] == 1:
            slotcolour17 = RED
        if nextpage[0][2] == 2:
            slotcolour17 = GREEN
        if nextpage[0][2] == 3:
            slotcolour17 = WHITE
        if nextpage[0][2] == 4:
            slotcolour17 = YELLOW
        if nextpage[0][2] == 5:
            slotcolour17 = BLUE

        if nextpage[0][3] == 1:
            slotcolour20 = RED
        if nextpage[0][3] == 2:
            slotcolour20 = GREEN
        if nextpage[0][3] == 3:
            slotcolour20 = WHITE
        if nextpage[0][3] == 4:
            slotcolour20 = YELLOW
        if nextpage[0][3] == 5:
            slotcolour20 = BLUE

    #~~~~~~~~~~~~~ROW2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if nextpage[1][0] == 1:
            slotcolour15 = RED
        if nextpage[1][0] == 2:
            slotcolour15 = GREEN
        if nextpage[1][0] == 3:
            slotcolour15 = WHITE
        if nextpage[1][0] == 4:
            slotcolour15 = YELLOW
        if nextpage[1][0] == 5:
            slotcolour15 = BLUE
    
        if nextpage[1][1] == 1:
            slotcolour14 = RED
        if nextpage[1][1] == 2:
            slotcolour14 = GREEN
        if nextpage[1][1] == 3:
            slotcolour14 = WHITE
        if nextpage[1][1] == 4:
            slotcolour14 = YELLOW
        if nextpage[1][1] == 5:
            slotcolour14 = BLUE
    
        if nextpage[1][2] == 1:
            slotcolour13 = RED
        if nextpage[1][2] == 2:
            slotcolour13 = GREEN
        if nextpage[1][2] == 3:
            slotcolour13 = WHITE
        if nextpage[1][2] == 4:
            slotcolour13 = YELLOW
        if nextpage[1][2] == 5:
            slotcolour13 = BLUE
    
        if nextpage[1][3] == 1:
            slotcolour16 = RED
        if nextpage[1][3] == 2:
            slotcolour16 = GREEN
        if nextpage[1][3] == 3:
            slotcolour16= WHITE
        if nextpage[1][3] == 4:
            slotcolour16 = YELLOW
        if nextpage[1][3] == 5:
            slotcolour16 = BLUE

    #~~~~~~~~~~~~~ROW3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if nextpage[2][0] == 1:
            slotcolour11 = RED
        if nextpage[2][0] == 2:
            slotcolour11 = GREEN
        if nextpage[2][0] == 3:
            slotcolour11 = WHITE
        if nextpage[2][0] == 4:
            slotcolour11 = YELLOW
        if nextpage[2][0] == 5:
            slotcolour11 = BLUE
    
        if nextpage[2][1] == 1:
            slotcolour10 = RED
        if nextpage[2][1] == 2:
            slotcolour10 = GREEN
        if nextpage[2][1] == 3:
            slotcolour10 = WHITE
        if nextpage[2][1] == 4:
            slotcolour10 = YELLOW
        if nextpage[2][1] == 5:
            slotcolour10 = BLUE
    
        if nextpage[2][2] == 1:
            slotcolour9 = RED
        if nextpage[2][2] == 2:
            slotcolour9 = GREEN
        if nextpage[2][2] == 3:
            slotcolour9 = WHITE
        if nextpage[2][2] == 4:
            slotcolour9 = YELLOW
        if nextpage[2][2] == 5:
            slotcolour9 = BLUE
    
        if nextpage[2][3] == 1:
            slotcolour12 = RED
        if nextpage[2][3] == 2:
            slotcolour12 = GREEN
        if nextpage[2][3] == 3:
            slotcolour12 = WHITE
        if nextpage[2][3] == 4:
            slotcolour12 = YELLOW
        if nextpage[2][3] == 5:
            slotcolour12 = BLUE

    #~~~~~~~~~~~~~ROW4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if nextpage[3][0] == 1:
            slotcolour7 = RED
        if nextpage[3][0] == 2:
            slotcolour7 = GREEN
        if nextpage[3][0] == 3:
            slotcolour7 = WHITE
        if nextpage[3][0] == 4:
            slotcolour7 = YELLOW
        if nextpage[3][0] == 5:
            slotcolour7 = BLUE
    
        if nextpage[3][1] == 1:
            slotcolour6 = RED
        if nextpage[3][1] == 2:
            slotcolour6 = GREEN
        if nextpage[3][1] == 3:
            slotcolour6 = WHITE
        if nextpage[3][1] == 4:
            slotcolour6 = YELLOW
        if nextpage[3][1] == 5:
            slotcolour6 = BLUE
    
        if nextpage[3][2] == 1:
            slotcolour5 = RED
        if nextpage[3][2] == 2:
            slotcolour5 = GREEN
        if nextpage[3][2] == 3:
            slotcolour5 = WHITE
        if nextpage[3][2] == 4:
            slotcolour5 = YELLOW
        if nextpage[3][2] == 5:
            slotcolour5 = BLUE

        if nextpage[3][3] == 1:
            slotcolour8 = RED
        if nextpage[3][3] == 2:
            slotcolour8 = GREEN
        if nextpage[3][3] == 3:
            slotcolour8 = WHITE
        if nextpage[3][3] == 4:
            slotcolour8 = YELLOW
        if nextpage[3][3] == 5:
            slotcolour8 = BLUE

    #~~~~~~~~~~~~~ROW5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if nextpage[4][0] == 1:
            slotcolour3 = RED
        if nextpage[4][0] == 2:
            slotcolour3 = GREEN
        if nextpage[4][0] == 3:
            slotcolour3 = WHITE
        if nextpage[4][0] == 4:
            slotcolour3 = YELLOW
        if nextpage[4][0] == 5:
            slotcolour3 = BLUE
    
        if nextpage[4][1] == 1:
            slotcolour2 = RED
        if nextpage[4][1] == 2:
            slotcolour2 = GREEN
        if nextpage[4][1] == 3:
            slotcolour2 = WHITE
        if nextpage[4][1] == 4:
            slotcolour2 = YELLOW
        if nextpage[4][1] == 5:
            slotcolour2 = BLUE

        if nextpage[4][2] == 1:
            slotcolour1 = RED
        if nextpage[4][2] == 2:
            slotcolour1 = GREEN
        if nextpage[4][2] == 3:
            slotcolour1 = WHITE
        if nextpage[4][2] == 4:
            slotcolour1 = YELLOW
        if nextpage[4][2] == 5:
            slotcolour1 = BLUE
    
        if nextpage[4][3] == 1:
            slotcolour4 = RED
        if nextpage[4][3] == 2:
            slotcolour4 = GREEN
        if nextpage[4][3] == 3:
            slotcolour4 = WHITE
        if nextpage[4][3] == 4:
            slotcolour4 = YELLOW
        if nextpage[4][3] == 5:
            slotcolour4 = BLUE

        #setting the y values for the first row (inside the run function so that it is constant)
        row1y = 100

        #setting the x values for each slot in a row
        slot1x = 430
        slot2x = 330
        slot3x = 230
        slot4x = 530

        #main loop
        main = True
        while main:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    main = False
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_q: #the player can press "q" at any time to quit
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_ESCAPE: #the player can return to the menu by pressing esc
                        menu()

            #creating rects for all the slots
            slot1Rect = pygame.Rect(slot1x,row1y,r*2,r*2)
            slot2Rect = pygame.Rect(slot2x,row1y,r*2,r*2)
            slot3Rect = pygame.Rect(slot3x,row1y,r*2,r*2)
            slot4Rect = pygame.Rect(slot4x,row1y,r*2,r*2)

            slot5Rect = pygame.Rect(slot1x,row2y,r*2,r*2)
            slot6Rect = pygame.Rect(slot2x,row2y,r*2,r*2)
            slot7Rect = pygame.Rect(slot3x,row2y,r*2,r*2)
            slot8Rect = pygame.Rect(slot4x,row2y,r*2,r*2)

            slot9Rect = pygame.Rect(slot1x,row3y,r*2,r*2)
            slot10Rect = pygame.Rect(slot2x,row3y,r*2,r*2)
            slot11Rect = pygame.Rect(slot3x,row3y,r*2,r*2)
            slot12Rect = pygame.Rect(slot4x,row3y,r*2,r*2)

            slot13Rect = pygame.Rect(slot1x,row4y,r*2,r*2)
            slot14Rect = pygame.Rect(slot2x,row4y,r*2,r*2)
            slot15Rect = pygame.Rect(slot3x,row4y,r*2,r*2)
            slot16Rect = pygame.Rect(slot4x,row4y,r*2,r*2)

            slot17Rect = pygame.Rect(slot1x,row5y,r*2,r*2)
            slot18Rect = pygame.Rect(slot2x,row5y,r*2,r*2)
            slot19Rect = pygame.Rect(slot3x,row5y,r*2,r*2)
            slot20Rect = pygame.Rect(slot4x,row5y,r*2,r*2)

            screen.fill(MUD) #setting the background colour

            #drawing all the balls and slots on the screen
            pygame.draw.circle(screen, slotcolour1, slot1Rect.center, r)
            pygame.draw.circle(screen, slotcolour2, slot2Rect.center, r)
            pygame.draw.circle(screen, slotcolour3, slot3Rect.center, r)
            pygame.draw.circle(screen, slotcolour4, slot4Rect.center, r)

            pygame.draw.circle(screen, slotcolour5, slot5Rect.center, r)
            pygame.draw.circle(screen, slotcolour6, slot6Rect.center, r)
            pygame.draw.circle(screen, slotcolour7, slot7Rect.center, r)
            pygame.draw.circle(screen, slotcolour8, slot8Rect.center, r)

            pygame.draw.circle(screen, slotcolour8, slot8Rect.center, r)
            pygame.draw.circle(screen, slotcolour9, slot9Rect.center, r)
            pygame.draw.circle(screen, slotcolour10, slot10Rect.center, r)
            pygame.draw.circle(screen, slotcolour11, slot11Rect.center, r)
            pygame.draw.circle(screen, slotcolour12, slot12Rect.center, r)

            pygame.draw.circle(screen, slotcolour13, slot13Rect.center, r)
            pygame.draw.circle(screen, slotcolour14, slot14Rect.center, r)
            pygame.draw.circle(screen, slotcolour15, slot15Rect.center, r)
            pygame.draw.circle(screen, slotcolour16, slot16Rect.center, r)

            pygame.draw.circle(screen, slotcolour17, slot17Rect.center, r)
            pygame.draw.circle(screen, slotcolour18, slot18Rect.center, r)
            pygame.draw.circle(screen, slotcolour19, slot19Rect.center, r)
            pygame.draw.circle(screen, slotcolour20, slot20Rect.center, r)

            triRect = pygame.Rect((screenWidth//2)-r,540,r*2,r*2)

            pygame.draw.polygon(screen, BROWN, points=[(375,50+500), (400,75+500), (425,50+500)]) #arrow to move screen down

            #pygame.draw.circle(screen, RED, triRect.center, r) #to show the hitbox of the arrow

            if(triRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                mastermind()

            fontTitle = pygame.font.SysFont("arial",40)

            backTitle = fontTitle.render("Back to Guess", True, BLACK) # render the text into an image of the text, colour is black

            backRect = backTitle.get_rect(center = pygame.display.get_surface().get_rect().center) # create a rect from the text
            # place this rect at the centre of the screen
            backRect.center = (screenWidth / 2), (screenHeight / 2)
            backRect.x = int(screenWidth//2)-125
            backRect.y = screenHeight-150
            screen.blit(backTitle, backRect)

            pygame.display.flip() #updating the display
    run()

def mastermind(): #main game
    choices = [1,2,3,4,5] #creating a list for all 5 balls
    balls = random.sample(choices, 4) #choosing 4 of the balls out of the 5
    random.shuffle(balls) #shuffling the 4 balls randomly

    game_start_time = time.time() #setting a variable for the time that the game was started

    def init(): #setting a function to initialize all the starting variables (run once at the start of the game)
        global prevguess, slotcolour5, slotcolour6, slotcolour7, slotcolour8, slotcolour9, slotcolour10, slotcolour11, slotcolour12, slotcolour13, slotcolour14, slotcolour15, slotcolour16, slotcolour17, slotcolour18, slotcolour19, slotcolour20, row2y, row3y, row4y, row5y, count, lookclicked
        prevguess = [] #creating a list for the previous guess

        #setting the y variables for the different rows
        row2y = 175
        row3y = 250
        row4y = 325
        row5y = 400

        #setting the colours for each of the slots
        slotcolour5 = BROWN
        slotcolour6 = BROWN
        slotcolour7 = BROWN
        slotcolour8 = BROWN

        slotcolour9 = BROWN
        slotcolour10 = BROWN
        slotcolour11 = BROWN
        slotcolour12 = BROWN

        slotcolour13 = BROWN
        slotcolour14 = BROWN
        slotcolour15 = BROWN
        slotcolour16 = BROWN

        slotcolour17 = BROWN
        slotcolour18 = BROWN
        slotcolour19 = BROWN
        slotcolour20 = BROWN

        lookclicked = False
    init()

    #functions for filling the previous guesses
    def fillguess():
        global prevguess, slotcolour5, slotcolour6, slotcolour7, slotcolour8

        cache = prevguess.copy() #creating a cache variable to store a copy of the previous guess

        # writing the colours of the previous guess to the next line
        if cache[0] == 1:
            slotcolour7 = RED
        if cache[0] == 2:
            slotcolour7 = GREEN
        if cache[0] == 3:
            slotcolour7 = WHITE
        if cache[0] == 4:
            slotcolour7 = YELLOW
        if cache[0] == 5:
            slotcolour7 = BLUE

        if cache[1] == 1:
            slotcolour6 = RED
        if cache[1] == 2:
            slotcolour6 = GREEN
        if cache[1] == 3:
            slotcolour6 = WHITE
        if cache[1] == 4:
            slotcolour6 = YELLOW
        if cache[1] == 5:
            slotcolour6 = BLUE

        if cache[2] == 1:
            slotcolour5 = RED
        if cache[2] == 2:
            slotcolour5 = GREEN
        if cache[2] == 3:
            slotcolour5 = WHITE
        if cache[2] == 4:
            slotcolour5 = YELLOW
        if cache[2] == 5:
            slotcolour5 = BLUE

        if cache[3] == 1:
            slotcolour8 = RED
        if cache[3] == 2:
            slotcolour8 = GREEN
        if cache[3] == 3:
            slotcolour8 = WHITE
        if cache[3] == 4:
            slotcolour8 = YELLOW
        if cache[3] == 5:
            slotcolour8 = BLUE
        
        file=open('save_file.txt','w')
        for items in cache:
            file.writelines(str(items)+' ')
        file.close()

    def fillguess1():
        global prevguess, slotcolour9, slotcolour10, slotcolour11, slotcolour12

        cache1 = prevguess.copy()

        if cache1[0] == 1:
            slotcolour11 = RED
        if cache1[0] == 2:
            slotcolour11 = GREEN
        if cache1[0] == 3:
            slotcolour11 = WHITE
        if cache1[0] == 4:
            slotcolour11 = YELLOW
        if cache1[0] == 5:
            slotcolour11 = BLUE

        if cache1[1] == 1:
            slotcolour10 = RED
        if cache1[1] == 2:
            slotcolour10 = GREEN
        if cache1[1] == 3:
            slotcolour10 = WHITE
        if cache1[1] == 4:
            slotcolour10 = YELLOW
        if cache1[1] == 5:
            slotcolour10 = BLUE

        if cache1[2] == 1:
            slotcolour9 = RED
        if cache1[2] == 2:
            slotcolour9 = GREEN
        if cache1[2] == 3:
            slotcolour9 = WHITE
        if cache1[2] == 4:
            slotcolour9 = YELLOW
        if cache1[2] == 5:
            slotcolour9 = BLUE

        if cache1[3] == 1:
            slotcolour12 = RED
        if cache1[3] == 2:
            slotcolour12 = GREEN
        if cache1[3] == 3:
            slotcolour12 = WHITE
        if cache1[3] == 4:
            slotcolour12 = YELLOW
        if cache1[3] == 5:
            slotcolour12 = BLUE

        file=open('save_file.txt','a')
        file.writelines('\n')
        for items in cache1:
            file.writelines(str(items)+' ')
        file.close()

    def fillguess2():
        global prevguess, slotcolour13, slotcolour14, slotcolour15, slotcolour16

        cache2 = prevguess.copy()

        if cache2[0] == 1:
            slotcolour15 = RED
        if cache2[0] == 2:
            slotcolour15 = GREEN
        if cache2[0] == 3:
            slotcolour15 = WHITE
        if cache2[0] == 4:
            slotcolour15 = YELLOW
        if cache2[0] == 5:
            slotcolour15 = BLUE

        if cache2[1] == 1:
            slotcolour14 = RED
        if cache2[1] == 2:
            slotcolour14 = GREEN
        if cache2[1] == 3:
            slotcolour14 = WHITE
        if cache2[1] == 4:
            slotcolour14 = YELLOW
        if cache2[1] == 5:
            slotcolour14 = BLUE

        if cache2[2] == 1:
            slotcolour13 = RED
        if cache2[2] == 2:
            slotcolour13 = GREEN
        if cache2[2] == 3:
            slotcolour13 = WHITE
        if cache2[2] == 4:
            slotcolour13 = YELLOW
        if cache2[2] == 5:
            slotcolour13 = BLUE

        if cache2[3] == 1:
            slotcolour16 = RED
        if cache2[3] == 2:
            slotcolour16 = GREEN
        if cache2[3] == 3:
            slotcolour16 = WHITE
        if cache2[3] == 4:
            slotcolour16 = YELLOW
        if cache2[3] == 5:
            slotcolour16 = BLUE

        file=open('save_file.txt','a')
        file.writelines('\n')
        for items in cache2:
            file.writelines(str(items)+' ')
        file.close()

    def fillguess3():
        global prevguess, slotcolour17, slotcolour18, slotcolour19, slotcolour20

        cache3 = prevguess.copy()

        if cache3[0] == 1:
            slotcolour19 = RED
        if cache3[0] == 2:
            slotcolour19 = GREEN
        if cache3[0] == 3:
            slotcolour19 = WHITE
        if cache3[0] == 4:
            slotcolour19 = YELLOW
        if cache3[0] == 5:
            slotcolour19 = BLUE

        if cache3[1] == 1:
            slotcolour18 = RED
        if cache3[1] == 2:
            slotcolour18 = GREEN
        if cache3[1] == 3:
            slotcolour18 = WHITE
        if cache3[1] == 4:
            slotcolour18 = YELLOW
        if cache3[1] == 5:
            slotcolour18 = BLUE

        if cache3[2] == 1:
            slotcolour17 = RED
        if cache3[2] == 2:
            slotcolour17 = GREEN
        if cache3[2] == 3:
            slotcolour17 = WHITE
        if cache3[2] == 4:
            slotcolour17 = YELLOW
        if cache3[2] == 5:
            slotcolour17 = BLUE

        if cache3[3] == 1:
            slotcolour20 = RED
        if cache3[3] == 2:
            slotcolour20 = GREEN
        if cache3[3] == 3:
            slotcolour20 = WHITE
        if cache3[3] == 4:
            slotcolour20 = YELLOW
        if cache3[3] == 5:
            slotcolour20 = BLUE

        file=open('save_file.txt','a')
        file.writelines('\n')
        for items in cache3:
            file.writelines(str(items)+' ')
        file.close()

    def writeguess1():
        global prevguess, slotcolour17, slotcolour18, slotcolour19, slotcolour20

        cache4 = prevguess.copy()

        file=open('save_file.txt','a')
        file.writelines('\n')
        for items in cache4:
            file.writelines(str(items)+' ')
        file.close()

    def run():
        global prevguess, slotcolour5, slotcolour6, slotcolour7, slotcolour8, row2y, row3y, row4y, row5y, count, elapsed
        by = 500 #setting the y values for the balls
        r = 20 #setting the radius for the balls

        # setting colours for the four main slots  
        slotcolour1 = BROWN
        slotcolour2 = BROWN
        slotcolour3 = BROWN
        slotcolour4 = BROWN

        #setting the y values for the first row (inside the run function so that it is constant)
        row1y = 100

        #setting the x values for each slot in a row
        slot1x = 430
        slot2x = 330
        slot3x = 230
        slot4x = 530

        #setting the colours for the balls
        ballcolour1 = YELLOW
        ballcolour2 = GREEN
        ballcolour3 = RED
        ballcolour4 = BLUE
        ballcolour5 = WHITE

        #making sure that none of the balls are selected at the start
        ball1clicked = False
        ball2clicked = False
        ball3clicked = False
        ball4clicked = False
        ball5clicked = False

        #making sure that all the balls are present at the start
        ball1gone = False
        ball2gone = False
        ball3gone = False
        ball4gone = False
        ball5gone = False

        #making sure none of the clickable slots are filled
        slot1filled = False
        slot2filled = False
        slot3filled = False
        slot4filled = False

        #setting variables to store the amount of correct guesses and correct positions (they will be changed later)
        correctguesses = 0
        correctpos = 0

        once = False

        #setting variables for the sounds that will be used in the game
        slotsound = pygame.mixer.Sound('Snap.wav')
        newrowsound = pygame.mixer.Sound('whoosh.wav')
        wrongbuzzer = pygame.mixer.Sound('wrongbuzzer.wav')
        winsound = pygame.mixer.Sound('win.wav')

        #main loop
        main = True
        while main:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    main = False
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_q: #the player can press "q" at any time to quit
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_ESCAPE: #the player can return to the menu by pressing esc
                        menu()

            #creating rects for all the balls
            ball1Rect = pygame.Rect(490,by,r*2,r*2)
            ball2Rect = pygame.Rect(270,by,r*2,r*2)
            ball3Rect = pygame.Rect(150,by,r*2,r*2)
            ball4Rect = pygame.Rect(600,by,r*2,r*2)
            ball5Rect = pygame.Rect(380,by,r*2,r*2)

            #creating rects for all the slots
            slot1Rect = pygame.Rect(slot1x,row1y,r*2,r*2)
            slot2Rect = pygame.Rect(slot2x,row1y,r*2,r*2)
            slot3Rect = pygame.Rect(slot3x,row1y,r*2,r*2)
            slot4Rect = pygame.Rect(slot4x,row1y,r*2,r*2)

            slot5Rect = pygame.Rect(slot1x,row2y,r*2,r*2)
            slot6Rect = pygame.Rect(slot2x,row2y,r*2,r*2)
            slot7Rect = pygame.Rect(slot3x,row2y,r*2,r*2)
            slot8Rect = pygame.Rect(slot4x,row2y,r*2,r*2)

            slot9Rect = pygame.Rect(slot1x,row3y,r*2,r*2)
            slot10Rect = pygame.Rect(slot2x,row3y,r*2,r*2)
            slot11Rect = pygame.Rect(slot3x,row3y,r*2,r*2)
            slot12Rect = pygame.Rect(slot4x,row3y,r*2,r*2)

            slot13Rect = pygame.Rect(slot1x,row4y,r*2,r*2)
            slot14Rect = pygame.Rect(slot2x,row4y,r*2,r*2)
            slot15Rect = pygame.Rect(slot3x,row4y,r*2,r*2)
            slot16Rect = pygame.Rect(slot4x,row4y,r*2,r*2)

            slot17Rect = pygame.Rect(slot1x,row5y,r*2,r*2)
            slot18Rect = pygame.Rect(slot2x,row5y,r*2,r*2)
            slot19Rect = pygame.Rect(slot3x,row5y,r*2,r*2)
            slot20Rect = pygame.Rect(slot4x,row5y,r*2,r*2)

            screen.fill(MUD) #setting the background colour

            #drawing all the balls and slots on the screen
            pygame.draw.circle(screen, slotcolour1, slot1Rect.center, r)
            pygame.draw.circle(screen, slotcolour2, slot2Rect.center, r)
            pygame.draw.circle(screen, slotcolour3, slot3Rect.center, r)
            pygame.draw.circle(screen, slotcolour4, slot4Rect.center, r)

            pygame.draw.circle(screen, slotcolour5, slot5Rect.center, r)
            pygame.draw.circle(screen, slotcolour6, slot6Rect.center, r)
            pygame.draw.circle(screen, slotcolour7, slot7Rect.center, r)
            pygame.draw.circle(screen, slotcolour8, slot8Rect.center, r)

            pygame.draw.circle(screen, slotcolour8, slot8Rect.center, r)
            pygame.draw.circle(screen, slotcolour9, slot9Rect.center, r)
            pygame.draw.circle(screen, slotcolour10, slot10Rect.center, r)
            pygame.draw.circle(screen, slotcolour11, slot11Rect.center, r)
            pygame.draw.circle(screen, slotcolour12, slot12Rect.center, r)

            pygame.draw.circle(screen, slotcolour13, slot13Rect.center, r)
            pygame.draw.circle(screen, slotcolour14, slot14Rect.center, r)
            pygame.draw.circle(screen, slotcolour15, slot15Rect.center, r)
            pygame.draw.circle(screen, slotcolour16, slot16Rect.center, r)

            pygame.draw.circle(screen, slotcolour17, slot17Rect.center, r)
            pygame.draw.circle(screen, slotcolour18, slot18Rect.center, r)
            pygame.draw.circle(screen, slotcolour19, slot19Rect.center, r)
            pygame.draw.circle(screen, slotcolour20, slot20Rect.center, r)

            if difficulty == "Easy" and count == 5:
                triRect = pygame.Rect((screenWidth//2)-r,20,r*2,r*2)

                pygame.draw.polygon(screen, BROWN, points=[(375,50), (400,25), (425,50)]) #arrow to move screen up

                #pygame.draw.circle(screen, RED, triRect.center, r) #to show the hitbox of the arrow

                if(triRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                    count = 5
                    run2()

            pygame.draw.circle(screen, ballcolour1, ball1Rect.center, r)
            pygame.draw.circle(screen, ballcolour2, ball2Rect.center, r)
            pygame.draw.circle(screen, ballcolour3, ball3Rect.center, r)
            pygame.draw.circle(screen, ballcolour4, ball4Rect.center, r)
            pygame.draw.circle(screen, ballcolour5, ball5Rect.center, r)

            if OSTon == True:
                smallfont = pygame.font.SysFont("arial",30)

                # render the text into an image of the text, colour is red
                targetTitle = smallfont.render("TARGET: {0}".format(balls), True, WHITE)
                # create a rect from the text
                targetRect = targetTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
                # place this rect at the centre of the screen
                
                targetRect.center = (screenWidth / 2), (screenHeight / 2)

                targetRect.x = int(screenWidth//2)-125
                targetRect.y = int(screenHeight//2)-275

                screen.blit(targetTitle, targetRect)

            pygame.display.flip() #updating the display

            if(ball1Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                ball2clicked = False
                ball3clicked = False
                ball4clicked = False
                ball5clicked = False
                ball1clicked = True

            if(slot1Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball1clicked == True and ball1gone != True and slot1filled != True:
                ball1clicked = False
                ball1gone = True
                slotcolour1 = ballcolour1
                slot1filled = True
                slotsound.play()
                prevguess.append(4)
                print ("slot1 is filled")
                pygame.display.flip()

            if(slot2Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball1clicked == True and ball1gone != True and slot2filled != True:
                ball1clicked = False
                ball1gone = True
                slotcolour2 = ballcolour1
                slot2filled = True
                slotsound.play()
                prevguess.append(4)
                print ("slot2 is filled")
                pygame.display.flip()

            if(slot3Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball1clicked == True and ball1gone != True and slot3filled != True:
                ball1clicked = False
                ball1gone = True
                slotcolour3 = ballcolour1
                slot3filled = True
                slotsound.play()
                prevguess.append(4)
                print ("slot3 is filled")
                pygame.display.flip()

            if(slot4Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball1clicked == True and ball1gone != True and slot4filled != True:
                ball1clicked = False
                ball1gone = True
                slotcolour4 = ballcolour1
                slot4filled = True
                slotsound.play()
                prevguess.append(4)
                print ("slot4 is filled")
                pygame.display.flip()


            if(ball2Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                ball1clicked = False
                ball3clicked = False
                ball4clicked = False
                ball5clicked = False
                ball2clicked = True
            
            if(slot1Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball2clicked == True and ball2gone != True and slot1filled != True:
                ball2clicked = False
                ball2gone = True
                slotcolour1 = ballcolour2
                slot1filled = True
                slotsound.play()
                prevguess.append(2)
                print ("slot1 is filled")
                pygame.display.flip()

            if(slot2Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball2clicked == True and ball2gone != True and slot2filled != True:
                ball2clicked = False
                ball2gone = True
                slotcolour2 = ballcolour2
                slot2filled = True
                slotsound.play()
                prevguess.append(2)
                print ("slot2 is filled")
                pygame.display.flip()

            if(slot3Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball2clicked == True and ball2gone != True and slot3filled != True:
                ball2clicked = False
                ball2gone = True
                slotcolour3 = ballcolour2
                slot3filled = True
                slotsound.play()
                prevguess.append(2)
                print ("slot3 is filled")
                pygame.display.flip()

            if(slot4Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball2clicked == True and ball2gone != True and slot4filled != True:
                ball2clicked = False
                ball2gone = True
                slotcolour4 = ballcolour2
                slot4filled = True
                slotsound.play()
                prevguess.append(2)
                print ("slot4 is filled")
                pygame.display.flip()

            if(ball3Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                ball1clicked = False
                ball2clicked = False
                ball4clicked = False
                ball5clicked = False
                ball3clicked = True
            
            if(slot1Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball3clicked == True and ball3gone != True and slot1filled != True:
                ball3clicked = False
                ball3gone = True
                slotcolour1 = ballcolour3
                slot1filled = True
                slotsound.play()
                prevguess.append(1)
                print ("slot1 is filled")
                pygame.display.flip()

            if(slot2Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball3clicked == True and ball3gone != True and slot2filled != True:
                ball3clicked = False
                ball3gone = True
                slotcolour2 = ballcolour3
                slot2filled = True
                slotsound.play()
                prevguess.append(1)
                print ("slot2 is filled")
                pygame.display.flip()

            if(slot3Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball3clicked == True and ball3gone != True and slot3filled != True:
                ball3clicked = False
                ball3gone = True
                slotcolour3 = ballcolour3
                slot3filled = True
                slotsound.play()
                prevguess.append(1)
                print ("slot3 is filled")
                pygame.display.flip()

            if(slot4Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball3clicked == True and ball3gone != True and slot4filled != True:
                ball3clicked = False
                ball3gone = True
                slotcolour4 = ballcolour3
                slot4filled = True
                slotsound.play()
                prevguess.append(1)
                print ("slot4 is filled")
                pygame.display.flip()

            if(ball4Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                ball1clicked = False
                ball2clicked = False
                ball3clicked = False
                ball5clicked = False
                ball4clicked = True
            
            if(slot1Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball4clicked == True and ball4gone != True and slot1filled != True:
                ball4clicked = False
                ball4gone = True
                slotcolour1 = ballcolour4
                slot1filled = True
                slotsound.play()
                prevguess.append(5)
                print ("slot1 is filled")
                pygame.display.flip()

            if(slot2Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball4clicked == True and ball4gone != True and slot2filled != True:
                ball4clicked = False
                ball4gone = True
                slotcolour2 = ballcolour4
                slot2filled = True
                slotsound.play()
                prevguess.append(5)
                print ("slot2 is filled")
                pygame.display.flip()

            if(slot3Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball4clicked == True and ball4gone != True and slot3filled != True:
                ball4clicked = False
                ball4gone = True
                slotcolour3 = ballcolour4
                slot3filled = True
                slotsound.play()
                prevguess.append(5)
                print ("slot3 is filled")
                pygame.display.flip()

            if(slot4Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball4clicked == True and ball4gone != True and slot4filled != True:
                ball4clicked = False
                ball4gone = True
                slotcolour4 = ballcolour4
                slot4filled = True
                slotsound.play()
                prevguess.append(5)
                print ("slot4 is filled")
                pygame.display.flip()

            if(ball5Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                ball1clicked = False
                ball2clicked = False
                ball3clicked = False
                ball5clicked = True
                ball4clicked = False
            
            if(slot1Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball5clicked == True and ball5gone != True and slot1filled != True:
                ball5clicked = False
                ball5gone = True
                slotcolour1 = ballcolour5
                slot1filled = True
                slotsound.play()
                prevguess.append(3)
                print ("slot1 is filled")
                pygame.display.flip()

            if(slot2Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball5clicked == True and ball5gone != True and slot2filled != True:
                ball5clicked = False
                ball5gone = True
                slotcolour2 = ballcolour5
                slot2filled = True
                slotsound.play()
                prevguess.append(3)
                print ("slot2 is filled")
                pygame.display.flip()

            if(slot3Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball5clicked == True and ball5gone != True and slot3filled != True:
                ball5clicked = False
                ball5gone = True
                slotcolour3 = ballcolour5
                slot3filled = True
                slotsound.play()
                prevguess.append(3)
                print ("slot3 is filled")
                pygame.display.flip()

            if(slot4Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) and ball5clicked == True and ball5gone != True and slot4filled != True:
                ball5clicked = False
                ball5gone = True
                slotcolour4 = ballcolour5
                slot4filled = True
                slotsound.play()
                prevguess.append(3)
                print ("slot4 is filled")
                pygame.display.flip()
            
            #if a ball is gone, its colour will be changed to the background colour (making it invisible)
            if ball1gone == True:
                ballcolour1 = MUD

            if ball2gone == True:
                ballcolour2 = MUD

            if ball3gone == True:
                ballcolour3 = MUD

            if ball4gone == True:
                ballcolour4 = MUD

            if ball5gone == True:
                ballcolour5 = MUD

            smallfont = pygame.font.SysFont("arial",20)

            #print (prevguess) #this was used for debugging

            if slot1filled == True and slot2filled == True and slot3filled == True and slot4filled == True and once == True: #code will be executed when this loop has been executed twice
                count += 1 #counting how many times the user has guessed
                if count == 1 or count == 6:
                    newrowsound.play()
                    current_time = time.time()
                    elapsed = current_time - game_start_time
                    fillguess()
                if count == 2 or count == 7:
                    row2y = 250
                    row3y = 175
                    row4y = 325
                    newrowsound.play()
                    current_time = time.time()
                    elapsed = current_time - game_start_time
                    fillguess1()
                if count == 3 or count == 8:
                    row2y += 75
                    row3y += 75
                    row4y = 175
                    newrowsound.play()
                    current_time = time.time()
                    elapsed = current_time - game_start_time
                    fillguess2()
                if count == 4 or count == 9:
                    row2y += 75
                    row3y += 75
                    row4y += 75
                    row5y = 175
                    newrowsound.play()
                    current_time = time.time()
                    elapsed = current_time - game_start_time
                    fillguess3()
                if count == 5 or count == 10:
                    writeguess1()
                if difficulty == "Easy" and count == 10 and correctpos != 4:
                    wrongbuzzer.play()
                    #when the user loses they go to an end screen so that the row will not clear
                    current_time = time.time()
                    elapsed = current_time - game_start_time #finding the user's time
                    gameover()

                #comparing the prevguess list with the balls list to determine if the guesses are correct
                if prevguess[0] == balls[0]:
                    correctpos += 1

                if prevguess[0] != balls[0]:
                    if prevguess[0] in balls:
                        correctguesses += 1

                if prevguess[1] == balls[1]:
                    correctpos += 1

                if prevguess[1] != balls[1]:
                    if prevguess[1] in balls:
                        correctguesses += 1

                if prevguess[2] == balls[2]:
                    correctpos += 1

                if prevguess[2] != balls[2]:
                    if prevguess[2] in balls:
                        correctguesses += 1

                if prevguess[3] == balls[3]:
                    correctpos += 1

                if prevguess[3] != balls[3]:
                    if prevguess[3] in balls:
                        correctguesses += 1

                if difficulty != "Impossible":
                    # render the text into an image of the text, colour is whit
                    textvar = "You guessed {:n} colours in the right position and {:n} right colours in the wrong position.".format(correctpos, correctguesses)
                    readout = smallfont.render(textvar, True, WHITE)
                    # create a rect from the text
                    readRect = readout.get_rect(center = pygame.display.get_surface().get_rect().center)
                    # place this rect at the centre of the screen
                    readRect.center = (screenWidth / 2), (screenHeight / 2)
                    readRect.x = 30
                    readRect.y = screenHeight - 100
                    pygame.draw.rect(screen, BLACK, readRect, 0)
                    screen.blit(readout, readRect)
                    pygame.display.flip()
                    time.sleep(2.5)
                else:
                    time.sleep(1)

                if TRon == True:
                    #console readout for debugging & cheat logic
                    print ("""
~~~~~~~READOUT~~~~~~~
                    """)
                    print ("Your Guess:", prevguess)
                    print ("Attempts: ", count)

                    if prevguess[0] == balls[0]:
                        print ("guess1 is correct!")

                    if prevguess[0] != balls[0]:
                        print ("guess1 is incorrect!")

                    if prevguess[1] == balls[1]:
                        print ("guess2 is correct!")

                    if prevguess[1] != balls[1]:
                        print ("guess2 is incorrect!")

                    if prevguess[2] == balls[2]:
                        print ("guess3 is correct!")

                    if prevguess[2] != balls[2]:
                        print ("guess3 is incorrect!")

                    if prevguess[3] == balls[3]:
                        print ("guess4 is correct!")

                    if prevguess[3] != balls[3]:
                        print ("guess4 is incorrect!")

                    print ("You guessed", correctpos, "colours in the right position and", correctguesses, "right colours in the wrong position")
                    print ("TARGET: ", balls) #printing the target list in the console for debugging (cheat)

                prevguess = [] #emptying the prevguess list

                if correctpos == 4: #if all the guesses are correct, the user goes to the win screen and a sound plays
                    winsound.play()
                    correct()
                if count == 5 and correctpos != 4:
                    if difficulty == "Hard":
                        wrongbuzzer.play()
                        #when the user loses they go to an end screen so that the row will not clear
                        current_time = time.time()
                        elapsed = current_time - game_start_time #finding the user's time
                        gameover()
                        print ("You have no more turns left :(")
                    if difficulty == "Easy":
                        if count == 5:
                            init()

                        if count == 10:
                            wrongbuzzer.play()
                            #when the user loses they go to an end screen so that the row will not clear
                            current_time = time.time()
                            elapsed = current_time - game_start_time #finding the user's time
                            gameover()
                            print ("You have no more turns left :(")

                    if difficulty == "Impossible":
                        wrongbuzzer.play()
                        #when the user loses they go to an end screen so that the row will not clear
                        current_time = time.time()
                        elapsed = current_time - game_start_time #finding the user's time
                        gameover()
                        print ("You have no more turns left :(")
                run()

            if slot1filled == True and slot2filled == True and slot3filled == True and slot4filled == True:
                once = True

            #setting the game speed
            clock.tick(FPS)

    run()

def gameover(): #gameover screen (loss)
    global elapsed
    smallTitle = pygame.font.SysFont("arial",35)
    fontTitle = pygame.font.SysFont("arial",50)

    main = True
    while main == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                sys.exit()

        clock.tick(FPS) # constrain this loop to the specified FPS
        
        screen.fill(PURPLISH)
        failImage = pygame.image.load('gameover24.jpg') #this image was found from: https://thehungryjpeg.com/product/3501235-game-over-games-screen-glitch-computer-video-gaming-phrase-and-playi
        screen.blit(failImage, (220, 10))

        time = "Time: {:.2f}s".format(elapsed)
        timeTitle = fontTitle.render(time, True, WHITE)
        timeRect = timeTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        timeRect.x = int(screenWidth//2)-300
        timeRect.y = int(screenHeight//2)-75

        screen.blit(timeTitle, timeRect)

        high = "Highscore: {:.2f}s".format(elapsed)
        highTitle = fontTitle.render(high, True, WHITE)
        highRect = highTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        highRect.x = int(screenWidth//2)-300
        highRect.y = int(screenHeight//2)+15

        screen.blit(highTitle, highRect)

        tries = "Attempts: {0}".format(count)
        triesTitle = fontTitle.render(tries, True, WHITE)
        triesRect = triesTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        triesRect.x = int(screenWidth//2)-300
        triesRect.y = int(screenHeight//2)+100

        screen.blit(triesTitle, triesRect)

        #render the text into an image of the text, colour is red
        backTitle = smallTitle.render("Main Menu", True, YELLOW)
        #create a rect from the text
        backRect = backTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        #place this rect at the centre of the screen

        backRect.center = (screenWidth / 2), (screenHeight / 2)

        backRect.x = 40
        backRect.y = screenHeight-100

        screen.blit(backTitle, backRect)

        #render the text into an image of the text, colour is red
        qTitle = smallTitle.render("Quit", True, RED)
        #create a rect from the text
        qRect = qTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        #place this rect at the centre of the screen

        qRect.center = (screenWidth / 2), (screenHeight / 2)

        qRect.x = screenWidth-115
        qRect.y = screenHeight-100

        screen.blit(qTitle, qRect)

        pygame.display.flip()

        if(backRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            menu()

        elif(qRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()

def correct(): #gameover screen (win)
    global elapsed, count
    smallTitle = pygame.font.SysFont("arial",35)
    fontTitle = pygame.font.SysFont("arial",50)

    clock.tick(FPS) # constrain this loop to the specified FPS                      

    screen.fill(PURPLISH)
    correctImage = pygame.image.load('correctimg.jpg') #this image was created using: https://web.over.app/
    screen.blit(correctImage, (220, 10))

    time = "Time: {:.2f}s".format(elapsed)
    timeTitle = fontTitle.render(time, True, WHITE)
    timeRect = timeTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
    timeRect.x = int(screenWidth//2)-300
    timeRect.y = int(screenHeight//2)-75

    screen.blit(timeTitle, timeRect)

    high = "Best Time: {:.2f}s".format(elapsed)
    highTitle = fontTitle.render(high, True, WHITE)
    highRect = highTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
    highRect.x = int(screenWidth//2)-300
    highRect.y = int(screenHeight//2)+15

    screen.blit(highTitle, highRect)

    tries = "Attempts: {0}".format(count)
    triesTitle = fontTitle.render(tries, True, WHITE)
    triesRect = triesTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
    triesRect.x = int(screenWidth//2)-300
    triesRect.y = int(screenHeight//2)+100

    screen.blit(triesTitle, triesRect)

    #render the text into an image of the text, colour is red
    backTitle = smallTitle.render("Play Again", True, YELLOW)
    #create a rect from the text
    backRect = backTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
    #place this rect at the centre of the screen

    backRect.center = (screenWidth / 2), (screenHeight / 2)

    backRect.x = 40
    backRect.y = screenHeight-100

    screen.blit(backTitle, backRect)

    # render the text into an image of the text, colour is red
    qTitle = smallTitle.render("Quit", True, RED)
    # create a rect from the text
    qRect = qTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
    # place this rect at the centre of the screen

    qRect.center = (screenWidth / 2), (screenHeight / 2)

    qRect.x = screenWidth-115
    qRect.y = screenHeight-100

    screen.blit(qTitle, qRect)

    pygame.display.flip()

    main = True
    while main == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                sys.exit()

        if(backRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            mastermind()

        elif(qRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()

def menu(): #main menu
    global count
    fontTitle = pygame.font.SysFont("arial",50)
    count = 0 #setting a counter variable to check which attempt the user is on

    main = True
    while main == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit()
                sys.exit()

        clock.tick(FPS) #constraining this loop to the specified FPS
        screen.fill(BLACK) #setting the background colour

        # render the text into an image of the text, colour is red
        mastermindTitle = fontTitle.render("Play", True, WHITE)
        # create a rect from the text
        mastermindRect = mastermindTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        mastermindRect.center = (screenWidth / 2), (screenHeight / 2)

        mastermindRect.x = int(screenWidth//2)-45
        mastermindRect.y = int(screenHeight//2)-200

        screen.blit(mastermindTitle, mastermindRect)

        # render the text into an image of the text, colour is red
        helpTitle = fontTitle.render("Instructions", True, WHITE)
        # create a rect from the text
        helpRect = helpTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        
        helpRect.center = (screenWidth / 2), (screenHeight / 2)

        helpRect.x = int(screenWidth//2)-125
        helpRect.y = int(screenHeight//2)-15

        screen.blit(helpTitle, helpRect)

        # render the text into an image of the text, colour is red
        quitTitle = fontTitle.render("Quit", True, WHITE)
        # create a rect from the text
        quitRect = quitTitle.get_rect(center = pygame.display.get_surface().get_rect().center)
        # place this rect at the centre of the screen
        quitRect.center = (screenWidth / 2), (screenHeight / 2)

        quitRect.x = int(screenWidth//2)-45
        quitRect.y = int(screenHeight//2)+150

        screen.blit(quitTitle, quitRect)

        pygame.display.flip()

        #checking if any of the buttons are clicked
        if(mastermindRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            diffselect()

        elif(quitRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()
            
        elif(helpRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            inst()
menu() #running the menu function at the start of the program (no other function is called)

