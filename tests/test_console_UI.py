import pytest
import sys

from console_UI import Console_UI
from board import Board

def test_it_prints_string_to_stdout_with_newline(capsys):
	test_string = 'testing'
	Console_UI.output_string(test_string)
	out, err = capsys.readouterr()
	assert out == 'testing\n'

def test_it_prints_board_to_stdout(capsys):
	_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
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



