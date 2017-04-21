import pytest

from board import Board

def test_it_sets_0_to_x():
	_input = [None, None, None, None, None, None, None, None, None]
	b = Board(_input)
	b[0] = 'X'
	assert b[0] == 'X'
