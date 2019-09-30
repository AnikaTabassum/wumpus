import pygame
import math
import sys
from KnowledgeBase import KnowledgeBase
from WumpusWorldGenerator import WumpusWorldGenerator
class Agent():

	def __init__(self):
		#print("Agent initiaated")
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
		self.screen=""
		self.rectangleHeight=""
		self.rectangleWidth=""
		self.back=pygame.image.load(r'/home/anika/Downloads/back.jpg')
		self.mirror=pygame.image.load(r'/home/anika/Downloads/mirroredagent.png')
		#self.quiver=WumpusWorldGenerator().numWmpi		
		self.quiver=1
	def start(self,Game,screen,rectangleHeight,rectangleWidth):
		self.game=Game
		self.screen=screen
		self.rectangleHeight=rectangleHeight
		self.rectangleWidth=rectangleWidth
		self.knowledgeBase=KnowledgeBase(screen,rectangleHeight,rectangleWidth)
		self.direction=self.knowledgeBase.NORTH
		#print("position ",self.position[0],",",self.position[1])
		self.knowledgeBase.registerMove(self.position[0],self.position[1])
		i=int (0)
		while True:
			self.infer()
			

	def move(self):
		#print("move")
		if not self.game.moveAgent():
			#print("-----------------------telling bump-----------------------")
			self.knowledgeBase.tellBump(self.position[0],self.position[1],self.direction)
			return 
		x=int(self.position[0])
		y=int(self.position[1])

		self.knowledgeBase.registerMove(x,y)
		self.processPercepts(x,y)
		#print("here")

	def getxy(self):
		moveStack=self.knowledgeBase.returnMoveStack()
		lastX=moveStack[len(moveStack)-1][0]
		lastY=moveStack[len(moveStack)-1][1]
		#print(lastX)
		#print(lastY)
		self.game.guiCreate(lastX,lastY)

	def processPercepts(self,x,y):
		#print("perceive",self.glimmer)
		if self.glimmer:
		
			self.knowledgeBase.tellGlimmer(x,y)
			#sys.exit()
		if not self.breeze and not self.stench:
			
			self.knowledgeBase.tellClear(x,y)
		
			return 
		#print("breeze ",self.breeze)
		if self.breeze:
			
			self.knowledgeBase.tellBreeze(x,y)
		#print("stench ",self.stench)
		if self.stench:
			#print("addddddddddd")
			self.knowledgeBase.tellStench(x,y)
		#print("pepepep")
	def setDirection(self, directionanika):
		#print('direction anika', directionanika)
		self.direction=directionanika
	def turn(self, direction):
		#print("direction in agent ",direction)
		self.game.turnAgent(direction)
		
		self.knowledgeBase.registerTurn(direction)
		#print("hhhhrrrrrrriiiiiiiiiiiiiddddddddiiiiiiiiiiiiiiiittttttttaaaaaaaaaaaa")
	def turnForLookback(self, direction):
		self.game.turnAgent(direction)
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
		self.quiver-=1
		print("agent loosed the arrow")
		self.game.processShot()
		self.processPercepts(self.position[0], self.position[1])

	def pickUp(self):
		self.game.agentGrabsGold()
		print("agent picked up the gold")
		print("score is ", self.game.getScore())
		pygame.time.wait(5000)
		sys.exit()

	def oppositeDirection(self,direction):
		if direction==self.knowledgeBase.NORTH:
			return self.knowledgeBase.SOUTH
		elif direction==self.knowledgeBase.SOUTH:
			return self.knowledgeBase.NORTH
		elif direction==self.knowledgeBase.EAST:
			return self.knowledgeBase.WEST
		elif direction==self.knowledgeBase.WEST:
			return self.knowledgeBase.EAST

	def backTrack(self, moveStack,riskFactor):
		#print("backtrack")
		i=int(self.lookback(riskFactor))
		#print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ",i)
		#print("move ", moveStack)
		if i<0:
			return False
		#moveStacking=self.knowledgeBase.returnMoveStack()
		cell= moveStack[i]
		#print("-----------------------------Backtracking to [",cell[0],", ",cell[1],"]")
		self.screen.blit(self.back, (cell[1]*self.rectangleWidth, cell[0]*self.rectangleHeight+self.rectangleHeight)) 
		pygame.display.update()
		pygame.time.wait(1000)
		#tempMoveStack=self.knowledgeBase.returnMoveStack()
		tempMoveStack=moveStack
		tempTurnStack=self.knowledgeBase.returnTurnStack()
		#print("moveStack size ", len(tempMoveStack), "tempTurnStack size ", len(tempTurnStack))

		try:
			#print("try in backTrack")
			self.turn(self.LEFT)
			self.turn(self.LEFT)
			self.move()
			#print("try")
			while self.position[0]!= cell[0] or self.position[1]!= cell[1]:
				nextMove=tempMoveStack[len(tempMoveStack)-1]
				oppDir=self.oppositeDirection(self.direction)
				#print("direction in infer ", oppDir[0],",",oppDir[1] )
				if self.position[0]+oppDir[0]== nextMove[0] and \
				self.position[1]+ oppDir[1]==nextMove[1]:
					self.move()
					#print("try-2")
					#print(tempMoveStack[len(tempMoveStack)-1])
					tempMoveStack.pop(len(tempMoveStack)-1)
					#print("mara")
				else:
					#print("backtrack er else")
					turnnn=int(tempTurnStack[len(tempTurnStack)-1])
					if turnnn==self.LEFT:
						self.turn(self.RIGHT)
						#print("aaaaaaaaannnnnnnnnnniiiiiiiiiiiiiiiiiiiiiikkkkkkkkkkkkkkaaaaaaaaaaa")
						tempTurnStack.pop(len(tempTurnStack)-1)
						break
					elif turnnn== self.RIGHT:
						self.turn(self.LEFT)
						#print("5555555555555555555555555555555555555555555555555555555555555555")
						tempTurnStack.pop(len(tempTurnStack)-1)
						break

			return True
		except IndexError:
			#print("inenenene")
			return False

	def lookback(self, riskFactor):
		##eita likhbo
		i=int(0)
		moveStacking=self.knowledgeBase.returnMoveStack()
		#print("riskfaactor in lookback ",riskFactor, len(moveStacking)-1)
		i=int(len(moveStacking))
		while i>=0:
			#print("-------------------while i------------------------------------ ", i)			
			i-=1
			m=moveStacking[i]
			#print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm ",m)
			for d in self.knowledgeBase.DIRECTIONS:
				x=int(m[0]+d[0])
				y=int(m[1]+d[1])
				#print("Directions in lookback ", x,",",y )

				if self.knowledgeBase.askPath(x,y) !=0 and self.knowledgeBase.askObstacle(x,y)<=0:
					#print("if if if if  ", x,",",y )
					#print("if er vitor if er if ",x,",",y, self.knowledgeBase.askWumpus(x,y))
					if (self.knowledgeBase.askWumpus(x,y)+self.knowledgeBase.askPit(x,y))<=riskFactor:
						#print("Lookback succeded")
						return i
		#print("Lookback failed")
		return -1



	def infer(self):

		###eita most important
		if self.knowledgeBase.askGlimmer(self.position[0],self.position[1]):
			#print("infer glimmer")
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

				#print("NORTH", forwardScore," ", leftScore," ",rightScore)
			elif self.direction==self.knowledgeBase.SOUTH:
				#print("SOUTH")
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
				#print("EAST")
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
				#print("WEST")
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
				#print("move if -1")
				self.knowledgeBase.printing()
				self.getxy()
				return 
			elif leftScore<= riskFactor and leftScore <= rightScore:
				self.turn(self.LEFT)
				#print("check")
				self.move()
				#print("move if -2")
				self.knowledgeBase.printing()
				self.getxy()
				return 
			elif rightScore<=riskFactor:
				self.turn(self.RIGHT)
				#print("check")
				self.move()
				#print("move if -3")
				self.knowledgeBase.printing()
				self.getxy()
				return
			else:
				#print("-----------------check-------------------------")
				moveStacking=self.knowledgeBase.returnMoveStack()
				#print("oononononono")
				backTracked=self.backTrack(moveStacking,riskFactor)
				if backTracked:
					print("\tbacktracked")
					return
				else:
					print("\tno suitable backtrack")
			riskFactor+=1



if __name__ == '__main__':
	Agent()