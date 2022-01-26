import pygame #import needed libraries and files
import random
from Config import *
from Class import *
from network import *

win = pygame.display.set_mode((width, height)) #set window size
pygame.display.set_caption(clientcaption) #window caption

clientNumber = 0 #needed later for the networking

clock = pygame.time.Clock() #clock to tick on each display

def recpos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def createpos(tup):
    return str(tup[0]) + "," + str(tup[1])

def main(): #main loop
    n = Network(server, port)
    run = True
    player1 = player(1200, win, path, 0) #initialise first player
    player1.newhand(n.retpos()) #gives new hand
    player2 = player(1200, win, path, 1)
    player2.newhand(n.retpos())

    button1 = button(path + "Draw", 50, 200, win) # creates a new button
    while run == True: # run loop

        for event in pygame.event.get(): #continously checking for events

            if event.type == pygame.QUIT: #checking to see if game is quit by player
                run = False
                pygame.quit() #quits without crashing

            player1.event_handler(event) #player1 event handler
            player2.event_handler(event)
            button1.event_handler(event, player1.drawcards) #button1 event handler

        win.fill((255, 255, 255)) #screen background: white
        player1.drawhand() #displays hand every clocktick to update
        player2.drawhand()
        button1.draw() #draws the button every tick
        clock.tick(120) #clock ticking to new frame
        pygame.display.update() #updating the display at the end of every loop

main() #calling the main loop