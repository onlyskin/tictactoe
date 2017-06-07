from minimax import minimax

class ComputerPlayer(object):

    def __init__(self, marker):
        self.marker = marker

    def get_move(self, board, opponent):
        best_node = minimax(board, self.marker)
        return best_node.move
