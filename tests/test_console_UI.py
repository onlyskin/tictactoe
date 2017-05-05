import pytest
import sys

from console_ui import ConsoleUi
from board import Board
from game import Game
from human_player import HumanPlayer

ui = ConsoleUi()

def test_it_prints_board_to_stdout(capsys):
	b = Board()
	ui.output_board(b)
	expected_stdout = open('mock/Console_UI_stdout.txt', 'r').read()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_it_gets_6_from_stdin():
	sys.stdin = open('mock/get_input_integer', 'r')
	test_input = ui.get_input_integer()
	assert test_input == 3

def test_it_gets_h_from_stdin():
	sys.stdin = open('mock/get_player_type_stdin_1', 'r')
	test_input = ui.get_player_type()
	assert test_input == 'h'

def test_it_gets_c_from_stdin():
	sys.stdin = open('mock/get_player_type_stdin_2', 'r')
	test_input = ui.get_player_type()
	assert test_input == 'c'

def test_it_gets_Z_from_stdin():
	sys.stdin = open('mock/get_player_marker_stdin_1', 'r')
	test_input = ui.get_player_marker()
	assert test_input == 'Z'

def test_it_gets_Y_from_stdin():
	sys.stdin = open('mock/get_player_marker_stdin_2', 'r')
	test_input = ui.get_player_marker()
	assert test_input == 'Y'

def test_it_gets_A_from_stdin():
	sys.stdin = open('mock/get_player_stdin', 'r')
	player = ui.get_player()
	assert player.marker == 'A'

def test_it_prints_A_moved_in_4(capsys):
	b = Board()
	player = HumanPlayer('A')
	move = 4
	b = b.move(move, player.marker)
	ui.output_moved_message(player, move, b)
	expected_stdout = open('mock/get_moved_message_expected_stdout.txt', 'r').read()
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_turn_start_message(capsys):
	player = HumanPlayer('A')
	ui.output_start_turn_message(player)
	expected_stdout = "Player A's turn:\n"
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_move_not_available_message(capsys):
	ui.output_move_not_available_message(3)
	expected_stdout = 'Cell 3 is not available, please choose another move:\n'
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_end_message_when_draw(capsys):
	g = Game(ui, '', '')
	g.board = Board(['O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X'])
	expected_stdout = 'Game over!\nThe game was a draw.\n'

	ui.output_end_message(g)
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_end_message_when_player_X_win(capsys):
	g = Game(ui, '', '')
	g.board = Board(['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'X'])
	expected_stdout = 'Game over!\nPlayer X won.\n'

	ui.output_end_message(g)
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_get_players_in_order_stdout(capsys):
	sys.stdin = open('mock/get_players_in_order_stdin_1', 'r')
	expected_stdout = 'Who should start, A or B?\n'
	p1 = HumanPlayer('A')
	p2 = HumanPlayer('B')
	ui.get_players_in_order(p1, p2)
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_get_players_in_order_returns_B_then_A():
	sys.stdin = open('mock/get_players_in_order_stdin_1', 'r')
	p1 = HumanPlayer('A')
	p2 = HumanPlayer('B')
	assert ui.get_players_in_order(p1, p2) == [p2, p1]

def test_get_players_in_order_asks_twice(capsys):
	sys.stdin = open('mock/get_players_in_order_stdin_2', 'r')
	expected_stdout = 'Who should start, A or B?\nWho should start, A or B?\n'
	p1 = HumanPlayer('A')
	p2 = HumanPlayer('B')
	ui.get_players_in_order(p1, p2)
	out, err = capsys.readouterr()
	assert out == expected_stdout

def test_get_players_in_order_rejects_X_accepts_A(capsys):
	sys.stdin = open('mock/get_players_in_order_stdin_2', 'r')
	p1 = HumanPlayer('A')
	p2 = HumanPlayer('B')
	assert ui.get_players_in_order(p1, p2) == [p2, p1]


