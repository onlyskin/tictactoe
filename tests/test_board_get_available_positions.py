import pytest

from board import Board

def test_it_returns_0_1_2_3_4_5_6_7_8():
    b = Board()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert b.get_available_positions() == expected

def test_it_returns_1_2_3_4_5_6_7_8():
    _input = ['X', None, None, None, None, None, None, None, None]
    b = Board(_input)
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert b.get_available_positions() == expected

def test_it_returns_0_1_2_4_5_6_7_8():
    _input = [None, None, None, 'X', None, None, None, None, None]
    b = Board(_input)
    expected = [0, 1, 2, 4, 5, 6, 7, 8]
    assert b.get_available_positions() == expected

def test_it_returns_1_2_3_4_5_6_7_8():
    _input = [None, None, None, 'X', None, None, None, 'O', None]
    b = Board(_input)
    expected = [0, 1, 2, 4, 5, 6, 8]
    assert b.get_available_positions() == expected
