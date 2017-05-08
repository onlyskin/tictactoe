import pytest

from board import Board

def test_it_returns_X_at_0():
    _input = ['X', None, None, None, None, None, None, None, None]
    b = Board(_input)
    assert b[0] == 'X'

def test_it_returns_O_at_1():
    _input = [None, 'O', None, None, None, None, None, None, None]
    b = Board(_input)
    assert b[1] == 'O'

def test_it_returns_O_at_2():
    _input = [None, None, 'O', None, None, None, None, None, None]
    b = Board(_input)
    assert b[2] == 'O'

def test_it_returns_X_at_3():
    _input = [None, None, None, 'X', None, None, None, None, None]
    b = Board(_input)
    assert b[3] == 'X'

def test_it_returns_X_at_6():
    _input = [None, None, None, None, None, None, 'X', None, None]
    b = Board(_input)
    assert b[6] == 'X'

def test_it_returns_None_at_8():
    _input = [None, None, None, None, None, None, 'X', None, None]
    b = Board(_input)
    assert b[8] == None
