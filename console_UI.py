from humanPlayer import HumanPlayer
from computerPlayer import ComputerPlayer

class Console_UI(object):

	@staticmethod
	def output_init_message():
		print "Welcome to Tic Tac Toe!"

	@staticmethod
	def output_play_instructions():
		print "Enter [0-8]:"

	@staticmethod
	def output_start_game_message(board):
		print
		print "Initial board:"
		Console_UI.output_board(board)
		Console_UI.output_play_instructions()

	@staticmethod
	def output_start_turn_message(player):
		print '''Player "{}"'s turn:'''.format(player.marker)

	@staticmethod
	def output_moved_message(player, move, board):
		print '''Player "{}" moved in cell {}:'''.format(player.marker, move)
        Console_UI.output_board(board)

	@staticmethod
	def output_end_message():
		print "Game over"

	@staticmethod
	def output_board(board):
		print board

	@staticmethod
	def get_input_integer():
		return int(raw_input())

	@staticmethod
	def get_players():
		player1 = Console_UI.get_player()
		player2 = Console_UI.get_player()
		return [player1, player2]

	@staticmethod
	def get_player_type():
		print "Choose player type [(h)uman or (c)omputer]:"
		type = raw_input()
		while type != 'h' and type != 'c':
			type = raw_input()
		return type

	@staticmethod
	def get_player_marker():
		print "Choose a symbol to represent this player:"
		marker = raw_input()
		while len(marker) != 1:
			marker = raw_input()
		return marker

	@staticmethod
	def get_player():
		type = Console_UI.get_player_type()
		marker = Console_UI.get_player_marker()
		if type == 'h':
			return HumanPlayer(marker)
		else:
			return ComputerPlayer(marker)
