from board import Board
from get_best_move import get_best_move

def get_computer_move(b, com_marker, hum_marker):
    available_positions = b.get_available_positions()
    if 4 in available_positions:
        return 4
    else:
        return get_best_move(b, com_marker, hum_marker)
