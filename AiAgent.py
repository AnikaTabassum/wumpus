import pygame
import math
import sys
from KnowledgeBase import KnowledgeBase
from WumpusWorldGenerator import WumpusWorldGenerator
class Agent():

	def __init__(self):
		print("Agent initiaated")
		self.knowledgeBase=""
		self.LEFT=int(0)
		self.RIGHT=int(1)
		self.position=[0,0]
		self.direction=""
		self.breeze = False;
		self.bump=False
		self.died=False
		self.stench = False;
		self.scream = False;
		self.haveGold   = False;
		self.glimmer= False;
		self.game=""
		#self.quiver=WumpusWorldGenerator().numWmpi		
		self.quiver=1
	def start(self,Game):
		self.game=Game
		self.knowledgeBase=KnowledgeBase()
		self.direction=self.knowledgeBase.NORTH
		print("position ",self.position[0],",",self.position[1])
		self.knowledgeBase.registerMove(self.position[0],self.position[1])
		i=int (0)
		while True:
			self.infer()
			

	def move(self):
		#print("move")
		if not self.game.moveAgent():
			print("-----------------------telling bump-----------------------")
			self.knowledgeBase.tellBump(self.position[0],self.position[1],self.direction)
			return 
		x=int(self.position[0])
		y=int(self.position[1])

		self.knowledgeBase.registerMove(x,y)
		self.processPercepts(x,y)

	def processPercepts(self,x,y):
		print("perceive",self.glimmer)
		if self.glimmer:

			self.knowledgeBase.tellGlimmer(x,y)
			#sys.exit()
		if not self.breeze and not self.stench:
			self.knowledgeBase.tellClear(x,y)
			return 
		print("breeze ",self.breeze)
		if self.breeze:
			self.knowledgeBase.tellBreeze(x,y)
		print("stench ",self.stench)
		if self.stench:
			self.knowledgeBase.tellStench(x,y)
	def setDirection(self, directionanika):
		print('direction anika', directionanika)
		self.direction=directionanika
	def turn(self, direction):
		print("direction in agent ",direction)
		self.game.turnAgent(direction)
		self.knowledgeBase.registerTurn(direction)
	def setPosition(self, position, direction):
		self.agentt.position[0]=self.agentt.position[0]+self.agentt.direction[0]
		self.agentt.position[1]=self.agentt.position[1]+self.agentt.direction[1]

	def placeGlimmer(self, flag):
		print("placeGlimmer")
		self.glimmer=flag
	def placeBreeze(self,flag):
		self.breeze=flag
	def placeStench(self,flag):
		self.stench=flag
	def shoot(self):
		quiver-=1
		print("agent loosed the arrow")
		game.processShot()
		self.processPercepts(position[0], position[1])

	def pickUp(self):
		self.game.agentGrabsGold()
		print("agent picked up the gold")

	def backTrack(self, moveStack,riskFactor):
		print("backtrack")
		i=int(self.lookback(riskFactor))
		print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ",i)
		print("move ", moveStack)
		if i<0:
			return False
		#moveStacking=self.knowledgeBase.returnMoveStack()
		cell= moveStack[i]
		print("Backtracking to [",cell[0],", ",cell[1],"]")
		tempMoveStack=self.knowledgeBase.returnMoveStack()
		tempTurnStack=self.knowledgeBase.returnTurnStack()
		print("moveStack size ", len(tempMoveStack), "tempTurnStack size ", len(tempTurnStack))

		try:
			print("try in backTrack")
			self.turn(self.LEFT)
			self.turn(self.LEFT)
			self.move()

			while self.position[0]!= cell[0] or self.position[1]!= cell[1]:
				nextMove=tempMoveStack[len(tempMoveStack)-1]
				if self.position[0]+self.direction[0]== nextMove[0] and \
				self.position[1]+ self.direction[1]==nextMove[1]:
					self.move()
					tempMoveStack.pop(tempMoveStack[len(tempMoveStack)-1])
				else:
					print("backtrack er else")
					turnnn=int(tempTurnStack[len(tempTurnStack)-1])
					if turnnn==self.LEFT:
						self.turn(self.RIGHT)
						tempTurnStack.pop(tempTurnStack[len(tempTurnStack)-1])
					elif turnnn== self.RIGHT:
						self.turn(self.LEFT)
						tempTurnStack.pop(tempTurnStack[len(tempTurnStack)-1])

			return True
		except IndexError:
			print("inenenene")
			return False

	def lookback(self, riskFactor):
		##eita likhbo
		i=int(0)
		moveStacking=self.knowledgeBase.returnMoveStack()
		print("riskfaactor in lookback ",riskFactor, len(moveStacking)-1)
		i=int(len(moveStacking))
		while i<=0:
			i-=1
			m=self.knowledgeBase.moveStack[i]
			for d in self.knowledgeBase.DIRECTIONS:
				x=int(m[0]+d[0])
				y=int(m[1]+d[1])

				if self.knowledgeBase.askPath(x,y) ==0 and self.knowledgeBase.askObstacle(x,y)<=0:
					if self.knowledgeBase.askWumpus(x,y)+self.knowledgeBase.askPit(x,y)<=riskFactor:
						print("Lookback succeded")
						return i
		print("Lookback failed")
		return -1



	def infer(self):

		###eita most important

		
		if self.knowledgeBase.askGlimmer(self.position[0],self.position[1]):
			print("infer glimmer")
			self.pickUp()
			return 
		'''except Exception as error:
			print('Caught this error: ' + repr(error))'''

		riskFactor=int(-2)
		i=int(0)
		while True:
			

			print("infer()\n\tpos:[", self.position[0],",",self.position[1],"]\n\tdirection:{",\
				self.direction[0],",",self.direction[1],"}\n\triskFactor",riskFactor)
			forwardScore=sys.maxsize
			leftScore=sys.maxsize
			rightScore=sys.maxsize
			#print("maxxxxxx \tforwardDanger: ", forwardScore, "\n\trightDanger: ", rightScore, "\n\tleftDanger: ",leftScore)
			if self.direction==self.knowledgeBase.NORTH:
				
				forwardScore=self.knowledgeBase.askWumpus(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askPit(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askObstacle(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askPath(self.position[0], self.position[1]+1)

				rightScore=self.knowledgeBase.askWumpus(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askPit(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askObstacle(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askPath(self.position[0]+1, self.position[1])

				leftScore=self.knowledgeBase.askWumpus(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askPit(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askObstacle(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askPath(self.position[0]-1, self.position[1])

				print("NORTH", forwardScore," ", leftScore," ",rightScore)
			elif self.direction==self.knowledgeBase.SOUTH:
				print("SOUTH")
				forwardScore=self.knowledgeBase.askWumpus(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askPit(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askObstacle(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askPath(self.position[0], self.position[1]-1)

				rightScore=self.knowledgeBase.askWumpus(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askPit(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askObstacle(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askPath(self.position[0]-1, self.position[1])

				leftScore=self.knowledgeBase.askWumpus(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askPit(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askObstacle(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askPath(self.position[0]+1, self.position[1])

			elif self.direction==self.knowledgeBase.EAST:
				print("EAST")
				forwardScore=self.knowledgeBase.askWumpus(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askPit(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askObstacle(self.position[0]+1, self.position[1])+\
				self.knowledgeBase.askPath(self.position[0]+1, self.position[1])

				rightScore=self.knowledgeBase.askWumpus(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askPit(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askObstacle(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askPath(self.position[0], self.position[1]-1)

				leftScore=self.knowledgeBase.askWumpus(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askPit(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askObstacle(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askPath(self.position[0], self.position[1]+1)

			elif self.direction==self.knowledgeBase.WEST:
				print("WEST")
				forwardScore=self.knowledgeBase.askWumpus(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askPit(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askObstacle(self.position[0]-1, self.position[1])+\
				self.knowledgeBase.askPath(self.position[0]-1, self.position[1])

				rightScore=self.knowledgeBase.askWumpus(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askPit(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askObstacle(self.position[0], self.position[1]+1)+\
				self.knowledgeBase.askPath(self.position[0], self.position[1]+1)

				leftScore=self.knowledgeBase.askWumpus(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askPit(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askObstacle(self.position[0], self.position[1]-1)+\
				self.knowledgeBase.askPath(self.position[0], self.position[1]-1)

			else:
				print("Direction did not match in infer()")

			print("\tforwardDanger: ", forwardScore, "\n\trightDanger: ", rightScore, "\n\tleftDanger: ",leftScore)

			if forwardScore<=riskFactor and forwardScore<=leftScore and forwardScore<=rightScore:
				self.move()
				print("move if -1")
				self.knowledgeBase.printing()
				return 
			elif leftScore<= riskFactor and leftScore <= rightScore:
				self.turn(self.LEFT)
				#print("check")
				self.move()
				print("move if -2")
				self.knowledgeBase.printing()
				return 
			elif rightScore<=riskFactor:
				self.turn(self.RIGHT)
				#print("check")
				self.move()
				print("move if -3")
				self.knowledgeBase.printing()
				return
			else:
				print("-----------------check-------------------------")
				moveStacking=self.knowledgeBase.returnMoveStack()
				backTracked=self.backTrack(moveStacking,riskFactor)
				if backTracked:
					print("\tbacktracked")
					return
				else:
					print("\tno suitable backtrack")
			riskFactor+=1



if __name__ == '__main__':
	Agent()