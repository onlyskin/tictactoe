from human_player import HumanPlayer
from computer_player import ComputerPlayer

class ConsoleUi(object):

	def output_init_message(self):
		print 'Welcome to Tic Tac Toe!'

	def output_play_instructions(self):
		print 'To play in a cell, enter [0-8]:\n'

	def output_start_game_message(self, board):
		print
		print 'Initial board:'
		self.output_board(board)
		self.output_play_instructions()

	def output_start_turn_message(self, player):
		print "Player {}'s turn:".format(player.marker)

	def output_moved_message(self, player, move, board):
		print 'Player {} moved in cell {}:'.format(player.marker, move)
		self.output_board(board)

	def output_move_not_available_message(self, move):
		print 'Cell {} is not available, please choose another move:'.format(move)

	def output_end_message(self, game):
		print 'Game over!'
		if game.is_tie():
			print 'The game was a draw.'
		else:
			print 'Player {} won.'.format(game.get_winner())

	def output_board(self, board):
		print board

	def get_input_integer(self):
		user_input = raw_input()
		try:
			user_input = int(user_input)
		except ValueError:
			print 'Please enter a number.'
			return self.get_input_integer()
		else:
			return user_input

	def get_players(self):
		player1 = self.get_player()
		player2 = self.get_player()
		try:
			assert player1.marker != player2.marker
		except AssertionError:
			print '\nYou must choose different symbols for each player.\nPlease try again:'
			return self.get_players()
		else:
			return [player1, player2]

	def get_player_type(self):
		print 'Choose player type [(h)uman or (c)omputer]:'
		type = raw_input()
		while type != 'h' and type != 'c':
			return self.get_player_type()
		return type

	def get_player_marker(self):
		print 'Choose a symbol to represent this player:'
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

	def get_players_in_order(self, player1, player2):
		print 'Who should start, {} or {}?'.format(player1.marker, player2.marker)
		choice = raw_input()
		try:
			assert choice in map(lambda x: x.marker, [player1, player2])
		except AssertionError:
			return self.get_players_in_order(player1, player2)
		else:
			if choice == player1.marker:
				return [player1, player2]
			else:
				return [player2, player1]

