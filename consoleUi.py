from humanPlayer import HumanPlayer
from computerPlayer import ComputerPlayer

class ConsoleUi(object):

	def output_init_message(self):
		print "Welcome to Tic Tac Toe!"

	def output_play_instructions(self):
		print "To play in a cell, enter [0-8]:\n"

	def output_start_game_message(self, board):
		print
		print "Initial board:"
		self.output_board(board)
		self.output_play_instructions()

	def output_start_turn_message(self, player):
		print "Player {}'s turn:".format(player.marker)

	def output_moved_message(self, player, move, board):
		print "Player {} moved in cell {}:".format(player.marker, move)
		self.output_board(board)

	def output_end_message(self):
		print "Game over"

	def output_board(self, board):
		print board

	def get_input_integer(self):
		return int(raw_input())

	def get_players(self):
		player1 = self.get_player()
		player2 = self.get_player()
		return [player1, player2]

	def get_player_type(self):
		print "Choose player type [(h)uman or (c)omputer]:"
		type = raw_input()
		while type != 'h' and type != 'c':
			type = raw_input()
		return type

	def get_player_marker(self):
		print "Choose a symbol to represent this player:"
		marker = raw_input()
		while len(marker) != 1:
			marker = raw_input()
		return marker

	def get_player(self):
		type = self.get_player_type()
		marker = self.get_player_marker()
		if type == 'h':
			return HumanPlayer(marker)
		else:
			return ComputerPlayer(marker)
