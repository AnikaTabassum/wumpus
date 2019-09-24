from Agent import Agent
from GameOverException import GameOverException
from WumpusWorldGenerator import WumpusWorldGenerator
class Game():

	def __init__(self, agent,size, wumpusProb, pitProb, obsProb):
		print("Game initiated")
		#self.knowledgeBase=KnowledgeBase()
		self.agentt=agent
		self.wwg=WumpusWorldGenerator()
		self.world=self.wwg.generateWorld(size,wumpusProb, pitProb, obsProb)
		self.agentt.position = self.wwg.startingPosition
		self.score=1000
		self.gameOver=False

	def getScore(self):
		return self.score

	def moveAgent(self):
		oldPos=[self.agentt.position[0],self.agentt.position[1]]
		if self.world[oldPos[0]+self.agentt.direction[0]][oldPos[1]+self.agentt.direction[1]]==3:
			return False
		elif self.world[oldPos[0]+self.agentt.direction[0]][oldPos[1]+self.agentt.direction[1]]==1 or \
		self.world[oldPos[0]+self.agentt.direction[0]][oldPos[1]+self.agentt.direction[1]]==2:
			self.score-=1000
			self.agentt.died=true
			self.gameOver=true
			GameOverException.exception(False)

		self.agentt.position[0]=self.agentt.position[0]+self.agentt.direction[0]
		self.agentt.position[1]=self.agentt.position[1]+self.agentt.direction[1]


		### set percepts

		if self.world[self.agentt.position[0]-1][self.agentt.position[1]]==1 or \
		self.world[self.agentt.position[1]+1][self.agentt.position[1]]==1 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]+1]==1 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]-1]==1:
			self.agentt.stench=True
		else:
			self.agentt.stench=False

		if self.world[self.agentt.position[0]-1][self.agentt.position[1]]==2 or \
		self.world[self.agentt.position[1]+1][self.agentt.position[1]]==2 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]+1]==2 or \
		self.world[self.agentt.position[0]][self.agentt.position[1]-1]==2:
			self.agentt.breeze=True
		else:
			self.agentt.breeze=False

		if world[self.agentt.position[0]][self.agentt.position[1]]==4:
			self.agentt.glimmer=True
		else:
			self.agentt.glimmer=False

		score-=1

		return True

	def turnAgent(self,direction):
		if self.agentt.direction==self.agentt.LEFT:
			print("Agent turned left")
			if self.agentt.direction==self.agentt.knowledgeBase.NORTH:
				self.agentt.direction=self.agentt.knowledgeBase.WEST
			elif self.agentt.direction==self.agentt.knowledgeBase.EAST:
				self.agentt.direction=self.agentt.knowledgeBase.NORTH
			elif self.agentt.direction==self.agentt.knowledgeBase.SOUTH:
				self.agentt.direction=self.agentt.knowledgeBase.EAST
			elif self.agentt.direction==self.agentt.knowledgeBase.WEST:
				self.agentt.direction=self.agentt.knowledgeBase.SOUTH
			else:
				print("asha uchit hoynai baam dik theke")

		elif self.agentt.direction==self.agentt.RIGHT:
			print("Agent turned right")
			if self.agentt.direction==self.agentt.knowledgeBase.NORTH:
				self.agentt.direction=self.agentt.knowledgeBase.EAST
			elif self.agentt.direction==self.agentt.knowledgeBase.EAST:
				self.agentt.direction=self.agentt.knowledgeBase.SOUTH
			elif self.agentt.direction==self.agentt.knowledgeBase.SOUTH:
				self.agentt.direction=self.agentt.knowledgeBase.WEST
			elif self.agentt.direction==self.agentt.knowledgeBase.WEST:
				self.agentt.direction=self.agentt.knowledgeBase.NORTH
			else:
				print("asha uchit hoynai daan dik theke")
		else:
			print("Sesh .... kicchu hobe na tomake diye -_- ")

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
		if self.world[self.agentt.position[0]][self.agentt.position[1]]==4:
			self.world[self.agentt.position[0]][self.agentt.position[1]]=0
			self.score+=1000
			GameOverException.exception(True)
		else:
			print("Gold nai gold nai.. faka she cell :)")




if __name__ == '__main__':
	Game()