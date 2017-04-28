class Node(object):
	def __init__(self, move=None, score=None):
		self.move = move
		self.score = score

	def __str__(self):
		return 'move: ' + str(self.move) + ', score: ' + str(self.score)

def maxkey(o):
	return o.score

def get_score(board, active_player_marker):
	if not board.is_full() and not board.is_winner():
		raise ValueError
	if board.is_full() and not board.is_winner():
		return 0
	if board.is_winner():
		if board.get_winner() == active_player_marker:
			return 10
		else:
			return -10

def minimax(board, active_player_marker, opponent_marker, depth=0):

	if board.is_winner() or board.is_full():
		score = get_score(board, active_player_marker)
		return Node(score=score)

	next_nodes = []
	for position in board.get_available_positions():
		if depth % 2 == 0:
			new_board = board.move(position, active_player_marker)
		else:
			new_board = board.move(position, opponent_marker)
		best_node = minimax(new_board, active_player_marker, opponent_marker, depth + 1)
		node = Node(move=position, score=best_node.score)
		next_nodes.append(node)

	if depth % 2 == 0:
		best_node = max(next_nodes, key=maxkey)
		return best_node
	else:
		best_node = min(next_nodes, key=maxkey)
		return best_node
