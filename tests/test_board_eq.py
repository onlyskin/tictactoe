import pytest

from board import Board

def test_it_returns_true():
	b1 = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', None, None])
	b2 = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', None, None])
	assert b1 == b2

def test_it_returns_false():
	b1 = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', None, None])
	b2 = Board(['X', 'O', 'X', 'O', 'O', 'X', 'X', None, 'X'])
	assert b1 != b2
