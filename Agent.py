import pygame
from Game import Game
from KnowledgeBase import KnowledgeBase
from WumpusWorldGenerator import WumpusWorldGenerator
class Agent:
	def start(self,game):
		game=game
		KnowledgeBase.registerMove(position[0],position[1])
		while True:
			self.infer()

	def move(self):
		if Game.moveAgent():
			KnowledgeBase.tellBump(position[0],position[1],direction)
			return 
		x=int(position[0])
		y=int(position[1])

		KnowledgeBase.registerMove(x,y)
		self.processPercepts(x,y)

	def processPercepts(self,x,y):
		if glimmer:
			KnowledgeBase.tellGlimmer(x,y)
		if not breeze and not stench:
			KnowledgeBase.tellClear(x,y)
		if breeze:
			KnowledgeBase.tellBreeze(x,y)
		if stench:
			KnowledgeBase.tellStench(x,y)

	def turn(self, direction):
		Game.turnAgent(direction)
		KnowledgeBase.registerTurn(direction)

	def shoot(self):
		quiver-=1
		print("agent loosed the arrow")
		self.processPercepts(position[0], position[1])

	def pickUp(self):
		Game.agentGrabsGold()
		print("agent picked up the gold")

	def backTrack(self, moveStack,riskFactor):
		i=int(self.lookBack(riskFactor))
		if i<0:
			return False

		cell= KnowledgeBase.moveStack[i]
		print("Backtracking to [",cell[0],", ",cell[1],"]")
		tempMoveStack=KnowledgeBase.moveStack
		tempTurnStack=KnowledgeBase.turnStack
		print("moveStack size ", len(tempMoveStack), "tempTurnStack size ", len(tempTurnStack))

		try:
			self.turn(LEFT)
			self.turn(LEFT)
			self.move()

			while position[0]!= cell[0] or position[1]!= cell[1]:
				nextMove=tempMoveStack[len(tempTurnStack)-1]
				if position[0]+direction[0]== nextMove[0] and \
				position[1]+ direction[1]= nextMove[1]:
					self.move()
					tempMoveStack.remove(tempMoveStack[len(tempMoveStack)-1])
				else:
					turn=int(tempTurnStack[len(tempTurnStack)-1])
					if turn==LEFT:
						turn(RIGHT)
						tempTurnStack.remove(tempTurnStack[len(tempTurnStack)-1])
					elif turn== RIGHT:
						turn=LEFT
						tempTurnStack.remove(tempTurnStack[len(tempTurnStack)-1])

			return True
		except IndexError:
			return False

	def lookback(self, riskFactor):
		##eita likhbo


	def infer(self):

		###eita most important


LEFT=int(0)
RIGHT=int(1)
position=[]
direction=KnowledgeBase.NORTH
breeze = False;
bump=False
died=False
stench = False;
scream = False;
haveGold   = False;
glimmer= False;

quiver=WumpusWorldGenerator.numWmpi
