from Agent import Agent
from WumpusWorldGenerator import WumpusWorldGenerator
class Game:
	def getScore(self):
		return score

	def moveAgent(self):
		oldPos=[Agent.position[0],Agent.position[1]]
		if world[oldPos[0]+Agent.direction[0]][oldPos[1]+Agent.direction[1]]==3:
			return False
		elif world[oldPos[0]+Agent.direction[0]][oldPos[1]+Agent.direction[1]]==1 or \
		world[oldPos[0]+Agent.direction[0]][oldPos[1]+Agent.direction[1]]==2:
			score-=1000
			Agent.died=true
			gameOver=true

		Agent.position[0]=Agent.position[0]+Agent.direction[0]
		Agent.position[1]=Agent.position[1]+Agent.direction[1]


		### set percepts

		if world[Agent.position[0]-1][Agent.position[1]]==1 or \
		world[Agent.position[1]+1][Agent.position[1]]==1 or \
		world[Agent.position[0]][Agent.position[1]+1]==1 or \
		world[Agent.position[0]][Agent.position[1]-1]==1:
			Agent.stench=True
		else:
			Agent.stench=False

		if world[Agent.position[0]-1][Agent.position[1]]==2 or \
		world[Agent.position[1]+1][Agent.position[1]]==2 or \
		world[Agent.position[0]][Agent.position[1]+1]==2 or \
		world[Agent.position[0]][Agent.position[1]-1]==2:
			Agent.breeze=True
		else:
			Agent.breeze=False

		if world[Agent.position[0]][Agent.position[1]]==4:
			Agent.glimmer=True
		else:
			Agent.glimmer=False

		score-=1

		return True

	def turnAgent(self,direction):
		if Agent.direction==Agent.LEFT:
			print("Agent turned left")
			if Agent.direction==Agent.knowledgeBase.NORTH:
				Agent.direction=Agent.knowledgeBase.WEST
			elif Agent.direction==Agent.knowledgeBase.EAST:
				Agent.direction=Agent.knowledgeBase.NORTH
			elif Agent.direction==Agent.knowledgeBase.SOUTH:
				Agent.direction=Agent.knowledgeBase.EAST
			elif Agent.direction==Agent.knowledgeBase.WEST:
				Agent.direction=Agent.knowledgeBase.SOUTH
			else:
				print("asha uchit hoynai baam dik theke")

		elif Agent.direction==Agent.RIGHT:
			print("Agent turned right")
			if Agent.direction==Agent.knowledgeBase.NORTH:
				Agent.direction=Agent.knowledgeBase.EAST
			elif Agent.direction==Agent.knowledgeBase.EAST:
				Agent.direction=Agent.knowledgeBase.SOUTH
			elif Agent.direction==Agent.knowledgeBase.SOUTH:
				Agent.direction=Agent.knowledgeBase.WEST
			elif Agent.direction==Agent.knowledgeBase.WEST:
				Agent.direction=Agent.knowledgeBase.NORTH
			else:
				print("asha uchit hoynai daan dik theke")
		else:
			print("Sesh .... kicchu hobe na tomake diye -_- ")

		score-=1

	def processShot(self):
		if Agent.direction==Agent.knowledgeBase.NORTH:
			for i in range(Agent.position[1], len(world)-1):
				if world[Agent.position[0]][i]==1:
					world[Agent.position[0]][i]==0
					Agent.scream=True
					return
				elif world[Agent.position[0]][i]==1:
					########jhmela ase mone hocchee################
					Agent.scream=False
					break
		elif Agent.direction==Agent.knowledgeBase.EAST:
			for i in range(Agent.position[0], len(world)-1):
				if world[i][Agent.position[1]]==1:
					world[i][Agent.position[1]]==0
					Agent.scream=True
					return
				elif world[i][Agent.position[1]]==1:
					########jhmela ase mone hocchee################
					Agent.scream=False
					break

		elif Agent.direction==Agent.knowledgeBase.SOUTH:
			for i in range(0,Agent.position[1]):
				if world[Agent.position[0]][i]==1:
					world[Agent.position[0]][i]==0
					Agent.scream=True
					return
				elif world[Agent.position[0]][i]==1:
					########jhmela ase mone hocchee################
					Agent.scream=False
					break

		elif Agent.direction==Agent.knowledgeBase.WEST:
			for i in range(0,Agent.position[0]):
				if world[i][Agent.position[1]]==1:
					world[i][Agent.position[1]]==0
					Agent.scream=True
					return
				elif world[i][Agent.position[1]]==1:
					########jhmela ase mone hocchee################
					Agent.scream=False
					break
			
		else:
			print("Arrow tao marte paro na.. gadha kothakar")


	def agentGrabsGold(self):
		if world[Agent.position[0]][Agent.position[1]]==4:
			world[Agent.position[0]][Agent.position[1]]=0
			score+=1000
		else:
			print("Gold nai gold nai.. faka she cell :)")


score=1000
size=int(10)
gameOver=False
wumpusProb=0.05
pitProb=0.05
obsProb=0.05
world=WumpusWorldGenerator.generateWorld(size,wumpusProb, pitProb, obsProb)
