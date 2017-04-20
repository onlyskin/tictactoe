import pytest
import sys

from game import Game
from console_UI import Console_UI
from humanPlayer import HumanPlayer
from computerPlayer import ComputerPlayer

def test_simulated_game_1_returns_expected_stdout(capsys):
	sys.stdin = open('mock/simulated_stdin_1', 'r')
	expected_stdout = open('mock/expected_stdout_1.txt', 'r').read()
	player1 = HumanPlayer("O")
	player2 = ComputerPlayer("X")
	game = Game(Console_UI, player1, player2)
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_simulated_game_2_returns_expected_stdout(capsys):
	sys.stdin = open('mock/simulated_stdin_2', 'r')
	expected_stdout = open('mock/expected_stdout_2.txt', 'r').read()
	player1 = HumanPlayer("O")
	player2 = ComputerPlayer("X")
	game = Game(Console_UI, player1, player2)
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_simulated_game_3_returns_expected_stdout(capsys):
	sys.stdin = open('mock/simulated_stdin_3', 'r')
	expected_stdout = open('mock/expected_stdout_3.txt', 'r').read()
	player1 = HumanPlayer("O")
	player2 = ComputerPlayer("X")
	game = Game(Console_UI, player1, player2)
	game.start_game()
	out, err = capsys.readouterr()
	assert out == expected_stdout

