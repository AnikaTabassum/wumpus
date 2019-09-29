from AiAgent import Agent
from GameOverException import GameOverException
from WumpusWorldGenerator import WumpusWorldGenerator
import sys
import pygame
class Game():

	def __init__(self, agent,size, wumpusProb, pitProb, obsProb,screen, rectangleHeight,rectangleWidth):
		print("Game initiated")
		#self.knowledgeBase=KnowledgeBase()
		self.agentt=agent
		self.wwg=WumpusWorldGenerator()
		#self.world=self.wwg.generateWorld(size,wumpusProb, pitProb, obsProb)
		self.world=self.wwg.generatePredefinedWorld(size,wumpusProb, pitProb, obsProb)
		self.agentt.position = self.wwg.startingPosition
		self.score=1000
		self.gameOver=False
		self.ge=GameOverException()
		self.screen=screen
		self.rectangleHeight=rectangleHeight
		self.rectangleWidth=rectangleWidth
		self.goldpic = pygame.image.load(r'/home/anika/Downloads/gold.png')

	def getScore(self):
		return self.score

	def moveAgent(self):
		oldPos=[self.agentt.position[0],self.agentt.position[1]]

		if self.world[oldPos[0]+self.agentt.direction[0]][oldPos[1]+self.agentt.direction[1]]==3:
			#print("-------------------------------------obstacle----------------------------------")
			return False
		elif self.world[oldPos[0]+self.agentt.direction[0]][oldPos[1]+self.agentt.direction[1]]==1 or \
		self.world[oldPos[0]+self.agentt.direction[0]][oldPos[1]+self.agentt.direction[1]]==2:
			print("breeze or stench. gelei mrittu")
			self.score-=1000
			self.agentt.died=True
			self.gameOver=True
			print("score is ", self.getScore())
			pygame.time.wait(9000)
			sys.exit()
			self.ge.exception(False)
		#print("direction ",self.agentt.direction)
		#print("move agents kakakakak  ", self.agentt.position[0],",",self.agentt.position[1])
		self.agentt.position[0]=self.agentt.position[0]+self.agentt.direction[0]
		self.agentt.position[1]=self.agentt.position[1]+self.agentt.direction[1]
		#agentPos=self.agentt.setPosition(self.agentt.position,self.agentt.direction)
		### set percepts
		#print("move agents before ", self.agentt.position[0],",",self.agentt.position[1])

		if self.world[self.agentt.position[0]-1][self.agentt.position[1]]==1 or \
		self.world[self.agentt.position[0]+1][self.agentt.position[1]]==1 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]+1]==1 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]-1]==1:
			#print("stench er if")
			self.agentt.placeStench(True)
			#self.agentt.stench=True

		else:
			self.agentt.placeStench(False)
			#self.agentt.stench=False

		if self.world[self.agentt.position[0]-1][self.agentt.position[1]]==2 or \
		self.world[self.agentt.position[0]+1][self.agentt.position[1]]==2 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]+1]==2 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]-1]==2:
			#print("breeze er if")
			self.agentt.placeBreeze(True)
			#self.agentt.breeze=True
		else:
			self.agentt.placeBreeze(False)
			#self.agentt.breeze=False

		if self.world[self.agentt.position[0]][self.agentt.position[1]]==4:
			#sprint("Glimmer if")

			self.agentt.placeGlimmer(True)
			
			#self.agentt.glimmer=True
		else:
			self.agentt.placeGlimmer(False)
			#self.agentt.glimmer=False
		print("move agents after ", self.agentt.position[0],",",self.agentt.position[1])
		self.score-=1

		return True

	def turnAgent(self,direction):
		#print("turn in game ",direction)
		if direction==self.agentt.LEFT:
			print("Agent turned left")
			if self.agentt.direction==self.agentt.knowledgeBase.NORTH:
				#self.agentt.direction=self.agentt.knowledgeBase.WEST
				#print("new direction set to be ", self.agentt.knowledgeBase.WEST)
				self.agentt.setDirection(self.agentt.knowledgeBase.WEST)
				#print("from north to west")
				#print("north to ",self.agentt.direction )
			elif self.agentt.direction==self.agentt.knowledgeBase.EAST:
				#-self.agentt.direction=self.agentt.knowledgeBase.NORTH
				#print("new direction set to be ", self.agentt.knowledgeBase.NORTH)
				self.agentt.setDirection(self.agentt.knowledgeBase.NORTH)
				#print("from east to north")
				#print("east to ",self.agentt.direction )
			elif self.agentt.direction==self.agentt.knowledgeBase.SOUTH:
				#self.agentt.direction=self.agentt.knowledgeBase.EAST
				#print("new direction set to be ", self.agentt.knowledgeBase.EAST)
				self.agentt.setDirection(self.agentt.knowledgeBase.EAST)
				#print("south to ",self.agentt.direction )
			elif self.agentt.direction==self.agentt.knowledgeBase.WEST:
				#self.agentt.direction=self.agentt.knowledgeBase.SOUTH
				#print("new direction set to be ", self.agentt.knowledgeBase.SOUTH)
				self.agentt.setDirection(self.agentt.knowledgeBase.SOUTH)
				#print("from west to south")
				#print("west to ",self.agentt.direction )
			else:
				print("asha uchit hoynai baam dik theke")
				sys.exit()

		elif direction==self.agentt.RIGHT:
			print("Agent turned right")
			if self.agentt.direction==self.agentt.knowledgeBase.NORTH:
				#self.agentt.direction=self.agentt.knowledgeBase.EAST
				self.agentt.setDirection(self.agentt.knowledgeBase.EAST)
				#print("new direction set to be ", self.agentt.knowledgeBase.EAST)
			elif self.agentt.direction==self.agentt.knowledgeBase.EAST:
				#self.agentt.direction=self.agentt.knowledgeBase.SOUTH
				self.agentt.setDirection(self.agentt.knowledgeBase.SOUTH)
				#print("new direction set to be ", self.agentt.knowledgeBase.SOUTH)
			elif self.agentt.direction==self.agentt.knowledgeBase.SOUTH:
				#self.agentt.direction=self.agentt.knowledgeBase.WEST
				self.agentt.setDirection(self.agentt.knowledgeBase.WEST)
				#print("new direction set to be ", self.agentt.knowledgeBase.WEST)
			elif self.agentt.direction==self.agentt.knowledgeBase.WEST:
				#self.agentt.direction=self.agentt.knowledgeBase.NORTH
				self.agentt.setDirection(self.agentt.knowledgeBase.NORTH)
				#print("new direction set to be ", self.agentt.knowledgeBase.NORTH)
			else:
				print("asha uchit hoynai daan dik theke")
				sys.exit()
		else:
			print("Sesh .... kicchu hobe na tomake diye -_- ")
			sys.exit()

		self.score-=1

	def processShot(self):
		if self.agentt.direction==self.agentt.knowledgeBase.NORTH:
			for i in range(self.agentt.position[1], len(self.world)-1):
				if self.world[self.agentt.position[0]][i]==1:
					self.world[self.agentt.position[0]][i]==0
					self.agentt.scream=True
					return
				elif self.world[self.agentt.position[0]][i]==1:
					########jhmela ase mone hocchee################
					self.agentt.scream=False
					break
		elif self.agentt.direction==self.agentt.knowledgeBase.EAST:
			for i in range(self.agentt.position[0], len(self.world)-1):
				if self.world[i][self.agentt.position[1]]==1:
					self.world[i][self.agentt.position[1]]==0
					self.agentt.scream=True
					return
				elif self.world[i][self.agentt.position[1]]==1:
					########jhmela ase mone hocchee################
					self.agentt.scream=False
					break

		elif self.agentt.direction==self.agentt.knowledgeBase.SOUTH:
			for i in range(0,self.agentt.position[1]):
				if self.world[self.agentt.position[0]][i]==1:
					self.world[self.agentt.position[0]][i]==0
					self.agentt.scream=True
					return
				elif self.world[self.agentt.position[0]][i]==1:
					########jhmela ase mone hocchee################
					self.agentt.scream=False
					break

		elif self.agentt.direction==self.agentt.knowledgeBase.WEST:
			for i in range(0,self.agentt.position[0]):
				if self.world[i][self.agentt.position[1]]==1:
					self.world[i][self.agentt.position[1]]==0
					self.agentt.scream=True
					return
				elif self.world[i][self.agentt.position[1]]==1:
					########jhmela ase mone hocchee################
					self.agentt.scream=False
					break
			
		else:
			print("Arrow tao marte paro na.. gadha kothakar")


	def agentGrabsGold(self):
		#print("oooooooooooooooooooo ",self.world[self.agentt.position[0]][self.agentt.position[1]])
		if self.world[self.agentt.position[0]][self.agentt.position[1]]==int(4):
			#print("ppppppppppppppppppppppppppppppppppppppppppppppppppppppppp", self.agentt.position[0],",",self.agentt.position[1])
			print("Agent is grabbing gold")
			self.world[self.agentt.position[0]][self.agentt.position[1]]=0
			self.score+=1000
			file = '/home/anika/Downloads/success.mp3'
			c=self.agentt.position[0]
			r=self.agentt.position[1]
			red = (255,0,0)
			font =pygame.font.SysFont("comicsansms", 70)
			winner="You have won the game!! score: "+str(self.getScore())
			label = font.render(winner, 1, red)
			self.screen.blit(label, (30,10))
			self.screen.blit(self.goldpic, (c*self.rectangleWidth, r*self.rectangleHeight+self.rectangleHeight)) 
			pygame.display.update()
			pygame.mixer.init()
			pygame.mixer.music.load(file)
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy(): 
				pygame.time.Clock().tick(10)
			self.ge.exception(True)
			
			
		else:
			print("Gold nai gold nai.. faka she cell :)")




if __name__ == '__main__':
	Game()