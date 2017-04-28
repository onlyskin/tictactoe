import pytest

from minimax import get_score
from board import Board

def test_it_raises_value_error_on_unfinished_board_no_winner():
	b = Board(['X', 'X', 'O', 'O', 'X', 'O', None, None, None])
	with pytest.raises(ValueError):
		get_score(b, 'X')

def test_it_returns_0_when_draw():
	b = Board(['O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'X'])
	assert get_score(b, 'X') == 0

def test_it_returns_10_on_unfinished_board_active_winner():
	b = Board(['X', 'X', 'X', 'O', 'O', None, None, None, None])
	assert get_score(b, 'X') == 10

def test_it_returns_10_on_finished_board_active_winner():
	b = Board(['X', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'])
	assert get_score(b, 'O') == 10

def test_it_returns_10_on_unfinished_board_opponent_winner():
	b = Board(['X', 'X', 'X', 'O', 'O', None, None, None, None])
	assert get_score(b, 'O') == -10

def test_it_returns_minus_10_on_finished_board_opponent_winner():
	b = Board(['X', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'])
	assert get_score(b, 'X') == -10
