import pytest

from board import Board

def test_it_returns_string_when_all_empty():
	_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board()
	assert b.__str__() == _output

def test_it_returns_string_when_0_X():
	_input = ['X', None, None, None, None, None, None, None, None]
	_output = ' X | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_1_X():
	_input = [None, 'X', None, None, None, None, None, None, None]
	_output = ' 0 | X | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_2_X():
	_input = [None, None, 'X', None, None, None, None, None, None]
	_output = ' 0 | 1 | X \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_3_O():
	_input = [None, None, None, 'O', None, None, None, None, None]
	_output = ' 0 | 1 | 2 \n===+===+===\n O | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_8_O():
	_input = [None, None, None, None, None, None, None, None, 'O']
	_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | O \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_1_X_5_O():
	_input = [None, 'X', None, None, None, 'O', None, None, None]
	_output = ' 0 | X | 2 \n===+===+===\n 3 | 4 | O \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

