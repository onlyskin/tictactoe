class HumanPlayer(object):

    def __init__(self, marker, ui):
        self.marker = marker
        self.ui = ui

    def get_move(self, board, opponent):
        available_positions = board.get_available_positions()
        while True:
            move = self.ui.get_input_integer()
            if move in available_positions:
                return move
            else:
                self.ui.output_move_not_available_message(move)
