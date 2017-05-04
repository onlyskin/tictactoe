class HumanPlayer(object):

	def __init__(self, marker):
		self.marker = marker

	def get_move(self, ui, board, opponent):
		move = None
		available_positions = board.get_available_positions()
		while move is None:
			move = ui.get_input_integer()
			if move in available_positions:
				return move
			else:
				ui.output_move_not_available_message(move)
				move = None