from negamax import negamax

class ComputerPlayer(object):

    def __init__(self, marker):
        self.marker = marker

    def get_move(self, board):
        best_node = negamax(board)
        return best_node.move
