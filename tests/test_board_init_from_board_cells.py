import pytest

from board import Board

def test_board_cells_all_numbers():
    _input = [[None, 'X', None],
                [None, 'X', None],
                [None, None, None]]
    b = Board.from_board_cells(_input)
    assert b.board_cells == _input
    assert b.board_cells is not _input
