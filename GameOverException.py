class GameOverException():

	def __init__(self):
		self.win=""
	def exception(self, flag):
		self.win=flag
	def checkWin(self):
		return  self.win

if __name__ == "__main__":
	GameOverException()
