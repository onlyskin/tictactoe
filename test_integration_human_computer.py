from StringIO import StringIO

import pytest

from game import GameMaker
from console_ui import ConsoleUi

def get_input_function(input_list):
    return lambda: input_list.pop(0)

def test_simulated_h_c_game_1_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'O', 'c', 'X', 'O', '4', '6', '1', '5', '8']))
    expected_output = open('fixtures/h_c_expected_output_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_simulated_h_c_game_2_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'A', 'c', 'B', 'A', '0', '6', '5', '7', '2']))
    expected_output = open('fixtures/h_c_expected_output_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_simulated_h_c_game_3_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', '!', 'c', '?', '!', '0', '5', '2']))
    expected_output = open('fixtures/h_c_expected_output_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_simulated_h_c_game_4_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'O', 'c', 'X', 'O', '4', '8', '1', '3', '6']))
    expected_output = open('fixtures/h_c_expected_output_4.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_simulated_c_h_game_player_2_goes_first():
    ui = ConsoleUi(StringIO(), get_input_function(['c', 'X', 'h', 'O', 'O', '4', '8', '1', '3', '6']))
    expected_output = open('fixtures/h_c_expected_output_5.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output
