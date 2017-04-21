import pytest
import sys

from humanPlayer import HumanPlayer
from board import Board
from console_UI import Console_UI

def test_it_gets_3_first_time():
	sys.stdin = open('mock/get_human_move_stdin_1', 'r')

	_input = [None, None, None, None, None, None, None, None, None]
	b = Board(_input)

	human_player = HumanPlayer('O')
	opponent = HumanPlayer('X')

	human_move = human_player.get_move(Console_UI, b, opponent)
	assert human_move == 3

def test_it_rejects_3_and_5_accepts_6():
	sys.stdin = open('mock/get_human_move_stdin_2', 'r')

	_input = [None, None, None, 'X', 'X', 'O', None, None, None]
	b = Board(_input)

	human_player = HumanPlayer('O')
	opponent = HumanPlayer('X')

	human_move = human_player.get_move(Console_UI, b, opponent)
	assert human_move == 6

