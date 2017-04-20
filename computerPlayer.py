from get_best_move import get_best_move

class ComputerPlayer(object):

	def __init__(self, marker):
		self.marker = marker

	def get_move(self, UI, board, opponent):
		return get_best_move(board, self.marker, opponent.marker)