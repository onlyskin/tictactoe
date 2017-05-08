from board import Board
from console_ui import ConsoleUi
from human_player import HumanPlayer
from computer_player import ComputerPlayer

class Game(object):
    def __init__(self, ui, player1, player2):
        self.board = Board()
        self.ui = ui
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        self.ui.output_start_game_message(self.board)
        active_player = self.player1
        opponent = self.player2
        while not self.game_is_over():
            self.ui.output_start_turn_message(active_player)
            move = active_player.get_move(self.ui, self.board, opponent)
            self.board = self.board.move(move, active_player.marker)
            self.ui.output_moved_message(active_player, move, self.board)
            active_player, opponent = opponent, active_player

        self.ui.output_end_message(self)

    def game_has_winner(self):
        return self.board.is_winner()

    def is_tie(self):
        return self.board.is_tie()

    def game_is_over(self):
        return self.board.game_is_over()

    def get_winner(self):
        return self.board.get_winner()

class GameMaker(object):
    def __init__(self, ui):
        self.ui = ui

    def make_game(self):
        self.ui.output_init_message()
        player1, player2 = self.ui.get_players()
        players = self.ui.get_players_in_order(player1, player2)
        game = Game(self.ui, *players)
        return game

if __name__ == '__main__':
    console_game_maker = GameMaker(ConsoleUi())
    game = console_game_maker.make_game()
    game.start_game()
