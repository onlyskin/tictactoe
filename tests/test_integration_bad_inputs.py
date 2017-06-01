import sys
from StringIO import StringIO

import pytest
from mock import patch

from game import GameMaker
from console_ui import ConsoleUi

ui = ConsoleUi()

@patch('sys.stdin', StringIO('h\nX\nc\nX\nc\nX\nh\nO\nO\n4\n6\n1\n5\n8\n'))
@patch('sys.stdout', StringIO())
def test_whole_game_when_same_marker_chosen_at_first():
    expected_stdout = open('fixtures/integration_bad_input_stdout_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\n4\n0\n6\n1\n3\n5\n8\n'))
@patch('sys.stdout', StringIO())
def test_whole_game_when_unavailable_moves_chosen():
    expected_stdout = open('fixtures/integration_bad_input_stdout_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\na\n4\no\n2\n3\n7\n8\n'))
@patch('sys.stdout', StringIO())
def test_whole_game_when_non_integer_entered_for_move():
    expected_stdout = open('fixtures/integration_bad_input_stdout_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('h\nX\nc\nO\na\nb\nX\n5\n4\n6\n1\n8\n'))
@patch('sys.stdout', StringIO())
def test_whole_game_when_bad_first_player_marker_chosen():
    expected_stdout = open('fixtures/integration_bad_input_stdout_4.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('x\nh\nO\nb\nr\nc\nX\nO\n4\n5\n6\n1\n8\n'))
@patch('sys.stdout', StringIO())
def test_whole_game_when_bad_player_type_chosen():
    expected_stdout = open('fixtures/integration_bad_input_stdout_5.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

