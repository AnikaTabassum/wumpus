import pygame
import numpy as np
import random
import sys
import math
rows,columns = 10,10

khaki = ( 240,230,140)
darkOliveGreen = ( 85,107,47)
red = (255,0,0)
blue= (0,0,205)
rectangleHeight=83
rectangleWidth=115
radius = 50
width=1150
height=930
size = (width, height)
stench = pygame.image.load(r'/home/anika/Downloads/stench.jpg')
breeze = pygame.image.load(r'/home/anika/Downloads/breeze.png')
wumpus = pygame.image.load(r'/home/anika/Downloads/wumpus.png')
gold = pygame.image.load(r'/home/anika/Downloads/gold.png')
screen = pygame.display.set_mode(size)
pygame.init()
#pygame.display.update()
def initialization():
	board = np.zeros((rows,columns))
	return board
def makegui(board):
	for c in range(columns):
		for r in range(rows):
			pygame.draw.rect(screen, khaki, (c*rectangleWidth, r*rectangleHeight+rectangleHeight, rectangleWidth, rectangleHeight))
			pygame.draw.rect(screen, darkOliveGreen, (c*rectangleWidth-1, r*rectangleHeight+rectangleHeight-1, rectangleWidth-1, rectangleHeight-1))
			screen.blit(stench, (c*rectangleWidth, r*rectangleHeight+rectangleHeight)) 
			screen.blit(breeze, ((c*rectangleWidth)+70, (r*rectangleHeight+rectangleHeight)+60)) 
	screen.blit(wumpus, ((5*rectangleWidth)+30, (4*rectangleHeight+rectangleHeight)+30))
	screen.blit(gold, ((9*rectangleWidth)+30, (9*rectangleHeight+rectangleHeight)+30)) 
	pygame.display.update()
board = initialization()
makegui(board)
pygame.time.wait(9000)