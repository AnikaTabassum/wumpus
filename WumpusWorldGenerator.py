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
		print("wumpus world ",wumpusWorld)
		return wumpusWorld

	def setStartLocation(self, wumpusWorld):
		#startingPosition=[0,0]
		self.startingPosition=self.getRandomEmptyLocation(wumpusWorld)
		print("sp ",self.startingPosition)

	def getRandomEmptyLocation(self, wumpusWorld):
		found=False
		while not found:
			randX=random.randrange(size+2)
			randY=random.randrange(size+2)

			if wumpusWorld[randX][randY]==0:
				empty=[randX, randY]
				return empty
		print("khub koshto ")
		return null
	def placeGold(self,wumpusWorld):
		goldposition=self.getRandomEmptyLocation(wumpusWorld)
		wumpusWorld[goldposition[0]][goldposition[1]]=4

	def populateWorld(self, wumpusWorld, wumpusProb, pitProb,obstacleProb):
		
		for i in range(len(wumpusWorld)):
			for j in range(len(wumpusWorld)):
				if i==0 or j==0 or i==len(wumpusWorld)-1 or j== len(wumpusWorld)-1:
					wumpusWorld[i][j]=3
					pass
				rand=random.random()
				if rand<=wumpusProb:
					wumpusWorld[i][j]=1
					self.numWmpi+=1
					pass
				rand=random.random()
				if rand<=pitProb:
					wumpusWorld[i][j]=2
					
					pass

				rand=random.random()
				if rand<=obstacleProb:
					wumpusWorld[i][j]=3
					
					pass
				




size=10 
wumpusProb=0.05 
pitProb=0.05 
obstacleProb=0.05
if __name__ == '__main__':
    WumpusWorldGenerator()
    #print(WumpusWorldGenerator.numWmpi)
#WumpusWorldGenerator().generateWorld(size,wumpusProb,pitProb,obstacleProb)