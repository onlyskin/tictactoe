import pytest

from board import Board

def test_it_returns_false_when_empty():
    b = Board()
    assert not b.is_tie()

def test_it_returns_true_when_full_tied():
    b = Board(['O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X'])
    assert b.is_tie()

def test_it_returns_false_when_full_with_winner():
    b = Board(['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X'])
    assert not b.is_tie()

