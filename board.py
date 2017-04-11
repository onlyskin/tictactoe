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

