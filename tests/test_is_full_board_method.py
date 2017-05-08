import pytest

from board import Board

def test_it_returns_false_when_empty():
    b = Board()
    assert not b.is_full()

def test_it_returns_true_when_full():
    _input = ['O', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O']
    b = Board(_input)
    assert b.is_full()

def test_it_returns_false_when_partly_full():
    _input = ['O', None, 'O', 'O', 'X', 'O', 'O', 'X', 'O']
    b = Board(_input)
    assert not b.is_full()
