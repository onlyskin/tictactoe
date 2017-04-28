import pytest

from board import Board

def test_board_cells_all_numbers():
	_input = [None, None, None, None, None, None, None, None, None]
	expected = [[None, None, None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_0():
	_input = ['O', None, None, None, None, None, None, None, None]
	expected = [['O', None, None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_X_in_0():
	_input = ['X', None, None, None, None, None, None, None, None]
	expected = [['X', None, None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_1():
	_input = [None, 'O', None, None, None, None, None, None, None]
	expected = [[None, 'O', None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_2():
	_input = [None, None, 'O', None, None, None, None, None, None]
	expected = [[None, None, 'O'],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_3():
	_input = [None, None, None, 'O', None, None, None, None, None]
	expected = [[None, None, None],
				['O', None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_X_in_5():
	_input = [None, None, None, None, None, 'X', None, None, None]
	expected = [[None, None, None],
				[None, None, 'X'],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_8():
	_input = [None, None, None, None, None, None, None, None, 'O']
	expected = [[None, None, None],
				[None, None, None],
				[None, None, 'O']]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_can_init_from_no_argument():
	expected = [[None, None, None],
				[None, None, None],
				[None, None, None]]
	b = Board()
	assert b.board_cells == expected
