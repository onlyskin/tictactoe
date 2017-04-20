class HumanPlayer(object):

	def __init__(self, marker):
		self.marker = marker

	def get_move(self, UI, board, opponent):
	    move = None
	    available_positions = board.get_available_positions()
	    while move is None:
	        move = UI.get_input_integer()
	        if move in available_positions:
	        	return move
	        else:
	            move = None