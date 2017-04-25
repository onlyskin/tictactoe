class Board(object):

	def __init__(self, flat_board_array=[None, None, None, None, None, None, None, None, None]):
		self.board_cells = [[None, None, None],
							[None, None, None],
							[None, None, None]]
		for i, row in enumerate(self.board_cells):
			for j, cell in enumerate(row):
				flat_cell = flat_board_array[3 * i + j]
				if flat_cell != None:
					self.board_cells[i][j] = flat_cell

	def __str__(self):
		flat = self.board_cells[0] + self.board_cells[1] + self.board_cells[2]
		mapped = [i if cell is None else cell for i, cell in enumerate(flat)]
		return ' %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n' % \
			tuple(mapped)

	def __getitem__(self, key):
		return self.board_cells[key / 3][key % 3]

	def __setitem__(self, key, value):
		self.board_cells[key / 3][key % 3] = value

	def __eq__(self, board2):
		return self.board_cells == board2.board_cells

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

	def get_winner(self):
		if not self.is_winner():
			raise ValueError
		b = self.board_cells
		rows = b
		columns = zip(*b)
		diagonals = [[b[0][0], b[1][1], b[2][2]],
					 [b[0][2], b[1][1], b[2][0]]]
		win_paths = rows + columns + diagonals
		for path in win_paths:
			if path[0] == path[1] == path[2] != None:
				return path[0]
		return False

	def move(self, position, marker):
		flat = self.board_cells[0] + self.board_cells[1] + self.board_cells[2]
		if flat[position] != None:
			raise IndexError
		new_board = Board(flat)
		new_board.board_cells[position / 3][position % 3] = marker
		return new_board

	def get_available_positions(self):
		result = []
		flat = self.board_cells[0] + self.board_cells[1] + self.board_cells[2]
		for i, cell in enumerate(flat):
			if cell == None:
				result.append(i)
		return result
