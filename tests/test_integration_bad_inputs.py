import pytest
import sys

from game import GameMaker
from console_ui import ConsoleUi
from human_player import HumanPlayer
from computer_player import ComputerPlayer

Ui = ConsoleUi()

def test_whole_game_when_same_marker_chosen_at_first(capsys):
    sys.stdin = open('mock/integration_bad_input_stdin_1', 'r')
    expected_stdout = open('mock/integration_bad_input_stdout_1.txt', 'r').read()
    consoleGameMaker = GameMaker(Ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    out, err = capsys.readouterr()
    assert out == expected_stdout

def test_whole_game_when_unavailable_moves_chosen(capsys):
    sys.stdin = open('mock/integration_bad_input_stdin_2', 'r')
    expected_stdout = open('mock/integration_bad_input_stdout_2.txt', 'r').read()
    consoleGameMaker = GameMaker(Ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    out, err = capsys.readouterr()
    assert out == expected_stdout

def test_whole_game_when_non_integer_entered_for_move(capsys):
    sys.stdin = open('mock/integration_bad_input_stdin_3', 'r')
    expected_stdout = open('mock/integration_bad_input_stdout_3.txt', 'r').read()
    consoleGameMaker = GameMaker(Ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    out, err = capsys.readouterr()
    assert out == expected_stdout


def test_whole_game_when_bad_first_player_marker_chosen(capsys):
    sys.stdin = open('mock/integration_bad_input_stdin_4', 'r')
    expected_stdout = open('mock/integration_bad_input_stdout_4.txt', 'r').read()
    consoleGameMaker = GameMaker(Ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    out, err = capsys.readouterr()
    assert out == expected_stdout

def test_whole_game_when_bad_player_type_chosen(capsys):
    sys.stdin = open('mock/integration_bad_input_stdin_5', 'r')
    expected_stdout = open('mock/integration_bad_input_stdout_5.txt', 'r').read()
    consoleGameMaker = GameMaker(Ui)
    game = consoleGameMaker.make_game()
    game.start_game()
    out, err = capsys.readouterr()
    assert out == expected_stdout

