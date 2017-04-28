from board import Board
from consoleUi import ConsoleUi
from humanPlayer import HumanPlayer
from computerPlayer import ComputerPlayer

class Game:
    def __init__(self, UI, player1, player2):
        self.board = Board()
        self.UI = UI
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        # start by outputting the board
        self.UI.output_start_game_message(self.board)
        # loop through until the game was won or tied
        active_player = self.player1
        opponent = self.player2
        while not self.game_has_winner() and not self.is_tie():
            self.UI.output_start_turn_message(active_player)
            move = active_player.get_move(self.UI, self.board, opponent)
            self.board = self.board.move(move, active_player.marker)
            self.UI.output_moved_message(active_player, move, self.board)
            active_player, opponent = opponent, active_player

        self.UI.output_end_message()

    def game_has_winner(self):
        return self.board.is_winner()

    def is_tie(self):
        return self.board.is_full()


class GameMaker(object):
    def __init__(self, UI):
        self.UI = UI

    def make_game(self):
        self.UI.output_init_message()
        player1, player2 = self.UI.get_players()
        game = Game(self.UI, player1, player2)
        return game

if __name__ == '__main__':
    consoleGameMaker = GameMaker(ConsoleUi())
    game = consoleGameMaker.make_game()
    game.start_game()
