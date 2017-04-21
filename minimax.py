def get_next_boards(board, active_player_marker):
	if board.is_full():
		raise ValueError
	available_positions = board.get_available_positions()
	next_boards = []
	for position in available_positions:
		new_board = board.move(position, active_player_marker)
		next_boards.append(new_board)
	return next_boards

def minimax(board, active_player_marker, opponent_marker):
	return
