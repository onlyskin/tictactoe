import pytest

from board import Board

def test_it_returns_X_at_0():
	_input = ['X', '1', '2', '3', '4', '5', '6', '7', '8']
	b = Board(_input)
	assert b[0] == 'X'

def test_it_returns_O_at_1():
	_input = ['0', 'O', '2', '3', '4', '5', '6', '7', '8']
	b = Board(_input)
	assert b[1] == 'O'

def test_it_returns_O_at_2():
	_input = ['0', '1', 'O', '3', '4', '5', '6', '7', '8']
	b = Board(_input)
	assert b[2] == 'O'

def test_it_returns_X_at_3():
	_input = ['0', '1', '2', 'X', '4', '5', '6', '7', '8']
	b = Board(_input)
	assert b[3] == 'X'

def test_it_returns_X_at_6():
	_input = ['0', '1', '2', '3', '4', '5', 'X', '7', '8']
	b = Board(_input)
	assert b[6] == 'X'

def test_it_returns_None_at_8():
	_input = ['0', '1', '2', '3', '4', '5', 'X', '7', '8']
	b = Board(_input)
	assert b[8] == None
