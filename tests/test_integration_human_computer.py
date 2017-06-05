import sys
from StringIO import StringIO

import pytest
from mock import patch

from game import GameMaker
from console_ui import ConsoleUi

@pytest.fixture(scope='function')
def ui():
    return ConsoleUi(StringIO())

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\n4\n6\n1\n5\n8\n'))
def test_simulated_h_c_game_1_returns_expected_output(ui):
    expected_output = open('fixtures/h_c_expected_output_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nA\nc\nB\nA\n0\n6\n5\n7\n2\n'))
def test_simulated_h_c_game_2_returns_expected_output(ui):
    expected_output = open('fixtures/h_c_expected_output_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\n!\nc\n?\n!\n0\n5\n2\n'))
def test_simulated_h_c_game_3_returns_expected_output(ui):
    expected_output = open('fixtures/h_c_expected_output_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\n4\n8\n1\n3\n6\n'))
def test_simulated_h_c_game_4_returns_expected_output(ui):
    expected_output = open('fixtures/h_c_expected_output_4.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('c\nX\nh\nO\nO\n4\n8\n1\n3\n6\n'))
def test_simulated_c_h_game_player_2_goes_first(ui):
    expected_output = open('fixtures/h_c_expected_output_5.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output
