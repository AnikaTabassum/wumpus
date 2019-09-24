from Game import Game
from Agent import Agent

class Driver:
	def run(self):
		agent=Agent()
		size=int(10)
		game=Game(agent,size,wumpusProb,pitProb,obsProb)
		try:
			agent.start(game)
		except Exception as e:
			raise e
wumpusProb=0.05
pitProb=0.05
obsProb=0.05
Driver().run()