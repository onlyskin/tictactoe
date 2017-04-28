import pytest
import sys

from game import GameMaker
from consoleUi import ConsoleUi
from humanPlayer import HumanPlayer
from computerPlayer import ComputerPlayer

Ui = ConsoleUi()

def test_simulated_h_c_game_1_returns_expected_stdout(capsys):
	sys.stdin = open('mock/h_c_simulated_stdin_1', 'r')
	expected_stdout = open('mock/h_c_expected_stdout_1.txt', 'r').read()
	consoleGameMaker = GameMaker(Ui)
	game = consoleGameMaker.make_game()
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_simulated_h_c_game_2_returns_expected_stdout(capsys):
	sys.stdin = open('mock/h_c_simulated_stdin_2', 'r')
	expected_stdout = open('mock/h_c_expected_stdout_2.txt', 'r').read()
	consoleGameMaker = GameMaker(Ui)
	game = consoleGameMaker.make_game()
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_simulated_h_c_game_3_returns_expected_stdout(capsys):
	sys.stdin = open('mock/h_c_simulated_stdin_3', 'r')
	expected_stdout = open('mock/h_c_expected_stdout_3.txt', 'r').read()
	consoleGameMaker = GameMaker(Ui)
	game = consoleGameMaker.make_game()
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

