class GameOverException():

	def __init__(self):
		self.win=False
	def exception(self, win):
		self.win=win

if __name__ == "__main__":
	GameOverException()
