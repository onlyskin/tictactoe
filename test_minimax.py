import pytest

from minimax import minimax, _get_score
from board import Board

def test_it_knows_opponent_will_take_winning_move():
    cells = [['O', None, 'X'], ['X', None, None], ['X', 'O', 'O']]
    b = Board(cells, 'X', 'O')
    minimax_result = minimax(b, 'X')
    assert minimax_result.move == 4

def test_it_blocks_opponent_winning_move():
    cells = [['O', 'X', 'O'], [None, 'X', 'O'], ['X', None, 'X']]
    b = Board(cells, 'X', 'O')
    minimax_result = minimax(b, 'O')
    assert minimax_result.move == 7

def test_it_chooses_winning_move():
    cells = [['O', 'X', 'O'], [None, 'O', 'O'], ['X', None, 'X']]
    b = Board(cells, 'O', 'X')
    minimax_result = minimax(b, 'X')
    assert minimax_result.move == 7

def test_it_blocks_opponent_winning_move_3_levels():
    cells = [['O', 'X', 'O'], [None, None, 'O'], ['X', None, 'X']]
    b = Board(cells, 'O', 'X')
    minimax_result = minimax(b, 'O')
    assert minimax_result.move == 7

def test_it_blocks_opponent_winning_move_near_start():
    cells = [['O', None, 'O'], ['X', None, None], [None, None, None]]
    b = Board(cells, 'O', 'X')
    minimax_result = minimax(b, 'X')
    assert minimax_result.move == 1

def test_get_score_raises_value_error_on_unfinished_board_no_winner():
    b = Board([['X', 'X', 'O'], ['O', 'X', 'O'], [None, None, None]])
    with pytest.raises(ValueError):
        _get_score(b, 'X')

def test_get_score_returns_0_when_draw():
    b = Board([['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']])
    assert _get_score(b, 'X') == 0

def test_get_score_returns_10_on_unfinished_board_active_winner():
    b = Board([['X', 'X', 'X'], ['O', 'O', None], [None, None, None]])
    assert _get_score(b, 'X') == 10

def test_get_score_returns_10_on_finished_board_active_winner():
    b = Board([['X', 'X', 'O'], ['X', 'O', 'O'], ['O', 'X', 'X']])
    assert _get_score(b, 'O') == 10

def test_get_score_returns_10_on_unfinished_board_opponent_winner():
    b = Board([['X', 'X', 'X'], ['O', 'O', None], [None, None, None]])
    assert _get_score(b, 'O') == -10

def test_get_score_returns_minus_10_on_finished_board_opponent_winner():
    b = Board([['X', 'X', 'O'], ['X', 'O', 'O'], ['O', 'X', 'X']])
    assert _get_score(b, 'X') == -10





