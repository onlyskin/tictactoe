import pytest
import sys

from get_human_move import get_human_move
from board import Board
from console_UI import Console_UI

def test_it_gets_3_first_time():
	sys.stdin = open('mock/get_human_move_stdin_1', 'r')

	_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	b = Board(_input)

	human_move = get_human_move(b, Console_UI)
	assert human_move == 3

def test_it_rejects_3_and_5_accepts_6():
	sys.stdin = open('mock/get_human_move_stdin_2', 'r')

	_input = ['0', '1', '2', 'X', 'X', 'O', '6', '7', '8']
	b = Board(_input)

	human_move = get_human_move(b, Console_UI)
	assert human_move == 6

