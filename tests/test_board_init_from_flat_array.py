import pytest

from board import Board

def test_board_cells_all_numbers():
	_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	expected = [[None, None, None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_0():
	_input = ['O', '1', '2', '3', '4', '5', '6', '7', '8']
	expected = [['O', None, None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_X_in_0():
	_input = ['X', '1', '2', '3', '4', '5', '6', '7', '8']
	expected = [['X', None, None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_1():
	_input = ['0', 'O', '2', '3', '4', '5', '6', '7', '8']
	expected = [[None, 'O', None],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_2():
	_input = ['0', '1', 'O', '3', '4', '5', '6', '7', '8']
	expected = [[None, None, 'O'],
				[None, None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_3():
	_input = ['0', '1', '2', 'O', '4', '5', '6', '7', '8']
	expected = [[None, None, None],
				['O', None, None],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_X_in_5():
	_input = ['0', '1', '2', '3', '4', 'X', '6', '7', '8']
	expected = [[None, None, None],
				[None, None, 'X'],
				[None, None, None]]
	b = Board(_input)
	assert b.board_cells == expected

def test_board_cells_O_in_8():
	_input = ['0', '1', '2', '3', '4', '5', '6', '7', 'O']
	expected = [[None, None, None],
				[None, None, None],
				[None, None, 'O']]
	b = Board(_input)
	assert b.board_cells == expected

