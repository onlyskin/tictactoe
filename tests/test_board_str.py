import pytest

from board import Board

def test_it_returns_string_when_all_empty():
	_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_0_X():
	_input = ['X', '1', '2', '3', '4', '5', '6', '7', '8']
	_output = ' X | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_1_X():
	_input = ['0', 'X', '2', '3', '4', '5', '6', '7', '8']
	_output = ' 0 | X | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_2_X():
	_input = ['0', '1', 'X', '3', '4', '5', '6', '7', '8']
	_output = ' 0 | 1 | X \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_3_O():
	_input = ['0', '1', '2', 'O', '4', '5', '6', '7', '8']
	_output = ' 0 | 1 | 2 \n===+===+===\n O | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_8_O():
	_input = ['0', '1', '2', '3', '4', '5', '6', '7', 'O']
	_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | O \n'
	b = Board(_input)
	assert b.__str__() == _output

def test_it_returns_string_when_1_X_5_O():
	_input = ['0', 'X', '2', '3', '4', 'O', '6', '7', '8']
	_output = ' 0 | X | 2 \n===+===+===\n 3 | 4 | O \n===+===+===\n 6 | 7 | 8 \n'
	b = Board(_input)
	assert b.__str__() == _output

