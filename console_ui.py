import sys

from human_player import HumanPlayer
from computer_player import ComputerPlayer

class ConsoleUi(object):
    def __init__(self, out_stream=sys.stdout, get_input=raw_input):
        self._out_stream = out_stream
        self._get_input = get_input

    def output_to_stream(self, content):
        self._out_stream.write(content)

    def output_init_message(self):
        self.output_to_stream('Welcome to Tic Tac Toe!\n')

    def output_play_instructions(self):
        self.output_to_stream('To play in a cell, enter [0-8]:\n\n')

    def output_start_game_message(self, board):
        self.output_to_stream('\nInitial board:\n')
        self.output_board(board)
        self.output_play_instructions()

    def output_start_turn_message(self, player):
        output = "Player {}'s turn:\n".format(player.marker)
        self.output_to_stream(output)

    def output_moved_message(self, player, move, board):
        output = 'Player {} moved in cell {}:\n'.format(player.marker, move)
        self.output_to_stream(output)
        self.output_board(board)

    def output_move_not_available_message(self, move):
        output = 'Cell {} is not available, please choose another move:\n'.format(move)
        self.output_to_stream(output)

    def output_end_message(self, game):
        self.output_to_stream('Game over!\n')
        if game.is_tie():
            self.output_to_stream('The game was a draw.\n')
        else:
            output = 'Player {} won.\n'.format(game.get_winner())
            self.output_to_stream(output)

    def output_board(self, board):
        cells = [board[i] for i in range(9)]
        mapped = [i if cell is None else cell for i, cell in enumerate(cells)]
        self.output_to_stream(' %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n\n' % \
            tuple(mapped))

    def get_input_integer(self):
        user_input = self._get_input()
        try:
            user_input = int(user_input)
        except ValueError:
            self.output_to_stream('Please enter a number.\n')
            return self.get_input_integer()
        else:
            return user_input

    def get_players(self):
        player1 = self.get_player()
        player2 = self.get_player()
        try:
            assert player1.marker != player2.marker
        except AssertionError:
            self.output_to_stream('\nYou must choose different symbols for each player.\nPlease try again:\n')
            return self.get_players()
        else:
            return [player1, player2]

    def get_player_type(self):
        self.output_to_stream('Choose player type [(h)uman or (c)omputer]:\n')
        type = self._get_input()
        while type != 'h' and type != 'c':
            return self.get_player_type()
        return type

    def get_player_marker(self):
        self.output_to_stream('Choose a symbol to represent this player:\n')
        marker = self._get_input()
        while len(marker) != 1:
            marker = self._get_input()
        return marker

    def get_player(self):
        type = self.get_player_type()
        marker = self.get_player_marker()
        if type == 'h':
            return HumanPlayer(marker, self)
        else:
            return ComputerPlayer(marker)

    def get_players_in_order(self, player1, player2):
        output = 'Who should start, {} or {}?\n'.format(player1.marker, player2.marker)
        self.output_to_stream(output)
        choice = self._get_input()
        try:
            assert choice in map(lambda x: x.marker, [player1, player2])
        except AssertionError:
            return self.get_players_in_order(player1, player2)
        else:
            if choice == player1.marker:
                return [player1, player2]
            else:
                return [player2, player1]

