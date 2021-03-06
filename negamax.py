winning_score = 10
losing_score = -10

class Node(object):
    def __init__(self, move=None, score=None):
        self.move = move
        self.score = score

def _get_score(board):
    if not board.game_is_over():
        raise ValueError
    if board.is_tie():
        return 0
    if board.is_winner():
        if board.get_winner() == board.get_current_player_marker():
            return winning_score
        else:
            return losing_score

def negamax(board):
    if board.game_is_over():
        score = _get_score(board)
        return Node(score=score)

    best_score = -1000000
    best_position = None
    for position in board.get_available_positions():
        new_board = board.move(position)
        x = negamax(new_board)
        x.score = -x.score
        if x.score > best_score:
            best_score = x.score
            best_position = position
        # if we have find a winning position, return immediately
        if best_score == winning_score:
            break

    return Node(move=best_position, score=best_score)
