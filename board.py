class Board(object):

	def __init__(self, flat_board_array):
		self.board_cells = [[None, None, None],
							[None, None, None],
							[None, None, None]]
		for i, row in enumerate(self.board_cells):
			for j, cell in enumerate(row):
				flat_cell = flat_board_array[3 * i + j]
				if flat_cell == 'O' or flat_cell == 'X':
					self.board_cells[i][j] = flat_cell

	def is_full(self):
		for row in self.board_cells:
			for cell in row:
				if cell == None:
					return False
		return True

	def is_winner(self):
		b = self.board_cells
		rows = b
		columns = zip(*b)
		diagonals = [[b[0][0], b[1][1], b[2][2]],
					 [b[0][2], b[1][1], b[2][0]]]
		win_paths = rows + columns + diagonals
		for path in win_paths:
			if path[0] == path[1] == path[2] != None:
				return True
		return False