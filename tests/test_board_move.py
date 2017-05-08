import pytest

from board import Board

def test_it_moves_X_in_0():
    b = Board()
    new_board = b.move(0, 'X')

    expected = [['X', None, None],
                [None, None, None],
                [None, None, None]]

    assert new_board.board_cells == expected

def test_it_moves_O_in_0():
    b = Board()
    new_board = b.move(0, 'O')

    expected = [['O', None, None],
                [None, None, None],
                [None, None, None]]

    assert new_board.board_cells == expected

def test_it_moves_X_in_1():
    b = Board()
    new_board = b.move(1, 'X')

    expected = [[None, 'X', None],
                [None, None, None],
                [None, None, None]]

    assert new_board.board_cells == expected

def test_it_moves_X_in_2():
    b = Board()
    new_board = b.move(2, 'X')

    expected = [[None, None, 'X'],
                [None, None, None],
                [None, None, None]]

    assert new_board.board_cells == expected

def test_it_moves_X_in_3():
    b = Board()
    new_board = b.move(3, 'X')

    expected = [[None, None, None],
                ['X', None, None],
                [None, None, None]]

    assert new_board.board_cells == expected

def test_it_moves_X_in_7():
    b = Board()
    new_board = b.move(7, 'X')

    expected = [[None, None, None],
                [None, None, None],
                [None, 'X', None]]

    assert new_board.board_cells == expected

def test_it_preserves_old_plays():
    _input = ['X', None, None, None, 'O', None, None, None, None]
    b = Board(_input)
    new_board = b.move(6, 'X')

    expected = [['X', None, None],
                [None, 'O', None],
                ['X', None, None]]

    assert new_board.board_cells == expected

def test_it_raises_index_error_when_cell_already_full():
    _input = ['X', None, None, None, 'O', None, None, None, None]
    b = Board(_input)

    with pytest.raises(IndexError):
        b.move(0, 'X')

