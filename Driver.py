from Game import Game
from GameOverException import GameOverException
from Agent import Agent

class Driver:
	def run(self):
		ge=GameOverException()
		agent=Agent()
		size=int(10)
		game=Game(agent,size,wumpusProb,pitProb,obsProb)
		try:
			agent.start(game)
		except:
			print(ge.win)
			if ge.checkWin():
				print("agent won the game")
			else:
				print("agent lost the game")
			print("Score: ",game.getScore())
wumpusProb=0.05
pitProb=0.05
obsProb=0.05
Driver().run()