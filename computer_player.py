from minimax import minimax

class ComputerPlayer(object):

    def __init__(self, marker):
        self.marker = marker

    def get_move(self, ui, board, opponent):
        best_node = minimax(board, self.marker, opponent.marker)
        return best_node.move
