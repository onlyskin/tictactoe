class Console_UI(object):

	@staticmethod
	def output_string(string):
		print string

	@staticmethod
	def output_board(board):
		print board

	@staticmethod
	def get_input_integer():
		return int(raw_input())
