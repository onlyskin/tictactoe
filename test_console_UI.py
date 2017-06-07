from StringIO import StringIO

import pytest

from console_ui import ConsoleUi
from board import Board
from game import Game
from human_player import HumanPlayer

def get_input_function(input_list):
    return lambda: input_list.pop(0)

def test_it_prints_board_to_stdout():
    ui = ConsoleUi(StringIO())
    b = Board()
    ui.output_board(b)
    expected_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    assert ui._out_stream.getvalue() == expected_output

def test_it_gets_6_from_stdin():
    ui = ConsoleUi(StringIO(), get_input_function(['3']))
    test_input = ui.get_input_integer()
    assert test_input == 3

def test_it_gets_h_from_stdin():
    ui = ConsoleUi(StringIO(), get_input_function(['we', 'h']))
    test_input = ui.get_player_type()
    assert test_input == 'h'

def test_it_gets_c_from_stdin():
    ui = ConsoleUi(StringIO(), get_input_function(['c']))
    test_input = ui.get_player_type()
    assert test_input == 'c'

def test_it_gets_Z_from_stdin():
    ui = ConsoleUi(StringIO(), get_input_function(['Z']))
    test_input = ui.get_player_marker()
    assert test_input == 'Z'

def test_it_gets_Y_from_stdin():
    ui = ConsoleUi(StringIO(), get_input_function(['xa', 'Y']))
    test_input = ui.get_player_marker()
    assert test_input == 'Y'

def test_it_gets_A_from_stdin():
    ui = ConsoleUi(StringIO(), get_input_function(['c', 'A']))
    player = ui.get_player()
    assert player.marker == 'A'

def test_it_prints_A_moved_in_4():
    ui = ConsoleUi(StringIO())
    b = Board(p1='A')
    player = HumanPlayer('A', ui)
    move = 4
    b = b.move(move)
    ui.output_moved_message(player, move, b)
    expected_output = 'Player A moved in cell 4:\n 0 | 1 | 2 \n===+===+===\n 3 | A | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    assert ui._out_stream.getvalue() == expected_output

def test_turn_start_message():
    ui = ConsoleUi(StringIO())
    player = HumanPlayer('A', ui)
    ui.output_start_turn_message(player)
    expected_output = "Player A's turn:\n"
    assert ui._out_stream.getvalue() == expected_output

def test_move_not_available_message():
    ui = ConsoleUi(StringIO())
    ui.output_move_not_available_message(3)
    expected_output = 'Cell 3 is not available, please choose another move:\n'
    assert ui._out_stream.getvalue() == expected_output

def test_end_message_when_draw():
    ui = ConsoleUi(StringIO())
    p1 = HumanPlayer('X', ui)
    p2 = HumanPlayer('O', ui)
    g = Game(ui, p1, p2)
    g.board = Board([['O', 'X', 'X'], ['X', 'X', 'O'], ['O', 'O', 'X']])
    expected_output = 'Game over!\nThe game was a draw.\n'
    ui.output_end_message(g)
    assert ui._out_stream.getvalue() == expected_output

def test_end_message_when_player_X_win():
    ui = ConsoleUi(StringIO())
    p1 = HumanPlayer('X', ui)
    p2 = HumanPlayer('O', ui)
    g = Game(ui, p1, p2)
    g.board = Board([['X', 'O', 'X'], ['O', 'O', 'X'], ['O', 'X', 'X']])
    expected_output = 'Game over!\nPlayer X won.\n'
    ui.output_end_message(g)
    assert ui._out_stream.getvalue() == expected_output

def test_get_players_in_order_stdout():
    ui = ConsoleUi(StringIO(), get_input_function(['B']))
    expected_output = 'Who should start, A or B?\n'
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    ui.get_players_in_order(p1, p2)
    assert ui._out_stream.getvalue() == expected_output

def test_get_players_in_order_returns_B_then_A():
    ui = ConsoleUi(StringIO(), get_input_function(['B']))
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    assert ui.get_players_in_order(p1, p2) == [p2, p1]

def test_get_players_in_order_asks_twice():
    ui = ConsoleUi(StringIO(), get_input_function(['X', 'B']))
    expected_output = 'Who should start, A or B?\nWho should start, A or B?\n'
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    ui.get_players_in_order(p1, p2)
    assert ui._out_stream.getvalue() == expected_output

def test_get_players_in_order_rejects_X_accepts_B():
    ui = ConsoleUi(StringIO(), get_input_function(['X', 'B']))
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    assert ui.get_players_in_order(p1, p2) == [p2, p1]

def test_get_player_rejects_when_same_symbol_chosen():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'A', 'h', 'A', 'h', 'A', 'h', 'B']))
    expected_output = open('fixtures/get_players_stdout.txt', 'r').read()
    ui.get_players()
    assert ui._out_stream.getvalue() == expected_output

def test_output_board_returns_string_when_all_empty():
    ui = ConsoleUi(StringIO())
    expected_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board()
    ui.output_board(b)
    assert ui._out_stream.getvalue() == expected_output

def test_output_board_returns_string_when_2_X():
    ui = ConsoleUi(StringIO())
    _input = [[None, None, 'X'], [None, None, None], [None, None, None]]
    expected_output = ' 0 | 1 | X \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert ui._out_stream.getvalue() == expected_output

def test_output_board_returns_string_when_3_O():
    ui = ConsoleUi(StringIO())
    _input = [[None, None, None], ['O', None, None], [None, None, None]]
    expected_output = ' 0 | 1 | 2 \n===+===+===\n O | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert ui._out_stream.getvalue() == expected_output

def test_output_board_returns_string_when_8_O():
    ui = ConsoleUi(StringIO())
    _input = [[None, None, None], [None, None, None], [None, None, 'O']]
    expected_output = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | O \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert ui._out_stream.getvalue() == expected_output

def test_output_board_returns_string_when_1_X_5_O():
    ui = ConsoleUi(StringIO())
    _input = [[None, 'X', None], [None, None, 'O'], [None, None, None]]
    expected_output = ' 0 | X | 2 \n===+===+===\n 3 | 4 | O \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert ui._out_stream.getvalue() == expected_output



