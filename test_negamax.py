import pytest

from negamax import negamax
from board import Board

def test_it_chooses_winning_move_and_blocks_opponent():
    cells = [['O', None, 'X'], ['X', None, None], ['X', 'O', 'O']]
    b = Board(cells, 'X', 'O')
    negamax_result = negamax(b)
    assert negamax_result.move == 4

def test_it_blocks_opponent_winning_move():
    cells = [['O', 'X', 'O'], [None, 'X', 'O'], ['X', None, 'X']]
    b = Board(cells, 'X', 'O')
    negamax_result = negamax(b)
    assert negamax_result.move == 7

def test_it_chooses_winning_move():
    cells = [['O', 'X', 'O'], [None, 'O', 'O'], ['X', None, 'X']]
    b = Board(cells, 'O', 'X')
    negamax_result = negamax(b)
    assert negamax_result.move == 7

def test_it_blocks_opponent_winning_move_3_levels():
    cells = [['O', 'X', 'O'], [None, None, 'O'], ['X', None, 'X']]
    b = Board(cells, 'O', 'X')
    negamax_result = negamax(b)
    assert negamax_result.move == 7

def test_it_blocks_opponent_winning_move_near_start():
    cells = [['O', None, 'O'], ['X', None, None], [None, None, None]]
    b = Board(cells, 'O', 'X')
    negamax_result = negamax(b)
    assert negamax_result.move == 1

def test_it_chooses_only_available_move():
    cells = [['O', 'X', 'X'], ['O', None, 'O'], ['X', 'O', 'X']]
    b = Board(cells, 'X', 'O')
    negamax_result = negamax(b)
    assert negamax_result.move == 4
