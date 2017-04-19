from board import Board
from get_human_move import get_human_move
from get_best_move import get_best_move

class Game:
    def __init__(self):
        self.board = Board(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        self.com = "X" # the computer's marker
        self.hum = "O" # the user's marker

    def start_game(self):
        # start by printing the board
        print self.board
        print "Enter [0-8]:"
        # loop through until the game was won or tied
        while not self.game_has_winner() and not self.is_tie():
            human_move = get_human_move(self.board)
            self.board = self.board.move(human_move, self.hum)
            if not self.game_has_winner() and not self.is_tie():
                computer_move = get_best_move(self.board, self.com, self.hum)
                self.board = self.board.move(computer_move, self.com)

            print self.board

        print "Game over"

    def game_has_winner(self):
        return self.board.is_winner()

    def is_tie(self):
        return self.board.is_full()

if __name__ == '__main__':
    game = Game()
    game.start_game()
