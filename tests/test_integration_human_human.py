import sys
from StringIO import StringIO

import pytest
from mock import patch

from game import GameMaker
from console_ui import ConsoleUi

@pytest.fixture(scope='function')
def ui():
    return ConsoleUi(StringIO())

@patch('sys.stdin', StringIO('h\nO\nh\nX\nO\n4\n0\n6\n2\n1\n7\n5\n3\n8\n'))
def test_simulated_h_h_game_1_returns_expected_output(ui):
    expected_output = open('fixtures/h_h_expected_output_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nA\nh\nB\nA\n0\n4\n6\n3\n5\n1\n7\n8\n2\n'))
def test_simulated_h_h_game_2_returns_expected_output(ui):
    expected_output = open('fixtures/h_h_expected_output_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nY\nh\nZ\nZ\n4\n3\n0\n8\n2\n6\n1\n'))
def test_simulated_h_h_game_3_returns_expected_output(ui):
    expected_output = open('fixtures/h_h_expected_output_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output
