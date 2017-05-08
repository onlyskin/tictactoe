import pytest

from board import Board

def test_it_returns_flat_version_of_board():
    b = Board(['X', 'O', None, None, None, 'X', None, None, None])
    assert b.flatten() == ['X', 'O', None, None, None, 'X', None, None, None]
