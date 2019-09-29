import sys
import pygame
class KnowledgeBase():
	def __init__(self,screen,rectangleHeight,rectangleWidth):
		print("i am Knowledgebase init")
		self.NORTH=[0,1]
		self.SOUTH=[0,-1]
		self.EAST=[1,0]
		self.WEST=[-1,0]
		self.CLEAR=-1
		self.DIRECTIONS=[self.NORTH,self.SOUTH,self.EAST,self.WEST]
		self.moveStack=[]
		self.turnStack=[]
		self.colDimension=10
		self.rowDimension=10
		self.wumpusMap= [[0 for x in range(self.colDimension)] for y in range(self.rowDimension)] 
		self.pitMap= [[0 for x in range(self.colDimension)] for y in range(self.rowDimension)] 
		self.obstacleMap= [[0 for x in range(self.colDimension)] for y in range(self.rowDimension)] 
		self.pathMap= [[0 for x in range(self.colDimension)] for y in range(self.rowDimension)] 
		self.glimmer=[0 for x in range(2)] 
		self.steps=int(0)

		self.stench = pygame.image.load(r'/home/anika/Downloads/stench.jpg')
		self.breeze = pygame.image.load(r'/home/anika/Downloads/breeze.png')
		self.wumpus = pygame.image.load(r'/home/anika/Downloads/wumpus.png')
		self.gold = pygame.image.load(r'/home/anika/Downloads/gold.png')
		self.pit = pygame.image.load(r'/home/anika/Downloads/pit.jpg')
		self.agent=pygame.image.load(r'/home/anika/Downloads/agent.png')
		self.screen=screen
		self.rectangleHeight=rectangleHeight
		self.rectangleWidth=rectangleWidth
		#self.calling()
	def calling(self):
		#print("Calling babyy ")
		#self.registerMove(0,0)
		self.tellBump(0,0, self.NORTH)
		self.registerMove(1,0)
		self.tellClear(1,0)
		self.registerMove(2,0)
		self.tellStench(2,0)
		self.tellGlimmer(5,5)
		self.printing()

	
	def perceive(self, x,y, map, val):

		for d in self.DIRECTIONS:
			#print("perceive ",d)
			#map[x][y]=-val
			if(x+d[0]>=0 and x+d[0]<len(map) and y+d[1]>=0 and y+d[1]<len(map)):
				#print("Working?????????????????????????????????")
				map[x+d[0]][y+d[1]]=self.CLEAR


	def registerMove(self,x,y):
		#print("i am Knowledgebase ",x,",",y)
		if self.pathMap[x][y]==0:
			move=[x,y]
			self.moveStack.append(move)
		print("reg ",self.moveStack[len(self.moveStack)-1])
		self.wumpusMap[x][y]=self.CLEAR
		self.pitMap[x][y]=self.CLEAR
		self.obstacleMap[x][y]=self.CLEAR
		self.pathMap[x][y]+=1

	def registerTurn(self,dirs):
		if dirs==0 or dirs==1:
			#print("direction in kb ", dirs)
			self.turnStack.append(dirs)
		else:
			print("Invalid direction passed to registerTurn")

	def tellClear(self,x,y):
		for d in self.DIRECTIONS:
			#print("aggggggggg ",d)
			if(x+d[0]>=0 and x+d[0]<len(self.pathMap) and y+d[1]>=0 and y+d[1]<len(self.pathMap)):
				self.wumpusMap[x+d[0]][y+d[1]]=self.CLEAR
				self.pitMap[x+d[0]][y+d[1]]=self.CLEAR
				#print("if er vetor")
	def returnMoveStack(self):
		#print("########################################################################################################")
		#print("lalalalqlalalaalalalaalalalala ",(self.moveStack))
		return self.moveStack

	def returnTurnStack(self):
		#print("*********************************************************************")
		#print("qeqqeqeqeqeqeqeqeqeqeqeqeqeqqeeeqq",(self.turnStack))
		return self.turnStack
	def askPath(self,x,y):
		try:
			#print("askPath ",x,",",y,",",self.pathMap[x][y])
			return self.pathMap[x][y]
		except IndexError as e:
			#print(e)
			return 100
		################################3out of bound ta dite hobe########

	def tellStench(self,x,y):
		#print("tellstench")
		if self.pathMap[x][y]<=1:
			self.perceive(x,y,self.wumpusMap, 2)

	def askWumpus(self, x,y):
		try:
			print("askWumpus ","x: ",x,"y: ",y,self.wumpusMap[x][y])
			return self.wumpusMap[x][y]
		except IndexError:
			return 100
		################################3out of bound ta dite hobe########

	def tellBreeze(self,x,y):
		if self.pathMap[x][y]<=1:
			self.perceive(x,y,self.pitMap,2)
			print("+++++++++++++++++++++++++++++++++++++++++tellbreeze ",x,",",y, "ddhqiued", self.pitMap[x][y])

	def askPit(self,x,y):
		try:
			print("askpit ","x: ",x,"y: ",y,self.pitMap[x][y])
			return self.pitMap[x][y]
		except IndexError:
			return 100
	def tellBump(self, x,y, direction):
		#print("tell bump", x,", ",y)
		try:

			self.obstacleMap[x+direction[0]][y+direction[1]]+=1
		except IndexError:
			return
	def askObstacle(self,x,y):
		try:
			if self.obstacleMap[x][y]>0:
				return 100
			else:
				return 0
		except:
			return 100

	def tellGlimmer(self, x,y):
		print("tellGlimmer", x,',',y)
		self.glimmer[0]=x
		self.glimmer[1]=y
	def askGlimmer(self,x,y):
		#print("Why am i even here?", self.glimmer[0])
		if self.glimmer[0]==x and self.glimmer[1]==y:
			return True

		else:
			return False


	def tellScream(self, x,y, direction):
		while x<len(self.wumpusMap) and y<len(self.wumpusMap):
			if self.obstacleMap[x][y]>0:
				self.wumpusMap[x][y]=self.CLEAR
				return
			else:
				self.wumpusMap[x][y]=self.CLEAR
				x+=direction[0]
				y+=direction[1]
	def printing(self):
		
		x=int(0)
		#print(int(len(self.pathMap)))
		y=int(10)
		while y>=0:
			y-=1
			############3ami eikhane ektu genjam korsi... last the e asha uchit chilo#########
			tempStr=""

			if x==0:
				tempStr+=str(y)+"|"
			for x in range(10):
				lastX=self.moveStack[len(self.moveStack)-1][0]
				lastY=self.moveStack[len(self.moveStack)-1][1]
				if lastX==x and lastY==y:
					#print(x,",",y)
					tempStr+="o "
					self.screen.blit(self.agent, (y*self.rectangleWidth, x*self.rectangleHeight+self.rectangleHeight)) 
					pygame.display.update()
					pygame.time.wait(1000)
				elif self.pathMap[x][y]>0:
					tempStr+="+ "
				elif self.obstacleMap[x][y]>0:
					#print(x,",",y)
					tempStr+="# "
				elif self.wumpusMap[x][y]<0 and self.pitMap[x][y]<0:
					tempStr+="  "
				elif self.wumpusMap[x][y]==0 and self.pitMap[x][y]==0:
					tempStr+="? "
				elif self.wumpusMap[x][y]>= self.pitMap[x][y]:
					tempStr+="w "
					self.screen.blit(self.stench, (x*self.rectangleWidth, y*self.rectangleHeight+self.rectangleHeight)) 
					pygame.display.update()
					pygame.time.wait(1000)
				elif self.pitMap[x][y]>0:
					tempStr+="p "
				else:
					tempStr+="! "
			x=0
			print(tempStr)
		print(" ")
		tete=""
		for i in range (len(self.pathMap)-1):
			tete+="--"
		print(tete)
		amiami=""
		for i in range (len(self.pathMap)-1):
			amiami+=" "+str(i)
		print(amiami)
		
					
					

#lastX=moveStack[len(moveStack)-1][0]
#print("pathMap ", len(moveStack)-1)
#Knowledgebase().calling()

if __name__ == "__main__":
	kn=KnowledgeBase()
	