def get_best_move(board, com_marker, hum_marker):
    available_positions = board.get_available_positions()
    best_move = None

    for position in available_positions:
        moved_board = board.move(position, com_marker)
        if moved_board.is_winner():
            best_move = position
            return best_move
        else:
            moved_board = board.move(position, hum_marker)
            if moved_board.is_winner():
                best_move = position
                return best_move

    if best_move:
        return best_move
    else:
        return available_positions[0]
