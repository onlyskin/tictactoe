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
	sys.stdin = open('mock/Console_UI_stdin', 'r')
	test_input = Console_UI.get_input_integer()
	assert test_input == 3

