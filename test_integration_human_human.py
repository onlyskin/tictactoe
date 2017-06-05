from StringIO import StringIO

import pytest

from game import GameMaker
from console_ui import ConsoleUi

def get_input_function(input_list):
    return lambda: input_list.pop(0)

def test_simulated_h_h_game_1_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'O', 'h', 'X', 'O', '4', '0', '6', '2', '1', '7', '5', '3', '8']))
    expected_output = open('fixtures/h_h_expected_output_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_simulated_h_h_game_2_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'A', 'h', 'B', 'A', '0', '4', '6', '3', '5', '1', '7', '8', '2']))
    expected_output = open('fixtures/h_h_expected_output_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

def test_simulated_h_h_game_3_returns_expected_output():
    ui = ConsoleUi(StringIO(), get_input_function(['h', 'Y', 'h', 'Z', 'Z', '4', '3', '0', '8', '2', '6', '1']))
    expected_output = open('fixtures/h_h_expected_output_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output
