from Game import Game
from GameOverException import GameOverException
from AiAgent import Agent
import pygame
class Driver:
	def run(self):
		ge=GameOverException()
		agent=Agent()
		dimension=int(10)
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
		for c in range(dimension):
			for r in range(dimension):
				pygame.draw.rect(screen, khaki, (c*rectangleWidth, r*rectangleHeight+rectangleHeight, rectangleWidth, rectangleHeight))
				pygame.draw.rect(screen, darkOliveGreen, (c*rectangleWidth-1, r*rectangleHeight+rectangleHeight-1, rectangleWidth-1, rectangleHeight-1))
				pygame.display.update()
		game=Game(agent,dimension,wumpusProb,pitProb,obsProb,screen,rectangleHeight,rectangleWidth)
		try:
			agent.start(game,screen,rectangleHeight,rectangleWidth)
		except Exception as e:
			print(ge.win)
			print(e)
			if ge.checkWin():
				print("agent won the game")
			else:
				print("agent lost the game")
			print("Score: ",game.getScore())
wumpusProb=0.05
pitProb=0.05
obsProb=0.05
Driver().run()