from get_best_move import get_best_move

class ComputerPlayer(object):

	def __init__(self, marker):
		self.marker = marker

	def get_move(self, board, opposition_marker):
		return get_best_move(board, self.marker, opposition_marker)