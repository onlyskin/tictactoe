import pytest

from board import Board

def test_it_sets_0_to_x():
	b = Board()
	b[0] = 'X'
	assert b[0] == 'X'
