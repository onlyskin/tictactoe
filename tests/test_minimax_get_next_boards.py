import pytest

from minimax import get_next_boards
from board import Board

def test_it_returns_nine_boards_when_empty():
	b = Board()
	next_boards = get_next_boards(b, 'X')
	assert len(next_boards) == 9

def test_it_returns_correct_two_boards_when_two_spaces():
	b = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', None, None])
	b1 = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', None])
	b2 = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', None, 'O'])
	expected_next_boards = [b1, b2]
	next_boards = get_next_boards(b, 'O')
	# sort for the array equality test
	next_boards.sort()
	expected_next_boards.sort()
	assert next_boards == expected_next_boards

def test_it_raises_error_when_board_full():
	b = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O'])
	with pytest.raises(ValueError):
		get_next_boards(b, 'X')
