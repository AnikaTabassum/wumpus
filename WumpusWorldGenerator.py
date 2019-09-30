import random
class WumpusWorldGenerator():
	def __init__(self):
		self.numWmpi=int(0)
		self.startingPosition=[]

	def calling():
		self.setStartLocation(wumpusWorld)

	def generateWorld(self, size, wumpusProb, pitProb, obstacleProb):
		wumpusWorld=[[0 for x in range(size+2)] for y in range(size+2)]
		self.populateWorld(wumpusWorld,wumpusProb,pitProb,obstacleProb)
		self.placeGold(wumpusWorld)
		self.setStartLocation(wumpusWorld)
		#print("wumpus world ",wumpusWorld)
		return wumpusWorld

	def generatePredefinedWorld(self,size,wumpusWorld,pitProb,obstacleProb):
		wumpusWorld=[[0 for x in range(size+2)] for y in range(size+2)]
		self.populateWorldManually(wumpusWorld)
		#print("manual ", wumpusWorld)
		return wumpusWorld

	def populateWorldManually(self,wumpusWorld):
		wumpusWorld[6][1]=2
		wumpusWorld[2][5]=1
		wumpusWorld[5][2]=2
		#wumpusWorld[4][9]=2
		wumpusWorld[8][3]=4
		#wumpusWorld[6][10]=2
		#wumpusWorld[7][6]=2
		#wumpusWorld[10][5]=2
		for i in range(len(wumpusWorld)):
			for j in range(len(wumpusWorld)):
				if i==0 or j==0 or i==len(wumpusWorld)-1 or j== len(wumpusWorld)-1:
					wumpusWorld[i][j]=3
					#print("jsdjsdjhs")

		self.startingPosition=[1,5]
	def setStartLocation(self, wumpusWorld):
		#startingPosition=[0,0]
		self.startingPosition=self.getRandomEmptyLocation(wumpusWorld)
		print("sp ",self.startingPosition)

	def getRandomEmptyLocation(self, wumpusWorld):
		found=False
		size=10
		while not found:
			randX=random.randrange(size)
			randY=random.randrange(size)

			if wumpusWorld[randX][randY]==0:
				empty=[randX, randY]
				return empty
		print("khub koshto ")
		return null
	def placeGold(self,wumpusWorld):
		goldposition=self.getRandomEmptyLocation(wumpusWorld)
		#print("gold position ",goldposition[0],",", goldposition[1])
		wumpusWorld[goldposition[0]][goldposition[1]]=4

	def populateWorld(self, wumpusWorld, wumpusProb, pitProb,obstacleProb):
		#print("populating ",len(wumpusWorld))
		cnt=int(0)
		for i in range(len(wumpusWorld)):
			for j in range(len(wumpusWorld)):
				if i==0 or j==0 or i==len(wumpusWorld)-1 or j== len(wumpusWorld)-1:
					wumpusWorld[i][j]=3
					#print("tetststs ","i ",i,"j ",j,wumpusWorld[i][j])
					continue
				rand=random.random()
				
				if rand<=wumpusProb and self.numWmpi<1:
					wumpusWorld[i][j]=1
					#print("wumpusWorld ",wumpusProb,"i: ",i,"j : ",j)
					self.numWmpi+=1 
					cnt+=1
					#print("cnt", cnt)
					continue
				rand2=random.random()
				if rand2<=pitProb:
					wumpusWorld[i][j]=2
					
					continue

				'''rand3=random.random()
				if rand3<=obstacleProb:
					wumpusWorld[i][j]=3
					
					continue'''
				



if __name__ == '__main__':
    WumpusWorldGenerator()
    #print(WumpusWorldGenerator.numWmpi)
#WumpusWorldGenerator().generateWorld(size,wumpusProb,pitProb,obstacleProb)