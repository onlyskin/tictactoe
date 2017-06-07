import pytest

from board import Board

def test_boards_with_same_cells_are_equal():
    b1 = Board([['X', 'O', 'X'], ['O', 'O', 'X'], ['X', None, None]])
    b2 = Board([['X', 'O', 'X'], ['O', 'O', 'X'], ['X', None, None]])
    assert b1 == b2

def test_boards_with_different_cells_arent_equal():
    b1 = Board([['X', 'O', 'X'], ['O', 'O', 'X'], ['X', None, None]])
    b2 = Board([['X', 'O', 'X'], ['O', 'O', 'X'], ['X', None, 'X']])
    assert b1 != b2

def test_flatten_returns_flat_board():
    b = Board([['X', 'O', None], [None, None, 'X'], [None, None, None]])
    assert b._flatten() == ['X', 'O', None, None, None, 'X', None, None, None]

def test_empty_board_returns_all_positions_as_available():
    b = Board()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert b.get_available_positions() == expected

def test_partly_full_board_returns_some_positions_as_available():
    _input = [[None, None, None], ['X', None, None], [None, 'O', None]]
    b = Board(_input)
    expected = [0, 1, 2, 4, 5, 6, 8]
    assert b.get_available_positions() == expected

def test_board_supports_get_indexing():
    _input = [['X', None, None], [None, None, None], [None, 'O', None]]
    b = Board(_input)
    assert b[0] == 'X'
    assert b[7] == 'O'
    assert b[4] == None

def test_board_can_initialize_from_all_None_cells():
    _input = [[None, None, None], [None, None, None], [None, None, None]]
    expected = [[None, None, None],
                [None, None, None],
                [None, None, None]]
    b = Board(_input)
    assert b._board_cells == expected

def test_board_can_initialize_from_some_filled_cells():
    _input = [['O', None, 'X'], [None, 'X', None], ['O', None, None]]
    expected = [['O', None, 'X'],
                [None, 'X', None],
                ['O', None, None]]
    b = Board(_input)
    assert b._board_cells == expected

def test_board_can_initialize_from_default_argument():
    expected = [[None, None, None],
                [None, None, None],
                [None, None, None]]
    b = Board()
    assert b._board_cells == expected

def test_move_puts_marker_in_cell():
    b = Board()
    new_board = b.move(0, 'X')

    expected = [['X', None, None],
                [None, None, None],
                [None, None, None]]

    assert new_board._board_cells == expected

def test_move_preserves_previous_board_cells():
    _input = [['X', None, None], [None, 'O', None], [None, None, None]]
    b = Board(_input)
    new_board = b.move(6, 'X')

    expected = [['X', None, None],
                [None, 'O', None],
                ['X', None, None]]

    assert new_board._board_cells == expected

def test_move_raises_index_error_when_cell_already_full():
    _input = [['X', None, None], [None, 'O', None], [None, None, None]]
    b = Board(_input)

    with pytest.raises(IndexError):
        b.move(0, 'X')

def test_board_supports_set_indexing():
    b = Board()
    b[0] = 'X'
    assert b[0] == 'X'

def test_is_full_it_returns_false_when_empty():
    b = Board()
    assert not b._is_full()

def test_is_full_returns_true_when_full():
    _input = [['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    b = Board(_input)
    assert b._is_full()

def test_is_full_returns_false_when_partly_full():
    _input = [['O', None, 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    b = Board(_input)
    assert not b._is_full()

def test_is_tie_returns_false_when_empty():
    b = Board()
    assert not b.is_tie()

def test_is_tie_returns_true_when_full_and_tied():
    b = Board([['O', 'X', 'X'], ['X', 'X', 'O'], ['O', 'O', 'X']])
    assert b.is_tie()

def test_is_tie_returns_false_when_full_with_winner():
    b = Board([['X', 'O', 'X'], ['O', 'O', 'X'], ['O', 'X', 'X']])
    assert not b.is_tie()

def test_it_returns_false_when_empty():
    b = Board()
    assert not b.is_winner()

def test_it_returns_true_when_left_column_all_X():
    b = Board([['X', None, None], ['X', None, None], ['X', None, None]])
    assert b.is_winner()

def test_it_returns_false_when_left_column_X_O_X():
    b = Board([['X', None, None], ['O', None, None], ['X', None, None]])
    assert not b.is_winner()

def test_it_returns_true_when_middle_column_all_X():
    b = Board([[None, 'X', None], [None, 'X', None], [None, 'X', None]])
    assert b.is_winner()

def test_it_returns_false_when_middle_column_O_X_X():
    b = Board([[None, 'O', None], [None, 'X', None], [None, 'X', None]])
    assert not b.is_winner()

def test_it_returns_true_when_right_column_all_X():
    b = Board([[None, None, 'X'], [None, None, 'X'], [None, None, 'X']])
    assert b.is_winner()

def test_it_returns_false_when_right_column_O_X_X():
    b = Board([[None, None, 'O'], [None, None, 'X'], [None, None, 'X']])
    assert not b.is_winner()

def test_it_returns_true_when_top_row_all_O():
    b = Board([['O', 'O', 'O'], [None, None, None], [None, None, None]])
    assert b.is_winner()

def test_it_returns_false_when_top_row_O_X_O():
    b = Board([['O', 'X', 'O'], [None, None, None], [None, None, None]])
    assert not b.is_winner()

def test_it_returns_true_when_second_row_all_O():
    b = Board([[None, None, None], ['O', 'O', 'O'], [None, None, None]])
    assert b.is_winner()

def test_it_returns_false_when_second_row_O_X_O():
    b = Board([[None, None, None], ['O', 'X', 'O'], [None, None, None]])
    assert not b.is_winner()

def test_it_returns_true_when_bottom_row_all_O():
    b = Board([[None, None, None], [None, None, None], ['O', 'O', 'O']])
    assert b.is_winner()

def test_it_returns_false_when_bottom_row_O_X_O():
    b = Board([[None, None, None], [None, None, None], ['O', 'X', 'O']])
    assert not b.is_winner()

def test_it_returns_true_when_diagonal_1_is_X():
    b = Board([['X', None, None], [None, 'X', None], [None, None, 'X']])
    assert b.is_winner()

def test_it_returns_true_when_diagonal_2_is_O():
    b = Board([[None, None, 'O'], [None, 'O', None], ['O', None, None]])
    assert b.is_winner()

def test_it_gets_current_player_as_A():
    b = Board(p1='A', p2='B')
    assert b.get_current_player_marker() == 'A'

def test_it_gets_current_player_as_B():
    b = Board(p1='B', p2='Y')
    assert b.get_current_player_marker() == 'B'

def test_it_gets_current_player_when_one_turn():
    b = Board(p1='B', p2='Y')
    b[1] = 'B'
    assert b.get_current_player_marker() == 'Y'

def test_it_gets_current_player_when_three_turns():
    b = Board(p1='B', p2='Y')
    b[1] = 'B'
    b[2] = 'Y'
    b[3] = 'B'
    assert b.get_current_player_marker() == 'Y'

def test_it_gets_current_player_when_two_turns():
    b = Board(p1='B', p2='Y')
    b[1] = 'B'
    b[2] = 'Y'
    assert b.get_current_player_marker() == 'B'

