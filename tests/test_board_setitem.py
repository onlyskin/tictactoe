import pytest

from board import Board

def test_it_sets_0_to_x():
	_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	b = Board(_input)
	b[0] = 'X'
	assert b[0] == 'X'
