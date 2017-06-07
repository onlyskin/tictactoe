from minimax import minimax

class ComputerPlayer(object):

    def __init__(self, marker):
        self.marker = marker

    def get_move(self, board):
        best_node = minimax(board)
        return best_node.move
