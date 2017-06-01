import sys
from StringIO import StringIO

import pytest
from mock import patch

from console_ui import ConsoleUi
from board import Board
from game import Game
from human_player import HumanPlayer

ui = ConsoleUi()

@patch('sys.stdout', StringIO())
def test_it_prints_board_to_stdout():
    b = Board()
    ui.output_board(b)
    expected_stdout = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('3\n'))
def test_it_gets_6_from_stdin():
    test_input = ui.get_input_integer()
    assert test_input == 3

@patch('sys.stdin', StringIO('we\nh\n'))
def test_it_gets_h_from_stdin():
    test_input = ui.get_player_type()
    assert test_input == 'h'

@patch('sys.stdin', StringIO('c\n'))
def test_it_gets_c_from_stdin():
    test_input = ui.get_player_type()
    assert test_input == 'c'

@patch('sys.stdin', StringIO('Z\n'))
def test_it_gets_Z_from_stdin():
    test_input = ui.get_player_marker()
    assert test_input == 'Z'

@patch('sys.stdin', StringIO('xa\n\nY\n'))
def test_it_gets_Y_from_stdin():
    test_input = ui.get_player_marker()
    assert test_input == 'Y'

@patch('sys.stdin', StringIO('c\nA\n'))
def test_it_gets_A_from_stdin():
    player = ui.get_player()
    assert player.marker == 'A'

@patch('sys.stdout', StringIO())
def test_it_prints_A_moved_in_4():
    b = Board()
    player = HumanPlayer('A', ui)
    move = 4
    b = b.move(move, player.marker)
    ui.output_moved_message(player, move, b)
    expected_stdout = 'Player A moved in cell 4:\n 0 | 1 | 2 \n===+===+===\n 3 | A | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_turn_start_message():
    player = HumanPlayer('A', ui)
    ui.output_start_turn_message(player)
    expected_stdout = "Player A's turn:\n"
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_move_not_available_message():
    ui.output_move_not_available_message(3)
    expected_stdout = 'Cell 3 is not available, please choose another move:\n'
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_end_message_when_draw():
    g = Game(ui, '', '')
    g.board = Board(['O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X'])
    expected_stdout = 'Game over!\nThe game was a draw.\n'
    ui.output_end_message(g)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_end_message_when_player_X_win():
    g = Game(ui, '', '')
    g.board = Board(['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X'])
    expected_stdout = 'Game over!\nPlayer X won.\n'
    ui.output_end_message(g)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('B\n'))
@patch('sys.stdout', StringIO())
def test_get_players_in_order_stdout():
    expected_stdout = 'Who should start, A or B?\n'
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    ui.get_players_in_order(p1, p2)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('B\n'))
def test_get_players_in_order_returns_B_then_A():
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    assert ui.get_players_in_order(p1, p2) == [p2, p1]

@patch('sys.stdin', StringIO('X\nB\n'))
@patch('sys.stdout', StringIO())
def test_get_players_in_order_asks_twice():
    expected_stdout = 'Who should start, A or B?\nWho should start, A or B?\n'
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    ui.get_players_in_order(p1, p2)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('X\nB\n'))
def test_get_players_in_order_rejects_X_accepts_A():
    p1 = HumanPlayer('A', ui)
    p2 = HumanPlayer('B', ui)
    assert ui.get_players_in_order(p1, p2) == [p2, p1]

@patch('sys.stdin', StringIO('h\nA\nh\nA\nh\nA\nh\nB\n'))
@patch('sys.stdout', StringIO())
def test_get_player_rejects_when_same_symbol_chosen():
    expected_stdout = open('fixtures/get_players_stdout.txt', 'r').read()
    ui.get_players()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_all_empty():
    expected_stdout = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board()
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_0_X():
    _input = ['X', None, None, None, None, None, None, None, None]
    expected_stdout = ' X | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_1_X():
    _input = [None, 'X', None, None, None, None, None, None, None]
    expected_stdout = ' 0 | X | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_2_X():
    _input = [None, None, 'X', None, None, None, None, None, None]
    expected_stdout = ' 0 | 1 | X \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_3_O():
    _input = [None, None, None, 'O', None, None, None, None, None]
    expected_stdout = ' 0 | 1 | 2 \n===+===+===\n O | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_8_O():
    _input = [None, None, None, None, None, None, None, None, 'O']
    expected_stdout = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | O \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdout', StringIO())
def test_output_board_returns_string_when_1_X_5_O():
    _input = [None, 'X', None, None, None, 'O', None, None, None]
    expected_stdout = ' 0 | X | 2 \n===+===+===\n 3 | 4 | O \n===+===+===\n 6 | 7 | 8 \n\n'
    b = Board(_input)
    ui.output_board(b)
    assert sys.stdout.getvalue() == expected_stdout

