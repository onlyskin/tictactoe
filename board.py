class Board(object):

    def __init__(self, board_cells=None):
        if board_cells == None:
            board_cells = [[None, None, None],
                            [None, None, None],
                            [None, None, None]]

        self.board_cells = [[None, None, None],
                            [None, None, None],
                            [None, None, None]]

        for i, row in enumerate(board_cells):
            for j, cell in enumerate(row):
                self.board_cells[i][j] = cell

    def __getitem__(self, key):
        return self.board_cells[key / 3][key % 3]

    def __setitem__(self, key, value):
        self.board_cells[key / 3][key % 3] = value

    def __eq__(self, board2):
        return self.board_cells == board2.board_cells

    def flatten(self):
        return self.board_cells[0] + self.board_cells[1] + self.board_cells[2]

    def is_full(self):
        for row in self.board_cells:
            for cell in row:
                if cell == None:
                    return False
        return True

    def is_winner(self):
        return bool(self.get_winner())

    def get_winner(self):
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

    def is_tie(self):
        return self.is_full() and not self.is_winner()

    def game_is_over(self):
        return self.is_winner() or self.is_tie()

    def move(self, position, marker):
        if position not in self.get_available_positions():
            raise IndexError
        new_board = Board(self.board_cells)
        new_board[position] = marker
        return new_board

    def get_available_positions(self):
        flat = self.flatten()
        available_cells = [i for i, cell in enumerate(flat) if cell == None]
        return available_cells
