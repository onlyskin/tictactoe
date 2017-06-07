class Node(object):
    def __init__(self, move=None, score=None):
        self.move = move
        self.score = score

    def __str__(self):
        return 'move: ' + str(self.move) + ', score: ' + str(self.score)

def _maxkey(o):
    return o.score

def _get_score(board, active_player_marker):
    if not board.game_is_over():
        raise ValueError
    if board.is_tie():
        return 0
    if board.is_winner():
        if board.get_winner() == active_player_marker:
            return 10
        else:
            return -10

def minimax(board, active_player_marker, depth=0):

    if board.game_is_over():
        score = _get_score(board, active_player_marker)
        return Node(score=score)

    next_nodes = []
    for position in board.get_available_positions():
        new_board = board.move(position)
        best_node = minimax(new_board, active_player_marker, depth + 1)
        node = Node(move=position, score=best_node.score)
        next_nodes.append(node)

    if depth % 2 == 0:
        best_node = max(next_nodes, key=_maxkey)
        return best_node
    else:
        best_node = min(next_nodes, key=_maxkey)
        return best_node

