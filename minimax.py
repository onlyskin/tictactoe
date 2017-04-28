class Node(object):
	def __init__(self, board=None, move=None, score=None):
		self.move = move
		self.score = score
		self.board = board

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

def minimax(node, active_player_marker, opponent_marker, depth=0):
	if depth <= 1:
		print 'active: ' + active_player_marker
		print 'opponent: ' + opponent_marker
	board = node.board

	if board.is_winner() or board.is_full():
		score = get_score(board, active_player_marker)
		if depth <= 1:
			print '\t' * depth + str(node.move) + ' scored ' + str(score)
		# print board
		return Node(score=score)

	next_nodes = []
	if depth == 0 or depth == 1:
		print '\t' * depth + 'CHOICES:' + ' '.join(map(lambda x: str(x), board.get_available_positions()))
	for position in board.get_available_positions():
		if depth % 2 == 0:
			new_board = board.move(position, active_player_marker)
		else:
			new_board = board.move(position, opponent_marker)
		next_nodes.append(Node(board=new_board, move=position))
	for node in next_nodes:
		if depth == 0 or depth == 1:
			print '\t' * depth + str(node.move)
		score = minimax(node, active_player_marker, opponent_marker, depth + 1)
		node.score = score.score

	if depth <= 1:
		print '\t' * depth + 'final array:'
		for node in next_nodes:
			print '\t' * depth + node.__str__()

	if depth % 2 == 0:
		best_node = max(next_nodes, key=maxkey)
		# print '\t' * depth + 'BEST:' + best_node.__str__()
		return best_node
	else:
		best_node = min(next_nodes, key=maxkey)
		# print '\t' * depth + 'BEST:' + best_node.__str__()
		return best_node

def minimax_on_board(board, active_player_marker, opponent_marker):
	root = Node(board=board)
	return minimax(root, active_player_marker, opponent_marker, depth=0)
