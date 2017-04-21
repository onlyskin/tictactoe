import pytest
import sys

from console_UI import Console_UI
from board import Board
from humanPlayer import HumanPlayer

def test_it_prints_board_to_stdout(capsys):
	_input = [None, None, None, None, None, None, None, None, None]
	b = Board(_input)
	Console_UI.output_board(b)
	expected_stdout = open('mock/Console_UI_stdout.txt', 'r').read()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_it_gets_6_from_stdin():
	sys.stdin = open('mock/get_input_integer', 'r')
	test_input = Console_UI.get_input_integer()
	assert test_input == 3

def test_it_gets_h_from_stdin():
	sys.stdin = open('mock/get_player_type_stdin_1', 'r')
	test_input = Console_UI.get_player_type()
	assert test_input == 'h'

def test_it_gets_c_from_stdin():
	sys.stdin = open('mock/get_player_type_stdin_2', 'r')
	test_input = Console_UI.get_player_type()
	assert test_input == 'c'

def test_it_gets_Z_from_stdin():
	sys.stdin = open('mock/get_player_marker_stdin_1', 'r')
	test_input = Console_UI.get_player_marker()
	assert test_input == 'Z'

def test_it_gets_Y_from_stdin():
	sys.stdin = open('mock/get_player_marker_stdin_2', 'r')
	test_input = Console_UI.get_player_marker()
	assert test_input == 'Y'

def test_it_gets_A_from_stdin():
	sys.stdin = open('mock/get_player_stdin', 'r')
	player = Console_UI.get_player()
	assert player.marker == 'A'

def test_it_prints_A_moved_in_4(capsys):
	player = HumanPlayer('A')
	move = 4
	Console_UI.output_moved_message(player, move)
	expected_stdout = 'Player "A" moved in cell 4:\n'
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_turn_start_message(capsys):
	player = HumanPlayer('A')
	Console_UI.output_turn_start_message(player)
	expected_stdout = '''Player "A"'s turn:\n'''
	out, err = capsys.readouterr()
	assert out == expected_stdout




