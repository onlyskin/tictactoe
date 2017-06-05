import sys
from StringIO import StringIO

import pytest
from mock import patch

from game import GameMaker
from console_ui import ConsoleUi

@pytest.fixture(scope='function')
def ui():
    return ConsoleUi(StringIO())

@patch('sys.stdin', StringIO('h\nX\nc\nX\nc\nX\nh\nO\nO\n4\n6\n1\n5\n8\n'))
def test_whole_game_when_same_marker_chosen_at_first(ui):
    expected_output = open('fixtures/integration_bad_input_output_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\n4\n0\n6\n1\n3\n5\n8\n'))
def test_whole_game_when_unavailable_moves_chosen(ui):
    expected_output = open('fixtures/integration_bad_input_output_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\na\n4\no\n2\n3\n7\n8\n'))
def test_whole_game_when_non_integer_entered_for_move(ui):
    expected_output = open('fixtures/integration_bad_input_output_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('h\nX\nc\nO\na\nb\nX\n5\n4\n6\n1\n8\n'))
def test_whole_game_when_bad_first_player_marker_chosen(ui):
    expected_output = open('fixtures/integration_bad_input_output_4.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output

@patch('sys.stdin', StringIO('x\nh\nO\nb\nr\nc\nX\nO\n4\n5\n6\n1\n8\n'))
def test_whole_game_when_bad_player_type_chosen(ui):
    expected_output = open('fixtures/integration_bad_input_output_5.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert ui._out_stream.getvalue() == expected_output
