def get_human_move(board, UI):
    move = None
    available_positions = board.get_available_positions()
    while move is None:
        move = UI.get_input_integer()
        if move in available_positions:
        	return move
        else:
            move = None