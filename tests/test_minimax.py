import pytest

from minimax import minimax_on_board
from board import Board

def test_it_knows_opponent_will_take_winning_move():
	b = Board(['O', None, 'X', 'X', None, None, 'X', 'O', 'O'])
	minimax_result = minimax_on_board(b, 'X', 'O')
	assert minimax_result.move == 4

def test_it_blocks_opponent_winning_move():
	b = Board(['O', 'X', 'O', None, 'X', 'O', 'X', None, 'X'])
	minimax_result = minimax_on_board(b, 'O', 'X')
	assert minimax_result.move == 7

def test_it_chooses_winning_move():
	b = Board(['O', 'X', 'O', None, 'O', 'O', 'X', None, 'X'])
	minimax_result = minimax_on_board(b, 'X', 'O')
	assert minimax_result.move == 7

def test_it_blocks_opponent_winning_move_3_levels():
	b = Board(['O', 'X', 'O', None, None, 'O', 'X', None, 'X'])
	minimax_result = minimax_on_board(b, 'O', 'X')
	assert minimax_result.move == 7

def test_it_blocks_opponent_winning_move_near_start():
	b = Board(['O', None, 'O', 'X', None, None, None, None, None])
	minimax_result = minimax_on_board(b, 'X', 'O')
	assert minimax_result.move == 1

