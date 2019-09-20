#choose option random world or pre-defined world
#generateRandomBoard()  or generateDefinedBoard()
#
import pygame
import sys
import os
import math
import random

# Tile Structure
class cellState:
    breeze = False;
    stench = False;
    wumpus = False;
    pit    = False;
    gold   = False;
    glitter= False;

colDimension = 10
rowDimension = 10
khaki = ( 240,230,140)
darkOliveGreen = ( 85,107,47)
red = (255,0,0)
blue= (0,0,205)
rectangleHeight=83
rectangleWidth=115
radius = 50
width=1150
height=910
size = (width, height)
stench = pygame.image.load(r'/home/anika/Downloads/stench.jpg')
breeze = pygame.image.load(r'/home/anika/Downloads/breeze.png')
wumpus = pygame.image.load(r'/home/anika/Downloads/wumpus.png')
gold = pygame.image.load(r'/home/anika/Downloads/gold.png')
pit = pygame.image.load(r'/home/anika/Downloads/pit.jpg')
screen = pygame.display.set_mode(size)
pygame.init()
board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]

def boundCheck(c,r):
    if(c>=0 and r>=0 and c<colDimension and r<rowDimension):
        return True

def addBreeze(c,r):
    if(boundCheck(c,r)):
        board[c][r].breeze=True

def addStench(c,r):
    if(boundCheck(c,r)):
        board[c][r].stench=True

def addGold(c,r):
    if(boundCheck(c,r)):
        board[c][r].gold=True

def addPit(c,r):
    if(boundCheck(c,r)):
        board[c][r].pit=True
        addBreeze(c,r+1)
        addBreeze(c,r-1)
        addBreeze(c+1,r)
        addBreeze(c-1,r)

def addWumpus(c,r):
    if(boundCheck(c,r)):
        board[c][r].wumpus=True
        addStench(c,r+1)
        addStench(c,r-1)
        addStench(c+1,r)
        addStench(c-1,r)

def printBoard():



    for r in range (rowDimension):
        cellInfo=""
        for c in range (colDimension):


            cellInfo+= "\t"+str(r) +", "+ str(c) +" : "

            if(r==0 and c==0):
                cellInfo+=" agent "


            if board[c][r].stench:
                cellInfo+="stench"
                screen.blit(stench, (c*rectangleWidth, r*rectangleHeight+rectangleHeight)) 
                pygame.display.update()
            elif board[c][r].wumpus:
                cellInfo+="wumpus"
                screen.blit(wumpus, ((c*rectangleWidth)+30, (r*rectangleHeight+rectangleHeight)+30))
                pygame.display.update()
            elif board[c][r].pit:
                cellInfo+="pit"
                screen.blit(pit, ((c*rectangleWidth)+30, (r*rectangleHeight+rectangleHeight)+30))
                pygame.display.update()
            elif board[c][r].breeze:
                cellInfo+="breeze"
                screen.blit(breeze, ((c*rectangleWidth)+70, (r*rectangleHeight+rectangleHeight)+60))
                pygame.display.update()
            elif board[c][r].gold:
                cellInfo+="gold"
                screen.blit(gold, ((c*rectangleWidth)+30, (r*rectangleHeight+rectangleHeight)+30)) 
                pygame.display.update()
            elif board[c][r].glitter:
                cellInfo+="glitter"

            else:
                cellInfo+="empty"

        print(cellInfo)


        print("\n")




def addFeatures ( ):
        # Generate pits
        for r in range (rowDimension):
            for c in range (colDimension):
                if (c != 0 or r != 0) and random.randrange(10) < 3: #etaaaaaaki
                    addPit ( c, r )

        # Generate wumpus
        wummpusC = 0
        wumpusR = 0

        while wummpusC == 0 and wumpusR == 0:
            wummpusC = random.randrange(colDimension)
            wumpusR = random.randrange(rowDimension)

        addWumpus ( wummpusC, wumpusR );

        # Generate gold
        goldC = 0
        goldR = 0

        while goldC == 0 and goldR == 0:
            goldC = random.randrange(colDimension)
            goldR = random.randrange(rowDimension)

        addGold ( goldC, goldR )


def main():


    board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]
    #addFeatures()

    #print("Want to play in a random world or predefined world?")
    #inp=input("Enter 1 for random world, 2 for predefined world")
    #print(input)

    #if(inp==1):
        #generateRandomBoard
        #printBoard

    print("Showing board for random world")
    print("\n")
    for c in range(colDimension):
        for r in range(rowDimension):
            pygame.draw.rect(screen, khaki, (c*rectangleWidth, r*rectangleHeight+rectangleHeight, rectangleWidth, rectangleHeight))
            pygame.draw.rect(screen, darkOliveGreen, (c*rectangleWidth-1, r*rectangleHeight+rectangleHeight-1, rectangleWidth-1, rectangleHeight-1))
            pygame.display.update()
    addFeatures()
    printBoard()
    

    #if(inp==2):
        #generateDefinedBoard
        #printBoard


main()
pygame.time.wait(9000)



