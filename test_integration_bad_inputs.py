from StringIO import StringIO

import pytest

from game import GameMaker
from console_ui import ConsoleUi

def get_input_function(input_list):
    return lambda: input_list.pop(0)

def test_whole_game_when_same_marker_chosen_at_first():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'X', 'c', 'X', 'c', 'X', 'h', 'O', 'O', '4', '6', '1', '5', '8']))
    expected_output = open('fixtures/integration_bad_input_output_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_whole_game_when_unavailable_moves_chosen():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'O', 'c', 'X', 'O', '4', '0', '6', '1', '3', '5', '8']))
    expected_output = open('fixtures/integration_bad_input_output_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_whole_game_when_non_integer_entered_for_move():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'O', 'c', 'X', 'O', 'a', '4', 'o', '2', '3', '7', '8']))
    expected_output = open('fixtures/integration_bad_input_output_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_whole_game_when_bad_first_player_marker_chosen():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'X', 'c', 'O', 'a', 'b', 'X', '5', '4', '6', '1', '8']))
    expected_output = open('fixtures/integration_bad_input_output_4.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_whole_game_when_bad_player_type_chosen():
    ui = ConsoleUi(StringIO(), get_input_function(['x', 'h', 'O', 'b', 'r', 'c', 'X', 'O', '4', '5', '6', '1', '8']))
    expected_output = open('fixtures/integration_bad_input_output_5.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output
