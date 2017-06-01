import sys
from StringIO import StringIO

import pytest
from mock import patch

from game import GameMaker
from console_ui import ConsoleUi

ui = ConsoleUi()

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\n4\n6\n1\n5\n8\n'))
@patch('sys.stdout', StringIO())
def test_simulated_h_c_game_1_returns_expected_stdout():
    expected_stdout = open('fixtures/h_c_expected_stdout_1.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('h\nA\nc\nB\nA\n0\n6\n5\n7\n2\n'))
@patch('sys.stdout', StringIO())
def test_simulated_h_c_game_2_returns_expected_stdout():
    expected_stdout = open('fixtures/h_c_expected_stdout_2.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('h\n!\nc\n?\n!\n0\n5\n2\n'))
@patch('sys.stdout', StringIO())
def test_simulated_h_c_game_3_returns_expected_stdout():
    expected_stdout = open('fixtures/h_c_expected_stdout_3.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('h\nO\nc\nX\nO\n4\n8\n1\n3\n6\n'))
@patch('sys.stdout', StringIO())
def test_simulated_h_c_game_4_returns_expected_stdout():
    expected_stdout = open('fixtures/h_c_expected_stdout_4.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

@patch('sys.stdin', StringIO('c\nX\nh\nO\nO\n4\n8\n1\n3\n6\n'))
@patch('sys.stdout', StringIO())
def test_simulated_c_h_game_player_2_goes_first():
    expected_stdout = open('fixtures/h_c_expected_stdout_5.txt', 'r').read()
    consoleGameMaker = GameMaker(ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    assert sys.stdout.getvalue() == expected_stdout

