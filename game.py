from board import Board
from get_best_move import get_best_move
from console_UI import Console_UI
from humanPlayer import HumanPlayer

class Game:
    def __init__(self, UI, player1):
        self.board = Board(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        self.com = "X" # the computer's marker
        self.hum = "O" # the user's marker
        self.UI = UI
        self.player1 = player1

    def start_game(self):
        # start by outputting the board
        self.UI.output_board(self.board)
        self.UI.output_string("Enter [0-8]:")
        # loop through until the game was won or tied
        while not self.game_has_winner() and not self.is_tie():
            human_move = self.player1.get_move(self.board, self.UI)
            self.board = self.board.move(human_move, self.player1.marker)
            if not self.game_has_winner() and not self.is_tie():
                computer_move = get_best_move(self.board, self.com, self.hum)
                self.board = self.board.move(computer_move, self.com)

            self.UI.output_board(self.board)

        self.UI.output_string("Game over")

    def game_has_winner(self):
        return self.board.is_winner()

    def is_tie(self):
        return self.board.is_full()

if __name__ == '__main__':
    player1 = HumanPlayer("O")
    game = Game(Console_UI, player1)
    game.start_game()
