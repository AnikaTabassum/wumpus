class Knowledgebase:

	def calling(self):
		self.registerMove(0,0)
		self.tellBump(0,0, NORTH)
		self.registerMove(1,0)
		self.tellClear(1,0)
		self.registerMove(2,0)
		self.tellStench(2,0)
		self.printing()

	def perceive(self, x,y, map):

		for d in DIRECTIONS:
			print(d)
			if(x+d[0]>=0 and x+d[0]<len(map) and y+d[1]>=0 and y+d[1]<len(map)):
				map[x+d[0]][y+d[1]]=CLEAR

	def registerMove(self,x,y):
		move=[x,y]
		moveStack.append(move)
		wumpusMap[x][y]=CLEAR
		pitMap[x][y]=CLEAR
		obstacleMap[x][y]=CLEAR
		pathMap[x][y]+=1

	def registerTurn(self,dir):
		if dir==0 or dir==1:
			turnStack.append(dir)
		else:
			print("Invalid direction passed to registerTurn")

	def tellClear(self,x,y):
		for d in DIRECTIONS:
			print(d)
			if(x+d[0]>=0 and x+d[0]<len(pathMap) and y+d[1]>=0 and y+d[1]<len(pathMap)):
				wumpusMap[x+d[0]][y+d[1]]=CLEAR
				pitMap[x+d[0]][y+d[1]]=CLEAR

	def askPath(self,x,y):
		try:
			return pathMap[x][y]
		except IndexError:
			return 100
		################################3out of bound ta dite hobe########

	def tellStench(self,x,y):
		if pathMap[x][y]<=1:
			self.perceive(x,y,wumpusMap)

	def askWumpus(self, x,y):
		try:
			return wumpusMap[x][y]
		except IndexError:
			return 100
		################################3out of bound ta dite hobe########

	def tellBreeze(self,x,y):
		if pathMap[x][y]<=1:
			self.perceive(x,y,pitMap)

	def askPit(self,x,y):
		try:
			return pitMap[x][y]
		except IndexError:
			return 100
	def tellBump(self, x,y, direction):
		print("tell bump", x,", ",y)
		try:
			obstacleMap[x+direction[0]][y+direction[1]]+=1
		except IndexError:
			return
	def askObstacle(self,x,y):
		try:
			if obstacleMap[x][y]>0:
				return 100
			else:
				return 0
		except:
			return 100

	def tellGlimmer(self, x,y):
		glimmer[0]=x
		glimmer[1]=y
	def askGlimmer(self,x,y):
		if glimmer[0]==x and glimmer[1]==y:
			return True
		else:
			return False

	def tellScream(self, x,y, direction):
		while x<len(wumpusMap) and y<len(wumpusMap):
			if obstacleMap[x][y]>0:
				wumpusMap[x][y]=CLEAR
				return
			else:
				wumpusMap[x][y]=CLEAR
				x+=direction[0]
				y+=direction[1]
	def printing(self):
		
		x=int(0)
		print(int(len(pathMap)))
		for y in range(12):

			############3ami eikhane ektu genjam korsi... last the e asha uchit chilo#########
			tempStr=""

			if x==0:
				tempStr+=str(y)+"|"
			for x in range(12):
				lastX=moveStack[len(moveStack)-1][0]
				lastY=moveStack[len(moveStack)-1][1]
				if lastX==x and lastY==y:
					print(x,",",y)
					tempStr+="o "
				elif pathMap[x][y]>0:
					tempStr+="+ "
				elif obstacleMap[x][y]>0:
					print(x,",",y)
					tempStr+="# "
				elif wumpusMap[x][y]<0 and pitMap[x][y]<0:
					tempStr+="  "
				elif wumpusMap[x][y]==0 and pitMap[x][y]==0:
					tempStr+="? "
				elif wumpusMap[x][y]>= pitMap[x][y]:
					tempStr+="w "
				elif pitMap[x][y]>0:
					tempStr+="p "
				else:
					tempStr+="! "
			x=0
			print(tempStr)
		print(" ")
		tete=""
		for i in range (len(pathMap)-1):
			tete+="--"
		print(tete)
		amiami=""
		for i in range (len(pathMap)-1):
			amiami+=" "+str(i)
		print(amiami)
		
					
					
				
NORTH=[0,1]
SOUTH=[0,-1]
EAST=[1,0]
WEST=[-1,0]
CLEAR=-1
DIRECTIONS=[NORTH,SOUTH,EAST,WEST]
moveStack=[]
turnStack=[]
colDimension=10
rowDimension=10
wumpusMap= [[0 for x in range(colDimension+2)] for y in range(rowDimension+2)] 
pitMap= [[0 for x in range(colDimension+2)] for y in range(rowDimension+2)] 
obstacleMap= [[0 for x in range(colDimension+2)] for y in range(rowDimension+2)] 
pathMap= [[0 for x in range(colDimension+2)] for y in range(rowDimension+2)] 
glimmer=[]
steps=int(0)
x = range(9, 6)

for n in x:
  	print(n)
#lastX=moveStack[len(moveStack)-1][0]
#print("pathMap ", len(moveStack)-1)
Knowledgebase().calling()
	