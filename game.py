from board import Board
from get_human_move import get_human_move
from get_best_move import get_best_move

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
        while not self.game_has_winner() and not self.is_tie():
            b = Board(self.board)
            human_move = get_human_move(b)
            self.board[human_move] = self.hum
            if not self.game_has_winner() and not self.is_tie():
                b = Board(self.board)
                computer_move = get_best_move(b, self.com, self.hum)
                self.board[computer_move] = self.com

            b = Board(self.board)
            print b

        print "Game over"

    def game_has_winner(self):
        board = Board(self.board)
        return board.is_winner()

    def is_tie(self):
        board = Board(self.board)
        return board.is_full()

if __name__ == '__main__':
    game = Game()
    game.start_game()
