import pytest

from board import Board

def test_it_returns_false_when_no_winner():
	b = Board([None, None, None, None, None, None, None, None, None])
	assert not b.get_winner()

def test_it_returns_X_when_left_column_all_X():
	b = Board(['X', None, None, 'X', None, None, 'X', None, None])
	assert b.get_winner() == 'X'

def test_it_returns_X_when_middle_column_all_X():
	b = Board([None, 'X', None, None, 'X', None, None, 'X', None])
	assert b.get_winner() == 'X'

def test_it_returns_X_when_right_column_all_X():
	b = Board([None, None, 'X', None, None, 'X', None, None, 'X'])
	assert b.get_winner() == 'X'

def test_it_returns_O_when_left_column_all_O():
	b = Board(['O', None, None, 'O', None, None, 'O', None, None])
	assert b.get_winner() == 'O'

def test_it_returns_true_when_top_row_all_O():
	b = Board(['O', 'O', 'O', None, None, None, None, None, None])
	assert b.get_winner() == 'O'

def test_it_returns_true_when_second_row_all_O():
	b = Board([None, None, None, 'O', 'O', 'O', None, None, None])
	assert b.get_winner() == 'O'

def test_it_returns_true_when_bottom_row_all_O():
	b = Board([None, None, None, None, None, None, 'O', 'O', 'O'])
	assert b.get_winner() == 'O'

def test_it_returns_true_when_diagonal_1_is_X():
	b = Board(['X', None, None, None, 'X', None, None, None, 'X'])
	assert b.get_winner() == 'X'

def test_it_returns_true_when_diagonal_2_is_O():
	b = Board([None, None, 'O', None, 'O', None, 'O', None, None])
	assert b.get_winner() == 'O'


