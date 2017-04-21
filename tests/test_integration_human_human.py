import pytest
import sys

from game import GameMaker
from console_UI import Console_UI
from humanPlayer import HumanPlayer

def test_simulated_h_h_game_1_returns_expected_stdout(capsys):
	sys.stdin = open('mock/h_h_simulated_stdin_1', 'r')
	expected_stdout = open('mock/h_h_expected_stdout_1.txt', 'r').read()
	consoleGameMaker = GameMaker(Console_UI)
	game = consoleGameMaker.make_game()
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_simulated_h_h_game_2_returns_expected_stdout(capsys):
	sys.stdin = open('mock/h_h_simulated_stdin_2', 'r')
	expected_stdout = open('mock/h_h_expected_stdout_2.txt', 'r').read()
	consoleGameMaker = GameMaker(Console_UI)
	game = consoleGameMaker.make_game()
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout
