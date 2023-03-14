#JESSE $ KEVIN R------------------------------------
import pygame
import random
import winsound
import math
pygame.init()#initializes Pygame
pygame.display.set_caption("Simon!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

#game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers in a TUPLE
turn = False
pattern = [] #this holds the random pattern
playerPattern = []
hasClicked = False
ded = False
pi = 3.1415

#draw everything first so things don't appear one at a time
pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
#more colors go here!   
pygame.display.flip()

def collision(xpos, ypos):
    if math.sqrt((xpos - 400)**2 + (ypos - 400)**2)>200 or math.sqrt((xpos - 400)**2 + (ypos - 400)**2)<100 :
        print("Outside of ring")
        return -1
    elif xpos < 400 and ypos < 400:
        print("Over the red button")
        pygame.draw.arc(screen, (255,0,0), (200,200,400,400), pi/2, pi, 100)
        pygame.display.flip()
        winsound.Beep(440, 500)
        return 0
    elif xpos < 400 and ypos > 400:
        print("Over the green button")
        pygame.draw.arc(screen, (0,255,0), (200,200,400,400), pi, (3*pi/2), 100)
        pygame.display.flip()
        winsound.Beep(640, 500)
        return 1
    elif xpos > 400 and ypos > 400:
        print("Over the blue")
        pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (3*pi/2), 0, 100)
        pygame.display.flip()
        winsound.Beep(840, 500)
        return 2
    elif xpos > 400 and ypos < 400:
        print("Over the yellow button")
        pygame.draw.arc(screen, (255,255,0), (200, 200, 400, 400), 0, (pi/2), 100)
        pygame.display.flip()
        winsound.Beep(1040, 500)       
        return 3

#gameloop###################################################
while ded == False:
    
    event = pygame.event.wait()#event queue 

    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break
 
    if event.type == pygame.MOUSEBUTTONDOWN:
        hasClicked = True
        #collision(mousePos[0], mousePos[1])
        playerPattern.append(collision(mousePos[0], mousePos[1]))
        print(playerPattern)
    
        

    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        print(mousePos[0],",",mousePos[1])
        

    
    if turn == True:
        if len(playerPattern) < len(pattern):
            if hasClicked == True:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False

        else:
            for i in range(len(pattern)):
                if playerPattern[i] != pattern[i]:
                    ded = True
            pattern.clear()
            turn = False
            pygame.time.wait(800)

    
    
    #update section---------------------------------------------
    
    if turn == False and ded == False:
        pattern.append(random.randrange(0, 4)) #push a new value into the pattern list
        
        #brighten colors and play beep for each number in the pattern
        for i in range(len(pattern)): 
            if pattern[i]==0: #RED
                pygame.draw.arc(screen, (255, 0,0), (200,200,400,400), pi/2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
                
            if pattern[i]==1:#GREEN
                pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)

            if pattern[i]==2:
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (3*pi/2), 0, 100)
                pygame.display.flip()
                winsound.Beep(840, 500)

            if pattern[i]==3:
                pygame.draw.arc(screen, (255,255,0), (200, 200, 400, 400), 0, (pi/2), 100)
                pygame.display.flip()
                winsound.Beep(1040, 500)
                
            #redraw board after every beep
            pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
            pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
            pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3*pi/2), 0, 100)
            pygame.draw.arc(screen, (155,155,0), (200, 200, 400, 400), 0, (pi/2), 100)
            pygame.display.flip()
            pygame.time.wait(800) #slows the game down a bit
            #playerPattern.clear()
            turn = True 
            
    #render section---------------------------------------------
    
    #game board
    pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3*pi/2), 0, 100)
    pygame.draw.arc(screen, (155,155,0), (200, 200, 400, 400), 0, (pi/2), 100)
    #more colors go here!
   
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()
