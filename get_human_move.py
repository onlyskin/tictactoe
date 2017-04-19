def get_human_move(board):
    move = None
    available_positions = board.get_available_positions()
    while move is None:
        move = int(raw_input())
        if move in available_positions:
        	return move
        else:
            move = None