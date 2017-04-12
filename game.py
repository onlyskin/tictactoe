from board import Board

class Game:
    def __init__(self):
        self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.com = "X" # the computer's marker
        self.hum = "O" # the user's marker

    def start_game(self):
        # start by printing the board
        b = Board(self.board)
        print b
        print "Enter [0-8]:"
        # loop through until the game was won or tied
        while not self.game_has_winner(self.board) and not self.is_tie(self.board):
            self.get_human_spot()
            if not self.game_has_winner(self.board) and not self.is_tie(self.board):
                self.eval_board()

            b = Board(self.board)
            print b

        print "Game over"

    def get_human_spot(self):
        spot = None
        while spot is None:
            spot = int(raw_input())
            if self.board[spot] != "X" and self.board[spot] != "O":
                self.board[spot] = self.hum
            else:
                spot = None

    def eval_board(self):
        spot = None
        while spot is None:
            if self.board[4] == "4":
                spot = 4
                self.board[spot] = self.com
            else:
                spot = self.get_best_move(self.board, self.com)
                if self.board[spot] != "X" and self.board[spot] != "O":
                    self.board[spot] = self.com
                else:
                    spot = None

    def get_best_move(self, board, next_player, depth = 0, best_score = {}):
        available_spaces = [s for s in board if s != "X" and s != "O"]
        best_move = None

        for avail in available_spaces:
            board[int(avail)] = self.com
            if self.game_has_winner(board):
                best_move = int(avail)
                board[int(avail)] = avail
                return best_move
            else:
                board[int(avail)] = self.hum
                if self.game_has_winner(board):
                    best_move = int(avail)
                    board[int(avail)] = avail
                    return best_move
                else:
                    board[int(avail)] = avail

        if best_move:
            return best_move
        else:
            return int(available_spaces[0])

    def game_has_winner(self, b):
        board = Board(b)
        return board.is_winner()

    def is_tie(self, b):
        board = Board(b)
        return board.is_full()

if __name__ == '__main__':
    game = Game()
    game.start_game()
